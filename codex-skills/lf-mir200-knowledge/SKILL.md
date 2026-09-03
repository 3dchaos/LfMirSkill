---
name: lf-mir200-knowledge
description: Use when answering or modifying LF/LFM2/翎风引擎 Mir200 server scripts, NPC scripts, MapInfo, MonGen, MerChant, QuestDiary, Market_def, Robot_def, item rules, command syntax, or engine help-document questions using the local Markdown manual, sample Mir200 directory, and learned script patterns.
---

# LF Mir200 Knowledge

## Overview

Use the included LF engine manual as the syntax source of truth. When a local `样本Mir200` server sample is available, search it before answering and prefer its examples for project-specific implementation patterns. Cite local file paths and distinguish official manual behavior from sample-derived observations.

This skill also learns a local script-thinking model from real sample files. The model is regenerated from the sample scripts and should be treated as a living summary of how Mir200 scripts are structured in practice.

The skill includes a generated training course. Use it to practice on real sample scripts in a progressive order before making broad claims or designing complex script changes.

Do not compile, launch, or run the Mir200 server. Perform static analysis only unless the user explicitly changes that constraint.

## Locate The Knowledge Root

The root is the directory containing:

- `knowledge_base/index.md`

`样本Mir200/` is optional local material. It is not included in the public skill package because it may contain private server files.

When paths are not obvious, run:

```powershell
python <skill-dir>\scripts\lf_kb.py --root <root> validate
```

If the root moves, either pass `--root` or set `LF_MIR200_KB_ROOT`.

## Standard Workflow

1. Run `update` when the manual, sample scripts, or indexes may be stale.
2. In a real project repo, read the nearest `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` first, then relevant project docs such as `docs/*.md` named by the user or matching the feature.
3. Search the manual for command syntax and official behavior.
4. If `样本Mir200` exists, search it for working examples; otherwise mark sample-derived conclusions as unavailable.
5. Read `references/mir200-training.md` when learning or improving the skill from examples.
6. Read `references/mir200-thinking.md` for the current local script-thinking summary.
7. Read `references/script-deep-dives.md` when the user names a specific script to study deeply.
8. Read `references/script-parameters.md` when the request involves labels or UI links written like `@标签(参数)`, `<$SCRIPTPARAM*>`, `CHECKSCRIPTPARAM`, or `GOTO @label(args|returns)`.
9. Read `references/envir-config-rules.md` when the request involves `Envir` `.txt` / `.ini` configuration tables rather than only NPC dialog scripts.
10. Read `references/envir-config-deep-dives.md` when the user names a specific `Envir` configuration file to study deeply.
11. Read `references/sample2-feature-buffs.md` when the request involves `样本2Mir200`, feature buffs, awakening seals, flow-school builds, inscription-like custom properties, pet contracts, special hidden attributes, or build-oriented buff systems.
12. Read `references/mir200-256-colors.md` when the request involves color values, `0-255` palettes, `/SCOLOR`, `{text|color}`, equipment name colors, item remarks, set remarks, custom item text colors, custom attributes, progress bars, monster name colors, or low-to-high rarity color presets.
13. Read `references/script-deadloop-debugging.md` when logs report `[脚本死循环]`, repeated `GOTO` failures, `QManage` timer failures, or a script starts failing after its refresh/call chain grows.
13a. Read `references/hero-autocall-slave.md` when the request involves hero pets/babies (`RECALLMOB` for heroes, `H.RECALLMOB`, `CHECKSLAVECOUNT`, `H.CHECKSKILL`, `@HeroLearnMagic`, `@OnHeroSlaveDie`, `@HeroSlaveAttack`, hero summon skills), hero pet count/occupancy, or auto-summon features.
14. Inspect the most relevant project files before making claims or edits.
15. For code/script edits, preserve original encoding and style, and modify only the requested files.
16. Validate statically after edits with `validate` and targeted searches.

## Durable Mir200 Rules

- Read Mir200 project text as ANSI by default. If the result is garbled, retry UTF-8. Preserve the original encoding when writing files back.
- `[@OnKillMob]` requires the target map to include `ONKILLMON` in `MapInfo.txt`.
- `[@KillMon]` does not require `ONKILLMON`; do not confuse it with `[@OnKillMob]`.
- Boss or first-kill logic must match the full monster name from `MonGen.txt`. Do not silently ignore numeric, bracketed, or other suffixes.
- When the same monster name appears on multiple maps, also check the current map and the relevant stage/state variable before changing global progress.
- When classifying monsters as Bosses from project data, cross-check `MonGen.txt` spawn density with the monster database (commonly `Mud2/DB/GEEM2.db`, table `Monster`). Treat the result as a heuristic unless the project has an explicit Boss list.
- A strong Boss candidate is usually in the top one or two level tiers on its map, has scarce spawns or long refresh, and has high HP/attack/defense relative to other monsters on that map. Names containing `教主`, `魔王`, `恶魔`, `尸王`, `[BOSS]`, `暗之`, `触龙神`, `黄泉`, `双头`, `蛛王`, `地藏王`, `重装使者`, or `王` are supporting evidence, not proof by themselves.
- Keep a separate "elite/head" bucket for high-level scarce monsters such as `卫士`, `将军`, `祭司`, `[精英]`, `[头目]`, `[狂化]`, or region variants. Do not automatically apply Boss-only balancing to these unless map context confirms they are the top rare encounter.
- Exclude obvious functional or guard monsters from Boss inference, such as city `弓箭守卫`, `恶魔弓箭手`, trainer/test monsters, and other non-hunting utility actors, even if their level is high.
- When balancing monster stats, classify by exact monster name as stored in the DB and spawned in `MonGen.txt`; do not merge suffix variants such as `牛魔王`, `牛魔王8`, `沃玛教主`, and `沃玛教主1`.
- In `MapInfo.txt`, lines like `0 308,264 -> 0102 3,7` are map links: stepping on source map `0` at X308 Y264 sends the player to target map `0102` at X3 Y7. Coordinates may be written as `X,Y` or `X Y`; parse both.
- Map links are directional. Do not assume a return path exists unless a separate reverse link is present, often on a neighboring coordinate.
- For dynamic map links, prefer documented engine commands over guessed syntax. The local manual documents `ADDMAPGATE`, `DELMAPGATE`, and `GETMAPGATE` in `knowledge_base/chapters/049-动态地图连接.md`; use that chapter before generating dynamic links.
- For staged map-opening designs, block every entry path, not only NPC teleport menus: `MapInfo` links, `MAPMOVE`/`MAP`/`MAPS`/`GROUPMAPMOVE`, recall and exchange-map commands, dynamic maps, activities, item teleports, random movement, reconnect/death/respawn paths, robot scripts, and GM/admin bypasses.
- `Market_def/QMission-0.txt` is a special task-page display script. Do not build current-state display pages by `GOTO @label` dispatch; in this context `GOTO` can fail to show the target content. Use menu links like `<当前世界进度/@世界当前进度>` and put each conditional `#SAY` branch directly under the selected label, ending matched branches with `#ACT` / `BREAK`.
- `Envir` `.txt` and `.ini` files are not one grammar. Before parsing or editing, classify the file family: map table, monster spawn table, NPC placement table, map event table, robot schedule, drop list, allow/deny list, sectioned recipe, wide item-rule row, or INI section/key file.
- In configuration tables, path and file name often carry runtime meaning. Do not guess target scripts or data files from display names alone; follow `MerChant.txt`, `Npcs.txt`, `Robot.txt`, `AutoRunRobot.txt`, `MapEvent.txt`, `MonItems/<monster>.txt`, `SmartMonster/<monster>.ini`, and `UserData/CustomSkill/<id>.ini` registration rules.
- Preserve optional-field positions in whitespace tables such as `MonGen.txt`. If a later optional field is needed, keep placeholder values for earlier optional fields instead of shifting columns left.
- Treat semicolon comments in config files as inactive data but useful schema hints. Empty list files and empty config directories can be intentional placeholders; do not remove them or infer a feature is impossible solely because the sample has no active rows.
- `TzItemDescList.txt` controls player-facing set remarks, not the actual set effects. Cross-check `GroupItemList.txt` before claiming required pieces or numeric effects; parenthesized comma groups in remarks are same-slot alternatives, not additional required pieces.
- `GroupItemList.txt` and `GroupItemSkillPowerList.txt` are the runtime set-bonus sources. Preserve every `|` zero placeholder in their fixed arrays, link skill-power sections by set ID, and use `TzItemDescList.txt` only as display cross-check.
- `ItemRuleList.txt` is the runtime item-rule table behind M2 `列表信息2 -> 物品规则`; `ItemDescList.txt` is player-facing item remark text. Do not infer trade/drop/repair/storage restrictions from remarks alone; cross-check the rule table, script triggers, and project deny lists.
- In `样本2Mir200`, feature buffs are usually a chain rather than a single file: `MerChant.txt` entry -> flow/feature NPC -> `QFunction-0.txt` callback -> `QuestDiary/游戏登陆/登陆脚本.txt` recalculation label -> attack/skill trigger -> item/set display table. Follow that chain before claiming a buff, inscription, or hidden property is active.
- For `样本2Mir200` flow-school and awakening systems, treat `QuestDiary/游戏登陆/流派BUFF读取.txt` as dispatch and `QuestDiary/游戏登陆/登陆脚本.txt` as the stat recalculation hub. Feature scripts should mutate state, then call only the affected readers such as `@_@元素读取`, `@_@攻魔道读取`, `@_@HPMP读取`, `@_@防御读取`, `@_@攻速读取`, `@_@施法速度`, `@_@吸血读取`, `@_@技能等级读取`, `@_@技能威力读取`, or `@_@BB读取`.
- For `样本2Mir200` timed buffs and debuffs, pair every stat-affecting `SetArrBuff` with a `[@CloseArrBuffX]` cleanup that clears the marker/counter and reruns affected readers. Persistent buffs such as `苹果`, `满江红`, and `幸运药水` store expiry state and rebuild icons after login; the icon itself is not the source of truth.
- For equipment-slot driven persistent buffs, confirm the equipped position before refresh and before combat procs, use `SetArrBuff` parameter 5 as `-1` for non-countdown self icons, and close the auto-arranged icon by button number only, for example `CloseArrBuff 87` for `SetArrBuff 1 87 ...`; do not use the group+button form `CloseArrBuff 1 87` for this project pattern.
- For equipment-slot driven persistent buffs, treat unequip, item drop, durability exhaustion, script-side removal, death checks, login refresh, and timer refresh as one lifecycle. A missing or changed equipped item must close the module, clear feature variables, stop the refresh timer, and close the icon before any later refresh can rebuild it.
- For hero equipment-driven persistent buffs, treat the hero's equip/unequip/login/death/timer/attack/struck path as one lifecycle, not as isolated callbacks. Keep hero state in its own `N$英雄*` / `S$英雄*` namespace, refresh from `@HeroTakeOnEx`, `@HeroTakeOffEx`, `@HeroLogin`, `@HeroDie`, `@HeroStruckDamage`, and `@HeroAttackDamage`, and clear timers plus cached state when the 14-slot item changes or disappears.
- `H.ChangeHumAbility ... 3` is a lease, not a permanent write. If the effect must stay up, give it a dedicated renewal timer and rebuild path; do not assume a one-time refresh will survive the engine's own periodic recalculation.
- In this project, `LockUpdateAbil` can stall hero or pet movement if it is held across a long refresh chain. Keep any lock scope as small as possible, pair it with the immediate `UpdateAbil`, and prefer lock-free refreshes when a feature only needs a final assignment.
- When Mir200 reports `[脚本死循环] ... 命令:GOTO @label`, do not treat the named label or the word `GOTO` as proof of a recursive cycle. First reconstruct the complete entry path through `QManage`, `#CALL`, and `GOTO`, then distinguish an unbounded cycle from a legitimate path that exceeded the configured jump budget; that path may be acyclic or contain a provably bounded loop. Follow `references/script-deadloop-debugging.md`.
- Audit both `ScriptGotoCountLimit` and `LimitScriptGotoCount` when they coexist in `!Setup.txt`. Their effective behavior can be engine-version-specific; a large legacy value does not prove that a later low limit is inactive. Keep the effective limit finite and only raise it above the measured legitimate path after reducing avoidable high-frequency work.
- Do not bulk-convert same-file `#CALL` statements to `GOTO` as a dead-loop fix. The manual documents `GOTO` label dispatch and callback-style `RETURN`, and project logs may report called labels as `GOTO`; changing the spelling does not prove that recursion or jump-budget consumption was reduced. Preserve established call semantics unless a verified engine rule requires a conversion.
- `SetOnTimer` without an execution-count argument repeats indefinitely until `SetOffTimer`. High-frequency handlers should perform a cheap state check and call the full refresh only when the equipped object changed or a lifecycle event set a dirty flag. Adding `BREAK` or preventing duplicate timer registration does not reduce the work performed by an already repeating timer.
- When replacing a repeating full refresh with a dirty check, audit every explicit-duration effect and recurring action that the old refresh was renewing. Treat `ChangeHumAbility`, `AddHumNewValue`, `ChangeSpeed`, and `ChangeState` time arguments as leases: keep the full refresh for state changes, add a small unchanged-state renewal label for leases and intentional periodic work, and stop the timer on cleanup so leases expire naturally. Do not make effects indefinite unless every removal path can safely remove only that feature's contribution.
- For buff/head-icon art resources, verify the resource table's index base before writing script numbers. In 老登军鼓, `EffectImageList.txt` image-file references were corrected to start from `0`, so `SetArrBuff`/`SETICON` file indexes should follow the local table rather than assuming `1`; clear stale icons before rebuilding (`CloseArrBuff`, `SETICON n -1`) and do not put chat `SENDMSG` or branch-stopping `BREAK` inside refresh/helper paths where timer refreshes or later description branches still need to run.
- Keep player-facing `SetArrBuff` hover text and `ItemDescList.txt` remarks at the gameplay layer: equipped slot, direction/build, trigger skills, visible effect, quality unlock, and player feedback. Do not expose developer-maintenance details such as refresh intervals, temporary stat durations, audit/recheck wording, cleanup internals, script recovery, or diagnostic records unless the surface is explicitly GM/admin-only.
- For feature proc chat feedback, use the project quiet flag that already controls similar player notices. In the 老登 project,军鼓 proc printing uses flag `[63]`; do not accidentally reuse unrelated quiet flags such as `[61]` without checking local helper scripts.
- For target-side debuffs in `样本2Mir200`, use the target prefix consistently (`M.` or named-player prefix), write a target-side marker such as `S$咒蛊术`, show the target-side buff icon, and force target-side recalculation. Sample patterns include `咒蛊术`, `体态压迫`, `撕裂`, `失心锁`, and `邪爆符`.
- For assignment-style commands that overwrite a whole attribute, such as `ChangeSpeed` or `H.CHANGESPEED`, never let login, equipment, buff, or feature scripts write competing final values. Keep one contribution variable per source, reset/recalculate the aggregate whenever state changes, and issue one final assignment per script subject. A player uses `ChangeSpeed`; a hero uses `H.CHANGESPEED`; these are separate subjects and each needs its own final-write label. When a feature is removed, set its contribution back to `0` and call the same aggregator; do not undo it by assigning only a base value in another branch.
- For script multiplier commands that set a whole rate, such as `KILLMONEXPRATE`, `POWERRATE`, and `KILLMONBURSTRATE`, separate overwrite sources from additive element sources. Activity, consumable, title/rank, and permanent-code benefits should write their own contribution variables and call one final settlement label that applies the winning/aggregate command value. Equipment, drum, and hidden-element bonuses that the manual defines as additive, such as `AddHumNewValue 26` kill-exp rate or `AddHumNewValue 11` kill-drop rate, should stay in the additive layer instead of issuing another direct multiplier command.
- For attack-speed balance implementations, store profession-base and route/buff contributions separately, for example `N$职业基础攻速`, `N$路线攻速`, and `N$最终攻速`, combine them with documented `FORMULATION`, and make login, refresh, route switching, and cleanup call the same recomputation label. Guard the recomputation by the intended subject/job first so non-target classes never fall through to a zero-value final write. Feature modules may update their contribution, but must not add another direct `ChangeSpeed 2` or `H.CHANGESPEED 2` assignment.
- For feature-buff skill coverage, query the project `Magic` table instead of relying on memory or familiar Mir skill lists. Only player skills present in the project DB should become player-facing promises; hero-only names such as `英雄群雷术` must not be advertised as player route triggers unless the design explicitly targets heroes.
- For feature buffs that need a visible monster-side state, prefer documented target/effect commands over fake skill casts. `RangeHarm` can apply damage plus state to only monsters with parameter 8 set to `2`; use documented effect codes such as `8` for ice/freeze and `10` for red poison when a full-stack route should visibly mark affected monsters without releasing persistent skills like `火墙`.
- For compensation pets or route-summoned babies, choose exact monster names from the project `Monster` table, compare their level/HP/attack to native summon pets, and avoid reusing over-strong or core class summons unless intended. Gate every `RECALLMOB` with `CHECKSLAVECOUNT` by exact compensation-pet name, add an explicit cooldown variable, and clean route-owned pets with `KillCallMob` when the route is closed or switched.
- For `ChangeState`, first identify the current script subject. An unprefixed `ChangeState` applies to that subject, not automatically to the current attacker or current target; in `[@Struck]` / `[@StruckDamage]` callbacks it usually affects the struck player. Use documented prefixes such as `M.`, `H.`, `FS.`, or `BB.` only after confirming the intended target context.
- `ChangeState` effect codes from the manual are `1` 石化, `2` 冰冻, `3` 蛛网, `4` 红毒, `5` 绿毒, `6` 定身, `7` 瘫痪, `8` 禁锢别人, `9` 防禁锢, `10` 吸血, `11` 吸蓝, `12` 禁锢自己, `13` 间隔掉血, and `14` 禁止使用技能. For effects `1-5`, parameter 3 controls whether corresponding resistance/prevention is checked (`0` no check, `1` check); setting time to `0` clears the state. Equipment-driven procs must still guard equipped item/slot, job, source object, chance, and cooldown before calling it.
- In `样本2Mir200`, "铭文" or hidden-property analysis must cross-check at least `CustomItemPropertyTextVarList.txt`, `ItemDescList.txt`, relevant NPC scripts, `QFunction-0.txt`, attack triggers, `GroupItemList.txt`, `GroupItemSkillPowerList.txt`, and `SkillPowerItemList.txt`. `ItemDescList.txt` is a discovery surface, not proof of runtime effect.
- Mir200 color values are numeric palette IDs from `0-255`, not arbitrary RGB input. For color work, use `references/mir200-256-colors.md` and the official color-related chapters before choosing numbers.
- The local `256色值` source skips color `32`; do not use `32` for new scripts unless another official project source confirms its meaning. Color `255` appears as a white final table cell without explicit HTML `bgColor`, so prefer confirmed `246`/`254` when exact white text is not required.
- Sample-backed readable presets include `218` for item remarks, `223,249` for active/inactive set remark states, `116` for equipment or set item names, `250` for positive/success values, `249` for danger/inactive/Boss warning, `251` for yellow headlines or timers, `253` for magenta rare callouts, and `254` for cyan labels.

## Project Knowledge Workflow

When working inside a Mir200 repo, build a small project model before editing:

1. Read the repo instruction file, usually `AGENTS.md`, for encoding, compile/run limits, ownership boundaries, and static checks.
2. Read user-mentioned design docs, then search `docs/` for nearby specs if the request references a feature name.
3. Extract durable facts into the working notes: stage variables, map groups, key entry scripts, trigger labels, manual chapters, and validation commands.
4. If those facts are reusable beyond one task, update this skill or a reference file with the rule, not the session narrative.
5. If a Mir200 project uses both HTTPS and SSH remotes for the same GitHub repo and HTTPS fails with `Failed to connect to github.com port 443`, verify the branch and remote URLs, then push the same branch through the configured SSH remote instead of changing code or rewriting history.

## Script Deep Dive Workflow

When the user names one Mir200 sample script for deep learning:

1. Run `learn-script` on that file first.
2. Read the report in this order: labels, calls, flags, input controls, item boxes, timers, variables, manual topics, learning notes.
3. Cross-check every reported manual topic against the official chapter before turning it into advice.
4. Promote only repeated findings into `mir200-thinking.md` or this skill.
5. Record script-specific observations in `references/script-deep-dives.md`.
6. Keep the training artifact small and reusable; do not copy the full script into the skill.

For this repository pattern, remember these reusable lessons:

- `Mir200/Envir/**/*.txt` is commonly GBK/ANSI and must be edited with encoding-preserving tools.
- `AGENTS.md`, `docs/`, and knowledge Markdown are maintained as UTF-8.
- For staged map opening with `G0`, natural `MapInfo.txt` links from lower-stage maps to higher-stage maps are potential bypasses; parse them directionally.
- Dynamic replacement links should be cleaned before regeneration (`DELMAPGATE`), then rebuilt only for stages allowed by the current `G0` (`ADDMAPGATE`).
- Startup or environment initialization may affect global variables, so dynamic stage-dependent links should be refreshed after initialization and after successful stage progression.
- `Robot.txt` only binds a robot name to `Envir\Robot_def\AutoRunRobot.txt`; `AutoRunRobot.txt` entries are resolved through `Envir\Robot_def\RobotManage.txt`, so a new scheduled tag needs a matching `[@tag]` in `RobotManage.txt` that then `#CALL`s the real script.
- For dynamic NPCs created by `CreateNPC`, keep the script in `Market_def`. If the last argument is `1`, the script file name omits the map suffix (`英雄引路人.txt`); if it is `0`, the script file name keeps the suffix (`英雄引路人-3.txt`).
- For shared feature modules that are called by many NPC scripts through `#CALL [系统功能\xxx.txt] @label`, this project may require a minimal wrapped call-file layout: only the first label needs a `{` immediately beneath it, and the file only needs one matching `}` as the final meaningful line. Do not add braces around every later label or "balance" each label locally. Preserve or opportunistically normalize this wrapper when editing nearby call files, and keep NPC files as thin menu entries that only dispatch to shared labels.
- LF script #IF starts an independent condition block. A following #IF is not automatically protected by the previous failed condition; failed prerequisite checks must use #ELSEACT BREAK (and optional #ELSESAY) to stop fall-through. For paid random attempts, write one block for CHECKITEM with failure reason and BREAK, put TAKE in that block's success #ACT, then start a separate #IF RANDOM ... block.
- Do not invent variable prefixes. Before using a custom form, confirm the variable family from the manual or samples first; `R$...` is not a documented list variable in the current evidence.
- Variable scope and persistence come from `628-程序变量说明.md`: `G`/`A` are global and saved, `I` is global but reset on restart, `P`/`D`/`M`/`N`/`S` are private temporary families with different reset points, and `U`/`T`/`J`/`Z` are private saved or daily-reset families. Choose the family by required lifetime, not by name convenience.
- `S$...` and `N$...` are documented extended character/number variables in `788-扩展字符变量S和数字变量N.md`. Use `<$STR(S$变量名)>` / `<$STR(N$变量名)>` when passing their values as command parameters.
- `L$...` is the documented array/list variable family in `192-多元数组元素变量.md`. Assign whole arrays with brackets, for example `MOV L$地图列表 [0,1,D1002]`; read with `<$STR(L$地图列表[0])>`; read by dynamic index with `<$STR(L$地图列表[<$STR(N$下标)>])>`.
- For gameplay dialog, decide which numbers are player-facing before writing `MESSAGEBOX`, `SENDMSG`, or `#SAY`. Show costs, rewards, required materials, remaining counts, and clear failure reasons when players need them for decisions; keep tuning knobs such as PK thresholds, punishment increments, probability cuts, timer tick counters, and maintenance details as internal script data unless the UI is explicitly GM/admin-only. Prefer diegetic outcome text such as "罪证被加重" over exposing formulas like "PK值+160" when the exact number is not needed.
- For repeatedly tuned gameplay numbers such as PK limits, single-attempt penalties, prices, reward bounds, cooldown ticks, and probability thresholds, assign them once to local extended variables near the entry or settlement label, for example `Mov N$红名PK值 200`, `Mov N$黄名PK值 160`, and `Mov N$一次PK值 40`. Use `<$STR(N$变量名)>` everywhere in checks, changes, messages that need exact values, and final guard branches so later balance changes do not require hunting scattered magic constants.
- For unlockable player features, trace the whole feature chain before editing: task-page hint (`QMission-0.txt`) -> teaching NPC -> saved personal flag (`CHECK [n]` / `SET [n]`) -> shared feature script guard. Keep the real action label guarded even if the menu only appears after learning, and mirror completion text in the task page.
- For crime/risk systems driven by PK value, cross-check `CHECKPKPOINTEX` with `CHANGEPKPOINT` chapters, keep thresholds and penalties in local `N$` variables, and make final punishment guards catch both `=` and `>` threshold cases. Do not let helper/挂机 features bypass the same crime policy without an explicit design exception.
- For金币 checks, use the documented condition command `CHECKGOLD 数量`, for example `CHECKGOLD 20000`. Treat the following `#ELSEACT` as the insufficient-gold path. Do not invent `CHECKITEM 金币` checks or prefer raw `<$GOLDCOUNT>` comparisons when `CHECKGOLD` expresses the guard.
- `GetStringPosEX` is a condition command: put it under `#IF`, not inside `#ACT`. Its path flag must match the path form (`0` for paths such as `..\QuestDiary\...`, `1` for absolute paths). When it returns a delimited config row to an `S$` variable, split that row with the documented `ExtractStringEx` command instead of relying on `GetListString` to fill more than two output variables.
- For random in-script list choice, use `MOVR` to generate an index, then read `L$` by that index. The sample `样本Mir200/Envir/Market_def/酒馆/翔天-3.txt` uses `MOV L$合英雄 [...]`, `MOVR N$抽44 0 5`, then `GIVE <$STR(L$合英雄[<$STR(N$抽44)>])> 1`.
- Do not invent function-style constants such as `<$MAPTITLE(<$STR(A91)>)>`. The manual documents `<$MapTitle>` as the current player's map name and `<$HMapTitle>` as the hero's current map name in `knowledge_base/chapters/642-脚本变量大全.md`; it does not document a parameterized map-code-to-title function. When a script randomly chooses a destination map code and must announce its display title, derive the title from confirmed project data, for example by maintaining a same-index `L$` display-name list beside the same-index `L$` map-code list built from `MapInfo.txt`.
- `RANDOM n` is a condition/probability gate, not a value assignment tool, and in Mir-style scripts it is commonly used as a `1/n` chance gate. Do not feed a percent-style variable such as `15/25/35/45` directly into `RANDOM`, because larger values lower the chance. For positive percentage gates, use the documented `RANDOMEX 子 母`, for example `RANDOMEX <$STR(N$触发几率)> 100`; use `MOVR` when a numeric random value must be stored.
- For mutually exclusive percent outcomes with a stored random value, draw `MOVR N$随机 1 100` and order threshold checks deliberately. A descending `LARGE` chain with `BREAK` after every `GOTO` maps cleanly to ranges, for example in the 老登偷窃 module: `LARGE N$偷窃随机 39` means 40-100, `LARGE ... 19` means 20-39 after the first branch is skipped, `LARGE ... 2` means 3-19, and the final unconditional branch means 1-2. Recompute the actual ranges from the ordered gates instead of assuming the written numbers are the percentages.
- `GetRandomText` is for file-backed random lines into documented `S`/`A` variables, per `438-取得随机字符串.md`. Prefer `L$` when the candidates are an in-script static list; prefer `GetRandomText` only when the candidates belong in a text file.
- In `QFunction-0.txt`, treat labels as engine callbacks: `@ButtonClickX` from `ADDBUTTON`, `@CustomButtonClick` from reserved UI buttons, `@MinMapCustomButtonClickX` from minimap buttons, `@StdModeFuncX` from item `AniCount`, `@ItemUpgrade` from gem upgrade, and `@AddBag` from items entering the bag. Do not rename or repurpose them without checking the official trigger chapter.
- The official `667-物品进入背包触发.md` warns not to write recycling logic directly inside `@AddBag`; dispatch to guarded helper scripts and keep pickup/link/update behavior narrow.
- Millisecond timers started by `SetOnTimerEx` fire `[@OnTimerExX]` in `MapQuest_def/QManage.txt`; ordinary `SetOnTimer` fires `[@OnTimerX]`. Audit both the start point and the QManage handler before changing timer IDs or intervals.
- For feature panels like `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt`, read UI flags and action labels as one map: `<$flag(n)>` renders current state, `check [n]` chooses the toggle branch, `SET [n]` writes the state, and `reset [start] count` can clear a contiguous flag range.
- For per-character paid helper toggles, prefer saved private variables such as `U10` when state must survive relog. Add the switch in the helper panel, guard enabling with `CHECKGOLD 数量`, reset any tick counters when toggling, and use `SENDMSG` for non-blocking status/failure notices when the feature should not interrupt play.
- If a shared millisecond timer such as `TimerEx7` already drives a workflow, do not change its interval just to add a slower periodic charge. Keep the existing `SETONTIMEREX` interval, add a small per-player counter, and run the paid action only every N ticks; pair the start point with a `#CALL` from `MapQuest_def/QManage.txt` to a focused helper label.
- In attack-trigger protection logic, first confirm the current target is a player with `CHECKCURRTARGETRACE = 0`, then read the target player's saved state with `C.` syntax such as `EQUAL <$C.STR(U10)> 1`. Do not replace a global switch with another global variable when the design is per-character.
- For parameterized labels such as `@召唤配置(骷髅,1)`, treat `<$SCRIPTPARAM*>` as label-local. The manual chapter `787-扩展NPC脚本点击触发带参数-NPC标签带参数.md` warns parameters can be cleared after jumps, so copy them to variables before any flow that may `GOTO` or trigger another label.
- For sensitive parameterized labels, add `CHECKSCRIPTPARAM` whitelist branches before charging, taking items, giving rewards, changing jobs, teleporting, mutating files, or changing saved variables. The local `样本Mir200` often omits this guard, so treat direct sample usage as an idiom, not the security baseline.
- For `GOTO @label(args|retvars)` callback-style helpers, pair the called label with `RETURN` and remember that `RETURN` ends the current script segment. Use this for same-file calculation/normalization helpers; do not assume undocumented direct `#CALL [file] @label(args)` parameter passing without manual or local sample proof.
- When parameters select a file path, category, item, pet, or class, immediately normalize them into `S$`/`N$` variables and validate the allowed values. Do not let raw `<$SCRIPTPARAM*>` become path authority or destructive-action authority.
- For mirror-map scripts like `样本Mir200/Envir/Market_def/比奇城/火龙将军-0.txt`, treat `AddMirrorMap`'s last argument as a variable name, not a value; pair it with explicit cleanup and stage flags before rebuilding instances.
- For dynamic NPC creation, keep the script file in `Market_def` and match the `CreateNPC` suffix rule to the map flag: `1` means one shared script name, `0` means map-suffixed script files.
- For party travel, use `GROUPMAPMOVE` when the whole group must move together; do not replace it with scattered teleport branches when map ownership or stage checks matter.
- For rebirth/class-reset flows like `样本Mir200/Envir/Market_def/云隐宗师.txt`, copy parameters to variables first, then verify hero state, bag space, level caps, and resource items before `CHANGEJOB`, `RENEWLEVEL`, `CLEARSKILL`, or storage deletion.
- Hero-side commands often need the `H.` prefix, such as `H.RENEWLEVEL`, `H.CLEARSKILL`, and `H.TAKEBAGITEM`; check the relevant manual chapter before assuming the player-side command applies to the hero.
- For batch reward loops like `样本Mir200/Envir/QuestDiary/系统功能/冶炼金矿.txt`, initialize loop counters before `While`, keep the guard branch separate from the reward branch, and write each reward counter explicitly.
- For persistent list editors like `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存仓.txt`, use `L$` for in-memory list work and text files for durable per-player storage; render text into `S$` separately from the stored list.
- For personal timers, pair `SetOnTimer n seconds` / `SetOffTimer n` in the feature script with `[@OnTimer<n>]` in `MapQuest_def/QManage.txt`. Do not change one side without checking the other.
- For `ITEMBOX` / `BOXITEM` flows, verify item ownership lifecycle: check the box item exists, bind it with `SetUpgradeItem`, mutate it, call `UpdateItem`, then `ReturnBoxItem`; every failure path that leaves an item in the box should return it.
- For script-generated equipment whose source must be visible client-side, bind the just-given item before mutation: `GIVE` -> `LINKGIVEITEM` -> `SetItemFrom -1 ...` -> `updateitem -1` -> `clearLinkItem`. The manual warns `LINKGIVEITEM` only binds the last successfully given item and must be paired with `clearLinkItem`; also verify the launcher/client hint files expose `[ItemFrom]` and the relevant `ItemFrom*` text labels.
- For two-slot transfer flows like `样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt`, audit both boxes as one transaction: verify compatible `<$BOXITEM[n].STDMODE>`, charge costs before random success, read old add-values/new-element values, clear the source, apply to the target, copy item states/custom text deliberately, `UpdateItem` both boxes, then `ReturnBoxItem` or `DelBoxItem` on every terminal path.
- Per `397-自定义OK框.md`, avoid reusing custom OK-box IDs between QFunction and NPC scripts in the same interaction surface. If a script serializes equipment, copy normal add-values, element values, source fields, and custom text as separate ranges, then update or clear the linked item explicitly.
- For `INPUTTEXT` / `INPUTNUM` controls, trace the input ID to `<$NPCINPUT(id)>` and any submit button that names that ID. The official input chapter still tells scripts to validate submitted data server-side, so do not trust only the client-side min/max or prompt text.
- For worn-item service costs like `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/探测.txt`, combine `CHECKITEMW` with position-specific mutation: check the equipped item, run the action, `ChangeItemDura <pos> - value`, `UpdateItem <pos>`, then remove with `TakePosW <pos>` only after a follow-up durability check confirms it is exhausted.
- `FindMonPoint` returns the nearest matching monster on the specified map. For locator panels, initialize every display variable to a known fallback such as `未知`, then overwrite only successful matches; for suffix variants, write explicit `#OR` checks or use documented count commands with suffix-ignore options only when that is intended.
- Treat admin/helper menus such as `样本Mir200/Envir/QuestDiary/系统功能/帮助菜单.txt` as mixed surfaces. Separate real player-facing entry points from `ISADMIN`-guarded GM probes, commented test calls, and temporary repair labels before promoting their patterns into production advice.
- For pet/slave storage like `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存储仆从.txt`, derive capacity from official skill state (`GetMagicInfo`) and current slave count before mutating state. Validate names with `CHECKSLAVENAME`, kill stored pets with `KillCallMob`, persist the `L$` list back to a saved variable or text file, and use `RECALLMOB` with an explicit owning skill type when restoring.
- Robot scheduled labels in `RobotManage.txt` should be treated as environment automation, not NPC dialog. Gate stage-dependent spawns with project state such as `G0`, check existing monster counts before `MonGenEx`, clean maps or lists deliberately (`CLEARMAPMON`, `CLEARNAMELIST`), and end each scheduled branch with `BREAK` after the intended action.
- For monster strengthening tasks, inspect `Monster` DB schema before updating values. In `GEEM2.db`, useful fields include `Lvl`, `HP`, `AC`, `MAC`, `DC`, `DCMAX`, `MC`, `SC`, `SPEED`, `WALK_SPD`, and `ATTACK_SPD`.
- `QMission-0.txt` task pages should prefer direct labels over dispatcher labels. For progress pages such as `[@世界当前进度]`, repeat `#IF EQUAL G0 n` / `#SAY ...` / `#ACT BREAK` in the same label and keep fixed detail pages reachable by `<文本/@标签>` links.
- When the late-game world splits across multiple maps, treat `G0=9/10/11/12` as a staged sequence instead of a single "all open" bucket; in this project that sequence is 雷炎 -> 雪域 -> 火龙 -> 狐月.
- The manual's "hero commands usually add `H.`" is a weak heuristic, not proof. `H.RECALLMOB` worked on the live server, but `H.CHECKSKILL`, `H.CHECKSLAVECOUNT`, `<$H.SlaveCount>`, `H.KILLCALLMOB`, and `H.CLEARSLAVE` do not exist. Verify every hero-side command against the manual or a live test before using it; when a command has no manual page and no project precedent, assume it is absent until a real test proves otherwise.
- `[@HeroMagSelfFuncX]` is documented in `832-英雄魔法触发功能.md` but did NOT fire for the hero summon skill on the live server. Treat hero magic self-triggers as version-dependent; use `[@HeroLearnMagic]` with `<$H.LearnMagicID>` as the dependable learn-time hook when a skill must set state.
- There is no engine command to read the hero pet count or delete an already-summoned hero pet. Represent pet occupancy with dedicated personal flags `[n]` as slots, reset them on login and on `@OnHeroSlaveDie`, and bias cleanup toward clearing more state (under-summon is acceptable, overflow is not). Overflow can only be cleaned by the hero dying, map change, or GM kill.
- `P0`/`P` variables do NOT persist across `[@OnTimerX]` callbacks; use personal flags `[n]` (which do persist) for any cross-callback counter or occupancy state. Reset them explicitly on login because they survive relog.
- Flat `#IF/#ACT` blocks are sequential, not else-if. A high-level subject matches every `#IF CheckHerolevel > N` branch at once. For "derive one value from one input" logic, use arithmetic (`MOV`/`DEC`/`DIV`/`INC`) with `SMALL`/`LARGE` clamps instead of a flat branch chain, or use `#ELSEACT BREAK` for truly exclusive branches.
- `DIV`/`MUL`/`MOV`/`INC`/`DEC` do not accept string variables: write `DIV N$X 5` (bare variable or literal), never `DIV N$X <$STR(N$X)> 5`. `SMALL`/`LARGE`/`EQUAL` take `变量 数值` with the variable first. `DIV` is integer division.
- For a pet whose level derives from its owner's level, compute it with `MOV N$级 <$H.LEVEL>` then `DEC`/`DIV`/`INC`, and clamp with `SMALL N$级 1` / `LARGE N$级 7`. See `references/hero-autocall-slave.md` for the full hero auto-summon pattern.

## Efficient Editing Guidance

- Prefer reusable repo tools for GBK-safe Mir200 edits when they exist, especially for batch replacements, `MapInfo` parsing, stage checks, monster DB inspection, Boss classification, and encoding checks.
- If tools do not exist yet and the task repeats, propose or create small `tools/` scripts instead of expanding one-off PowerShell blocks.
- Use ordinary patch editing for UTF-8 Markdown, JSON, and small ASCII-safe config changes.
- For generated Mir200 script blocks, verify command counts, label uniqueness, `#CALL` targets, and remaining bypass paths with targeted static searches.
- When touching `QMission-0.txt`, statically search new display labels for `GOTO @...`; avoid it inside task-page display flow unless an existing working example in that same file proves the engine context supports it.

## Training Workflow

Use this loop when the user asks the skill to learn, train, self-upgrade, or extract reusable experience from `样本Mir200` or a real Mir200 project:

1. Run `update` to rebuild indexes, thinking, and the training course.
2. Inspect `references/mir200-training.md`.
3. Pick one lesson at a time, starting from entry/dispatch and ending at combined systems.
4. Inspect the listed sample files and write down: entry, guards, actions, state writeback, failure path.
5. Compare command syntax with the Markdown manual before turning observations into advice.
6. For real projects, also inspect `AGENTS.md` and relevant `docs/*.md`; extract repo-specific rules as project facts and only promote durable cross-project lessons into this skill.
7. When continuing open-ended sample training, score candidates by command diversity, trigger coverage, state writes, and manual cross-check value; avoid repeatedly studying near-duplicate shop/storage scripts.
8. Update the generated summary by running `update`; make manual SKILL.md changes only for durable workflow rules.

Do not treat runtime logs or binary/server files as training material. Prefer `Envir/Market_def`, `QuestDiary`, `MapQuest_def`, `Robot_def`, `MapInfo`, `MapEvent`, `MerChant`, `Npcs`, and `MonGen` files.

## Commands

Run from any directory under the knowledge root, or pass `--root`.

```powershell
python <skill-dir>\scripts\lf_kb.py update
python <skill-dir>\scripts\lf_kb.py validate
python <skill-dir>\scripts\lf_kb.py learn-script "样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt"
python <skill-dir>\scripts\lf_kb.py search "CHECKITEM GIVE 装备回收" --source all --limit 8
python <skill-dir>\scripts\lf_kb.py search "MAPMOVE" --source sample --limit 5
python <skill-dir>\scripts\lf_kb.py search "0 308 264 0102" --source mapinfo --limit 5
python <skill-dir>\scripts\lf_kb.py inspect "knowledge_base/chapters/661-丢弃背包物品前触发.md"
python <skill-dir>\scripts\lf_kb.py inspect "样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/mir200-thinking.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/mir200-training.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/script-deep-dives.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/script-parameters.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/envir-config-rules.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/envir-config-deep-dives.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/sample2-feature-buffs.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/mir200-256-colors.md"
```

## Search Guidance

Use both Chinese feature names and script command keywords:

- NPC/dialog: `[@main]`, `#IF`, `#ACT`, `#SAY`, `GOTO`, `BREAK`
- Items and rewards: `CHECKITEM`, `GIVE`, `TAKE`, `GAMEGOLD`, `CHECKBAGSIZE`
- Maps and NPCs: `MapInfo`, `MerChant`, `Npcs`, `MAPMOVE`, `MonGen`
- Timers and automation: `Robot_def`, `AutoRunRobot`, `RobotManage`
- Script loop diagnosis: `[脚本死循环]`, `ScriptGotoCountLimit`, `LimitScriptGotoCount`, `#CALL`, `GOTO`, `BREAK`, `RETURN`, `SetOnTimer`, `SetOffTimer`, `QManage`, `OnTimer`
- Hero lifecycle triggers: `HeroTakeOnEx`, `HeroTakeOffEx`, `HeroLogin`, `HeroDie`, `HeroStruckDamage`, `HeroAttackDamage`, `H.CHECKUSEITEM`, `H.GetItemFieldValue`, `LockUpdateAbil`, `UpdateAbil`
- Hero pets/summon: `RECALLMOB`, `H.RECALLMOB`, `CHECKSLAVECOUNT`, `H.CHECKSKILL`, `@HeroLearnMagic`, `<$H.LearnMagicID>`, `@OnHeroSlaveDie`, `@HeroSlaveAttack`, `@HeroSlaveMagicAttack`, `<$H.CurSlaveName>`, `<$H.DIESLAVENAME>`, `@HeroMagSelfFuncX`, `CheckHerolevel`, `<$H.LEVEL>`, `KillCallMob`
- UI/dialog extensions: `OPENMERCHANTBIGDLG`, `ITEMBOX`, `Text`, `Img`
- State/effect commands: `ChangeState`, `石化`, `冰冻`, `蛛网`, `红毒`, `绿毒`, `定身`, `瘫痪`, `禁锢`, `吸血`, `吸蓝`, `禁止使用技能`, `[@Struck]`, `[@StruckDamage]`, `M.ChangeState`, `H.ChangeState`, `FS.ChangeState`, `BB.ChangeState`
- Colors and rarity palettes: `颜色值列表`, `256色值`, `SCOLOR`, `/SCOLOR`, `{文字|250}`, `{文字内容|文字颜色0-255}`, `SetCustomItemTextColor`, `SetCustomItemAbil`, `TzItemDescList`, `ItemDescList`, `BossNameColor`, `TZNoActiveItemColor`, `223,249`, `218`, `116`, `249`, `250`, `251`, `253`, `254`
- Sample2 feature systems: `流派`, `觉醒之印`, `神剑BUFF`, `SetArrBuff`, `CloseArrBuff`, `BUFF检测`, `元素读取`, `五维读取`, `攻魔道读取`, `HPMP读取`, `防御读取`, `攻速读取`, `施法速度`, `吸血读取`, `技能威力读取`, `技能等级读取`, `BB读取`, `咒蛊术`, `体态压迫`, `撕裂`, `失心锁`, `苗疆蛊毒`, `苹果`, `满江红`, `幸运药水`, `远古契约`, `先祖契约`, `毒龙之殇`, `浴血狂攻`

When a query returns too many hits, search the manual with exact command names and search samples with the feature name or folder name.

## Maintenance

Self-upgrade means refreshing derived indexes from the current manual and sample scripts:

```powershell
python <skill-dir>\scripts\lf_kb.py update
python <skill-dir>\scripts\lf_kb.py validate
```

If the CHM is reconverted, run the project conversion scripts first, then run this skill's `update`.

After updating, use the regenerated `references/mir200-thinking.md` as the local thinking summary. It should be updated from real scripts, not from memory.

Use `references/mir200-training.md` as the course map for continued improvement. Each lesson names signals, sample files, and reading focus so a future agent can keep practicing without needing the original conversion context.

## Response Rules

- Cite the local Markdown chapter or sample file used.
- Distinguish official manual behavior from inference based on sample scripts.
- Mention when no matching manual entry exists and the answer is sample-derived.
- When the answer relies on repeated script patterns, explain the pattern in plain Mir200 terms, not only the command list.
- Do not invent command syntax. Search for it. When a feature looks like a list/array problem, first check whether `L$` already exists before falling back to file-backed text lists.
- Do not edit binary/runtime files such as `.exe`, `.db`, `.dat`, `.lic`.
