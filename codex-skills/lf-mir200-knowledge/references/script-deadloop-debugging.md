# Mir200 Script Dead-Loop Diagnosis

Use this reference when the server repeatedly logs `[脚本死循环]`, especially when the reported NPC is `QManage`, the reported command is `GOTO @label`, or the failures began after a refresh/login chain grew.

## Core Distinction

The same log surface can represent two different failures:

- **True unbounded cycle:** the active call path can repeatedly reach a label already on that path without a mandatory counter, state transition, guard failure, or terminal action that forces convergence, such as an unguarded `@A -> @B -> @A` or `GOTO @A` self-call.
- **Jump-budget exhaustion:** one legitimate entry executes more `#CALL`/`GOTO` transitions than the effective `!Setup.txt` limit allows. The path may be acyclic or may contain a provably bounded loop whose finite iteration count is still too large.

Do not propose a fix until this distinction is established. A reported command such as `GOTO @刷新图标` identifies where the engine stopped, not necessarily where the fault began.

## Evidence Levels

Official manual behavior:

- `GOTO @label` transfers execution to a label. The documented parameter form can return values with `RETURN`, and the manual states that `RETURN` is equivalent to `BREAK` for ending that script segment.
- Recursive `GOTO` is explicitly shown as a stack-overflow risk; the manual recommends `While` / `EndWhile` for intentional loops.
- `SetOnTimer index seconds` with no execution count repeats without limit until `SetOffTimer`; an explicit third argument limits the number of executions.
- Older update notes document `ScriptGotoCountLimit` as a script-loop limit.

Local manual anchors:

- `knowledge_base/chapters/100-循环脚本.md`
- `knowledge_base/chapters/163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`
- `knowledge_base/chapters/205-个人定时器.md`
- `knowledge_base/chapters/362-循环脚本运行次数设置.md`
- `knowledge_base/chapters/629-传奇脚本命令详解.md`

Project/engine observations that must be verified locally:

- A source `#CALL` may be surfaced by the runtime log as `命令:GOTO @label`. Therefore, the log word `GOTO` is not sufficient evidence that the source line was a literal `GOTO`.
- Newer layouts may also contain `LimitScriptGotoCount`. When both keys exist, runtime behavior may follow the newer/later low value even if `ScriptGotoCountLimit` is much larger.
- Same-file `#CALL` and `GOTO` can both contribute to the engine's script-transition accounting. A spelling-only conversion is not evidence of reduced work.

Keep these observations labeled as project-derived unless the exact engine version's manual confirms them.

## Static Investigation Workflow

1. Preserve the exact timestamp, NPC, map position, and every reported target label. Labels reported in the same second often belong to one larger entry path.
2. Find every source occurrence of each target label and every caller of it. Search both `#CALL ... @label` and `GOTO @label`.
3. Identify the real entry labels, especially `[@Login]`, `[@OnTimerX]`, `[@OnTimerExX]`, combat callbacks, and `QFunction-0.txt` callbacks.
4. Inspect the first bad commit and all attempted fixes. Count newly added calls, not only newly added labels or action lines.
5. Build a directed call graph. A node is `file + label`; an edge is a `#CALL` or `GOTO` that can transfer to another label.
6. Run an active-stack cycle check. A back-edge to a node already on the current path proves a structural cycle, but not yet an infinite one. Inspect its guards and state writes to determine whether every traversal must converge. Revisiting a label from a separate completed branch is not a back-edge.
7. Count the transitions on each legitimate entry. Include sequential sibling calls after a called label returns and multiply provably bounded cycles by their maximum iteration count; graph depth alone undercounts both cases.
8. Read all occurrences of `ScriptGotoCountLimit` and `LimitScriptGotoCount` with line numbers. Do not assume the first key or the largest value is effective.
9. Inspect every timer start and stop. Confirm interval, optional execution count, start frequency, and whether the handler performs a full recalculation every tick.
10. Compare the measured legitimate transition count with the effective limit. If failures consistently begin near that boundary and every structural cycle is absent or provably bounded, classify the fault as budget exhaustion.

An indefinitely repeating timer is not automatically a same-stack infinite cycle: separate timer ticks can be separate entries. It is still a serious load amplifier, and each tick can independently exhaust the per-entry jump budget.

## Repair Strategy

For a true cycle:

- Remove or guard the back-edge.
- Use `While` / `EndWhile` for bounded intentional iteration when supported by the local engine pattern.
- Ensure every terminal/failure branch ends at the intended scope with `BREAK` or documented `RETURN`.
- Add a static cycle-classification check for the affected modules so unbounded and provably bounded back-edges are reported separately.

For jump-budget exhaustion:

- Reduce repeated work first. A periodic equipment/buff timer should normally check only whether the slot is empty, whether the item identity changed, or whether a dirty flag is set.
- Run the full refresh on login, item change, death/revival recovery, explicit state changes, and other real lifecycle events rather than on every timer tick.
- Before removing the old full-refresh call, inventory everything that depended on its cadence. Explicit-duration `ChangeHumAbility`, `AddHumNewValue`, `ChangeSpeed`, and `ChangeState` commands need a lightweight unchanged-state renewal path; cooldown decrement, pet replacement, periodic healing, and similar tick-driven behavior need an intentional periodic path too.
- Keep the renewal path separate from the full refresh. It should use cached, already validated module state, renew only the active class/direction contributions, and avoid config parsing, icon rebuilding, module open/close, or other deep call chains that caused the original budget failure.
- Clear the dirty flag after a successful full refresh and during defensive cleanup. If the local script must clear it at refresh entry to prevent re-entry, every failure/abort path must set it again so the next timer tick can retry.
- Raise the effective jump limit conservatively above the measured worst legitimate path. Keep a finite ceiling so genuine recursion is still stopped.
- Treat `!Setup.txt` changes as startup configuration; tell the operator that a Mir200 restart is required before runtime verification.

## Post-Repair Lifecycle Audit

A dead-loop repair is incomplete until the optimized timer preserves the old feature contract. Use this audit after replacing a repeating full refresh with an identity/dirty check:

1. Extract every command in the old refresh chain with an explicit duration. Treat the duration as a renewable lease rather than a one-time assignment.
2. Compare the heartbeat interval with the shortest lease. Keep the heartbeat shorter with margin for timer jitter; for example, a 2-second heartbeat can renew a 3-second lease, but skipping the unchanged-state renewal makes the effect disappear on the first expiry.
3. Map base contributions and direction-specific contributions separately. Verify that each route renews only its own attributes and cannot inherit another route's damage, resistance, accuracy, speed, or state effect.
4. Trace non-attribute cadence work independently: cooldown counters, summon replacement, periodic HP/MP recovery, pet recovery, stack decay, and delayed cleanup.
5. Revalidate the cheap path's assumptions. If job, mode, stage, or another eligibility condition can change without changing the item name, recheck that condition before renewal; on failure, clean up or request a full refresh.
6. Keep removal behavior explicit. Unequip, drop, durability loss, invalid job, and invalid item should stop the timer and cleanup; death/revival behavior must follow the feature design rather than being inferred from ordinary unequip behavior.
7. Recount the new call path and run the cycle check again. A lightweight dispatcher can still recreate a cross-file cycle if a module calls back into the full refresh.

Do not solve this regression by simply removing all duration arguments. Online-indefinite assignments require complete, contribution-safe cleanup, and broad `= 0` resets can erase values owned by unrelated systems.

If the user/operator authorizes runtime verification of an ambiguous effective config key, change only one candidate key at a time, restart Mir200, and compare the failure boundary. Do not simultaneously alter both keys and the call chain, because that destroys the evidence needed to identify the effective setting.

For mixed failures, remove the real cycle before increasing any limit. A larger budget only delays a genuine recursion failure.

## Mismatched `{ }` Block Nesting and Label Fall-Through

Two additional project-observed root causes that look like recursion but are not:

- **A single `{ }` block spanning multiple labels.** In the engine, `{`/`}` delimit a callable script block. If one `{` opens under `[@A]` and the matching `}` only closes after a second label `[@B]` was declared inside it, the labels are nested inside one block. A `#CALL ... @B` (or falling into `@B`) then cannot return cleanly when the outer `}` closes, and the engine's transition accounting reports a dead loop. Fix: each label must own a balanced `{ }` pair, or drop the braces and use the flat label layout with `BREAK`/`#ELSEACT BREAK` terminals.
- **A conditional `#IF` with no `#ELSEACT`/`BREAK` falls through into the next label.** When `#IF` is false and there is no `#ELSEACT` (and no `BREAK`), execution continues into whatever label/segment follows, which can re-enter a sibling `#CALL` target and create a convergence failure. Fix: give conditional blocks an explicit `#ELSEACT BREAK` (or a `BREAK` terminal) so a failed guard stops instead of falling through.

Observed instance: `AutoRunRobot HOUR 1 @英雄偶遇` → `RobotManage [@英雄偶遇]` → `#CALL 随机英雄NPC.txt @英雄偶遇` → `#CALL @生成英雄引路人`, where `随机英雄NPC.txt` wrapped both labels in one `{ }` pair and the first label had no else-terminal; the log read `[脚本死循环] NPC:RobotManage ... 命令:GOTO @英雄偶遇`.

## Failed Fix Patterns

- **Bulk `#CALL` to `GOTO` conversion:** changes syntax without proving fewer transitions and risks altering established return/dispatch behavior.
- **Adding `BREAK` everywhere:** useful only when fall-through or a missing terminal is the cause; it does not shorten calls that already return correctly.
- **Timer registration flags only:** preventing duplicate registration does not make an already infinite repeating timer cheaper.
- **Changing only `ScriptGotoCountLimit`:** may edit a legacy key while `LimitScriptGotoCount` remains the effective low limit.
- **Setting an enormous limit first:** masks evidence and weakens protection against actual recursion.
- **Fixing only the first logged label:** the first rejected transition is often downstream of the expensive entry chain.

## Static Regression Checks

A focused checker should verify:

- every same-file and cross-file `#CALL` target file/label exists, and every `GOTO` target label exists;
- no reachable back-edge is unbounded; any allowed bounded back-edge has an explicit monotonic state change and finite upper bound;
- the effective jump-limit key exists and is within the intended finite range;
- high-frequency `QManage` timers call lightweight check labels rather than unconditional full-refresh labels;
- every explicit-duration effect from the old full-refresh chain has an unchanged-state renewal counterpart under the correct class/direction guard;
- every cooldown, summon, periodic heal, or other cadence-dependent action intentionally remains reachable after the timer optimization;
- unchanged-item fast paths revalidate eligibility fields that can change independently of item identity, such as the player's current job;
- dirty flags are set by lifecycle events and cleared by full refresh and cleanup;
- timer start/stop pairs and callback label numbers match;
- restored/unrelated scripts have no content diff;
- Mir200 script encoding, BOM state, and line endings remain unchanged.

Run the focused checker before broad legacy checks. If a broad checker still fails, separate pre-existing balance/content findings from dead-loop findings instead of claiming all checks pass.
