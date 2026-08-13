---
name: lf-mir200-knowledge
description: Use when answering or modifying LF/LFM2/翎风引擎 Mir200 server scripts, NPC scripts, MapInfo, MonGen, MerChant, QuestDiary, Market_def, Robot_def, item rules, command syntax, or engine help-document questions using the local Markdown manual, sample Mir200 directory, and learned script patterns.
---

# LF Mir200 Knowledge

## Overview

Use the local LF engine manual and sample `Mir200` server as the source of truth. Search before answering, cite local file paths, and prefer examples from the sample scripts when the user asks how to write or change scripts.

This skill also learns a local script-thinking model from real sample files. The model is regenerated from the sample scripts and should be treated as a living summary of how Mir200 scripts are structured in practice.

The skill includes a generated training course. Use it to practice on real sample scripts in a progressive order before making broad claims or designing complex script changes.

Do not compile, launch, or run the Mir200 server. Perform static analysis only unless the user explicitly changes that constraint.

## Locate The Knowledge Root

The root is the directory containing both:

- `knowledge_base/index.md`
- `样本Mir200/`

When paths are not obvious, run:

```powershell
python <skill-dir>\scripts\lf_kb.py --root <root> validate
```

If the root moves, either pass `--root` or set `LF_MIR200_KB_ROOT`.

## Standard Workflow

1. Run `update` when the manual, sample scripts, or indexes may be stale.
2. In a real project repo, read the nearest `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` first, then relevant project docs such as `docs/*.md` named by the user or matching the feature.
3. Search the manual for command syntax and official behavior.
4. Search `样本Mir200` for working examples.
5. Read `references/mir200-training.md` when learning or improving the skill from examples.
6. Read `references/mir200-thinking.md` for the current local script-thinking summary.
7. Inspect the most relevant project files before making claims or edits.
8. For code/script edits, preserve original encoding and style, and modify only the requested files.
9. Validate statically after edits with `validate` and targeted searches.

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

## Project Knowledge Workflow

When working inside a Mir200 repo, build a small project model before editing:

1. Read the repo instruction file, usually `AGENTS.md`, for encoding, compile/run limits, ownership boundaries, and static checks.
2. Read user-mentioned design docs, then search `docs/` for nearby specs if the request references a feature name.
3. Extract durable facts into the working notes: stage variables, map groups, key entry scripts, trigger labels, manual chapters, and validation commands.
4. If those facts are reusable beyond one task, update this skill or a reference file with the rule, not the session narrative.

For this repository pattern, remember these reusable lessons:

- `Mir200/Envir/**/*.txt` is commonly GBK/ANSI and must be edited with encoding-preserving tools.
- `AGENTS.md`, `docs/`, and knowledge Markdown are maintained as UTF-8.
- For staged map opening with `G0`, natural `MapInfo.txt` links from lower-stage maps to higher-stage maps are potential bypasses; parse them directionally.
- Dynamic replacement links should be cleaned before regeneration (`DELMAPGATE`), then rebuilt only for stages allowed by the current `G0` (`ADDMAPGATE`).
- Startup or environment initialization may affect global variables, so dynamic stage-dependent links should be refreshed after initialization and after successful stage progression.
- `Robot.txt` only binds a robot name to `Envir\Robot_def\AutoRunRobot.txt`; `AutoRunRobot.txt` entries are resolved through `Envir\Robot_def\RobotManage.txt`, so a new scheduled tag needs a matching `[@tag]` in `RobotManage.txt` that then `#CALL`s the real script.
- For dynamic NPCs created by `CreateNPC`, keep the script in `Market_def`. If the last argument is `1`, the script file name omits the map suffix (`英雄引路人.txt`); if it is `0`, the script file name keeps the suffix (`英雄引路人-3.txt`).
- For monster strengthening tasks, inspect `Monster` DB schema before updating values. In `GEEM2.db`, useful fields include `Lvl`, `HP`, `AC`, `MAC`, `DC`, `DCMAX`, `MC`, `SC`, `SPEED`, `WALK_SPD`, and `ATTACK_SPD`.
- `QMission-0.txt` task pages should prefer direct labels over dispatcher labels. For progress pages such as `[@世界当前进度]`, repeat `#IF EQUAL G0 n` / `#SAY ...` / `#ACT BREAK` in the same label and keep fixed detail pages reachable by `<文本/@标签>` links.

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
7. Update the generated summary by running `update`; make manual SKILL.md changes only for durable workflow rules.

Do not treat runtime logs or binary/server files as training material. Prefer `Envir/Market_def`, `QuestDiary`, `MapQuest_def`, `Robot_def`, `MapInfo`, `MapEvent`, `MerChant`, `Npcs`, and `MonGen` files.

## Commands

Run from any directory under the knowledge root, or pass `--root`.

```powershell
python <skill-dir>\scripts\lf_kb.py update
python <skill-dir>\scripts\lf_kb.py validate
python <skill-dir>\scripts\lf_kb.py search "CHECKITEM GIVE 装备回收" --source all --limit 8
python <skill-dir>\scripts\lf_kb.py search "MAPMOVE" --source sample --limit 5
python <skill-dir>\scripts\lf_kb.py search "0 308 264 0102" --source mapinfo --limit 5
python <skill-dir>\scripts\lf_kb.py inspect "knowledge_base/chapters/661-丢弃背包物品前触发.md"
python <skill-dir>\scripts\lf_kb.py inspect "样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/mir200-thinking.md"
python <skill-dir>\scripts\lf_kb.py inspect "codex-skills/lf-mir200-knowledge/references/mir200-training.md"
```

## Search Guidance

Use both Chinese feature names and script command keywords:

- NPC/dialog: `[@main]`, `#IF`, `#ACT`, `#SAY`, `GOTO`, `BREAK`
- Items and rewards: `CHECKITEM`, `GIVE`, `TAKE`, `GAMEGOLD`, `CHECKBAGSIZE`
- Maps and NPCs: `MapInfo`, `MerChant`, `Npcs`, `MAPMOVE`, `MonGen`
- Timers and automation: `Robot_def`, `AutoRunRobot`, `RobotManage`
- UI/dialog extensions: `OPENMERCHANTBIGDLG`, `ITEMBOX`, `Text`, `Img`

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
- Do not invent command syntax. Search for it.
- Do not edit binary/runtime files such as `.exe`, `.db`, `.dat`, `.lic`.
