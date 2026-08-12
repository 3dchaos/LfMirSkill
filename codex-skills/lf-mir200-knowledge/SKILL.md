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
2. Search the manual for command syntax and official behavior.
3. Search `样本Mir200` for working examples.
4. Read `references/mir200-training.md` when learning or improving the skill from examples.
5. Read `references/mir200-thinking.md` for the current local script-thinking summary.
6. Inspect the most relevant files before making claims or edits.
7. For code/script edits, preserve original encoding and style, and modify only the requested files.
8. Validate statically after edits with `validate` and targeted searches.

## Durable Mir200 Rules

- Read Mir200 project text as ANSI by default. If the result is garbled, retry UTF-8. Preserve the original encoding when writing files back.
- `[@OnKillMob]` requires the target map to include `ONKILLMON` in `MapInfo.txt`.
- `[@KillMon]` does not require `ONKILLMON`; do not confuse it with `[@OnKillMob]`.
- Boss or first-kill logic must match the full monster name from `MonGen.txt`. Do not silently ignore numeric, bracketed, or other suffixes.
- When the same monster name appears on multiple maps, also check the current map and the relevant stage/state variable before changing global progress.
- In `MapInfo.txt`, lines like `0 308,264 -> 0102 3,7` are map links: stepping on source map `0` at X308 Y264 sends the player to target map `0102` at X3 Y7. Coordinates may be written as `X,Y` or `X Y`; parse both.
- Map links are directional. Do not assume a return path exists unless a separate reverse link is present, often on a neighboring coordinate.
- For staged map-opening designs, block every entry path, not only NPC teleport menus: `MapInfo` links, `MAPMOVE`/`MAP`/`MAPS`/`GROUPMAPMOVE`, recall and exchange-map commands, dynamic maps, activities, item teleports, random movement, reconnect/death/respawn paths, robot scripts, and GM/admin bypasses.

## Training Workflow

Use this loop when the user asks the skill to learn, train, self-upgrade, or extract reusable experience from `样本Mir200`:

1. Run `update` to rebuild indexes, thinking, and the training course.
2. Inspect `references/mir200-training.md`.
3. Pick one lesson at a time, starting from entry/dispatch and ending at combined systems.
4. Inspect the listed sample files and write down: entry, guards, actions, state writeback, failure path.
5. Compare command syntax with the Markdown manual before turning observations into advice.
6. Update the generated summary by running `update`; make manual SKILL.md changes only for durable workflow rules.

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
