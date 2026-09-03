# Hero Auto-Summon Pet (英雄自动召唤宝宝)

This note records reusable lessons from implementing an auto-summon feature for a hero pet (`英雄召唤圣兽` / "holy beast") in the 老登 project, where the engine does not natively auto-summon hero pets. It documents which hero-side commands and triggers exist in the manual, which ones turned out to be absent or unreliable on the real server, and the working slot-flag pattern that replaced them.

## The Feature and Its Constraints

Goal: when the hero has learned the summon skill, automatically keep N summoned pets alive, with pet level derived from hero level.

Design rules confirmed with the user:

1. Only summon when the hero has learned the skill (`英雄召唤圣兽`, Magic ID `76`, `Job=2` Taoist).
2. Cap the number of simultaneously summoned pets by hero level (40-49 = 1, 50-59 = 2, 60+ = 3).
3. Pet level = hero level mapped: level 40 -> pet 1, then +1 per 5 hero levels, capped at 7.
4. Do not summon past the cap.

## Official Facts (manual-backed)

- `832-英雄魔法触发功能.md` lists `[@HeroMagSelfFuncX]` (hero casts skill X on self), `[@HeroMagTagFuncX]`, `[@HeroMagTagFuncExX]`, `[@HeroMagMonFuncX]`. **These labels exist in the manual**, but the user's real server did NOT fire `[@HeroMagSelfFunc76]` for the hero summon skill. Treat manual-documented hero magic triggers as version-dependent and verify on the live server before relying on them.
- `712-英雄学习技能触发.md` documents `[@HeroLearnMagic]` firing in QFunction when the hero learns a skill, with `<$H.LearnMagicID>` holding the just-learned skill ID. This DID work and became the reliable skill-detection substitute.
- `366-英雄宝宝攻击触发.md` documents `@OnHeroSlaveDie` (hero pet death) and `<$H.DIESLAVENAME>` (dead hero pet name, digits NOT stripped). It also documents `@HeroSlaveAttack` / `@HeroSlaveMagicAttack` with `<$H.CurSlaveName>`.
- `502-检查英雄等级.md`: `CheckHerolevel 操作符(> = <) 级别`. `642-脚本变量大全.md` documents `<$H.LEVEL>` as the hero level variable.
- `390-召唤宝宝.md` (RECALLMOB) parameter `所属技能`: `3` = 圣兽. Format `RECALLMOB 怪物名 等级 叛变时间 颜色类型 颜色值 所属技能 数量`.

## Commands That Do NOT Exist (verified absence, do not invent)

These "hero-prefixed" commands were assumed from the manual's "hero commands usually add `H.`" convention (`807-天下第一雕像相关说明.md`, `811-...`), but **none of them exist in the engine**. Searching the full manual and the live server proved they are absent:

- `H.CHECKSKILL` — no hero skill-level check command exists. Use `[@HeroLearnMagic]` + `<$H.LearnMagicID>` + a saved flag instead.
- `H.CHECKSLAVECOUNT` / `<$H.SlaveCount>` / `H.CHECKSLAVENAME` — no hero pet count/name read command exists.
- `H.RECALLMOB` — **this one actually worked on the live server** (confirmed by repeated summon spam in the logs), despite having no manual page. It is the only "H.-prefixed" command of this set that proved usable.
- `H.KILLCALLMOB` / `H.CLEARSLAVE` — no hero pet kill/clear command exists. Overflowing pets can only be cleaned by the hero dying, map change, or GM `@kill`.

Rule: **"hero commands usually add `H.`" is a weak heuristic, not proof.** Verify each hero-side command against the manual or a live-server test before using it. When a command has no manual page and no project precedent, assume it does not exist until a real test proves otherwise.

## Why the First Attempts Failed (live-server observations)

1. `[@HeroMagSelfFunc76]` never fired -> moved to a per-player timer.
2. `H.CHECKSKILL` did not exist -> replaced with `[@HeroLearnMagic]` setting flag `[800]`.
3. `H.CHECKSLAVECOUNT` did not exist -> count guard never matched, timer summoned unconditionally -> overflow.
4. `P0`/`P` variables did NOT persist across `[@OnTimerX]` callbacks -> self-maintained counter always read as 0 -> overflow again.
5. Flat `#IF/#ACT` blocks are NOT mutually exclusive branches -> hero level 100 matched all seven level branches at once -> summoned pets of every level 7..1 in one pass.

## The Working Pattern: Slot Flags

Because there is no hero pet count read and P-variables do not survive timer callbacks, the count is represented by **dedicated personal flags as occupancy slots**:

- `[800]` = master has learned the summon skill (set in `[@HeroLearnMagic]` when `<$H.LearnMagicID>` equals the skill ID).
- `[801]` `[802]` `[803]` = three pet slots, `0` = empty, `1` = occupied. Higher hero levels open more slots (60+ uses all three, 50-59 uses two, 40-49 uses one).

Timer flow (`[@OnTimer7]` -> `#CALL` to the feature script):

1. Guard `CHECK [800] 1`, then `CheckHeroOnline`.
2. Find the first empty slot in the hero's level band and set it to `1`, then `GOTO` the summon label and `BREAK`. This makes each timer tick fill at most one slot, so it cannot overflow.
3. On `@OnHeroSlaveDie`, clear all three slots to `0` (we cannot tell which slot died, so clear all; under-summon is acceptable, overflow is not).
4. **On login (`[@Login]`), clear all three slots before starting the timer.** Personal flags are persistent; if a previous session left them `1`, the timer would see "all full" and never re-summon. This was the final bug the user fixed by hand.

## Arithmetic for the Pet Level (avoid flat #IF chains)

Deriving "level 40 -> 1, +1 per 5 levels, cap 7" must NOT be written as seven flat `#IF CheckHerolevel > N` branches, because those are sequential (not else-if) and all match at once. Use arithmetic instead:

```mir200
MOV N$圣兽等级 <$H.LEVEL>   ; hero level
DEC N$圣兽等级 40
DIV N$圣兽等级 5            ; integer division
INC N$圣兽等级 1
#IF
SMALL N$圣兽等级 1
#ACT
MOV N$圣兽等级 1
#IF
LARGE N$圣兽等级 7
#ACT
MOV N$圣兽等级 7
```

## Arithmetic Command Syntax (verified)

From `629-传奇脚本命令详解.md` and `001-翎风引擎历史更新记录.md` (~9402):

- `DIV N1 N2 N3` = N1 = N2 / N3 (three-arg); `DIV N1 数` = N1 = N1 / 数 (two-arg). Both are **integer division**.
- `MUL N1 N2 N3` = N1 = N2 * N3; `MUL N1 数` = N1 = N1 * 数.
- `MOV 变量 值` / `INC 变量 n` / `DEC 变量 n` likewise.
- **`DIV`/`MUL`/`MOV`/`INC`/`DEC` do NOT accept string variables.** Do not write `DIV N$X <$STR(N$X)> 5`; pass the bare variable name (`DIV N$X 5`) or a literal.
- `SMALL 变量 数值` (less-than), `LARGE 变量 数值` (greater-than), `EQUAL 变量 数值` (equal). Argument order is **variable first, value second**.

## Encoding / Line-Ending Pitfall

PowerShell and many Python writers emit LF line endings by default. LF-engine scripts require CRLF. When writing `.txt` scripts under `Mir200/Envir/**`, verify CRLF and GBK (no BOM) after writing; stray LF or UTF-8 bytes can cause garbled reads or load failures.

## Guardrails

- Personal flags `[n]` persist across login and are reliable across `[@OnTimerX]` callbacks (unlike `P0`). Use them for cross-callback occupancy/state. Reset them explicitly on login and on the relevant death/teardown trigger.
- Do not rely on `[@HeroMagSelfFuncX]` firing for hero skills; if it must drive summoning, verify on the live server first. `[@HeroLearnMagic]` is the dependable learn-time hook.
- Over-summoning is the dangerous failure; under-summoning is acceptable. Bias cleanup toward clearing more state (clear all slots) than toward precise slot bookkeeping when the engine cannot report which slot died.
- There is no script-side way to delete an already-summoned hero pet. Overflow must be cleaned by the hero dying, changing map, or a GM kill.
