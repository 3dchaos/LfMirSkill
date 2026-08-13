# Mir200 Envir Config Rules

Use this reference when reading `样本Mir200/Envir/**/*.txt` and `*.ini` as configuration rather than NPC dialog scripts. Prefer official chapters for command semantics, and use sample files for real-world spacing, comments, optional fields, and path conventions.

## General Reading Rules

- Treat `Envir` text as ANSI/GBK unless proven otherwise. Preserve encoding and line endings when editing real server files.
- Skip blank lines and lines starting with `;` for active data, but read comments as field hints. Many sample files document their own column order in comments above the data.
- Do not parse every text file as CSV. The sample uses several formats: whitespace columns, bracketed sections, `key=value` INI sections, `:` subfields, `|` lists, slash-delimited rates, and script-like labels.
- File name and folder path often carry meaning. Examples: `MonItems/白野猪.txt` is the drop list for `白野猪`; `SmartMonster/雪域领主[狂化].ini` configures that custom monster; `UserData/CustomSkill/201.ini` configures custom skill ID `201`.
- Empty files and empty directories can still be intentional feature switches or placeholders, such as deny/allow lists and `Market_Prices`/`Market_Upg` folders. Do not delete or ignore them as accidental without project evidence.
- When linking config to scripts, follow the registration chain instead of guessing paths: `MerChant.txt` / `Npcs.txt` place NPCs, `Robot.txt` points to `Robot_def/AutoRunRobot.txt`, schedules in `AutoRunRobot.txt` jump to labels in `Robot_def/RobotManage.txt`, and `MapEvent.txt` calls labels in `Market_def/QFunction-0.txt`.

## Core World Tables

### `MapInfo.txt`

- Map definitions look like `[mapId[|alias] title [parent?]] PARAM PARAM(ARG) ...`. The map ID can contain letters and digits; aliases are separated by `|`, for example `[hlmg|hl001 火龙迷宫]`.
- Map parameters are case-insensitive in samples, but keep existing casing when editing. Cross-check parameter meaning with `knowledge_base/chapters/747-地图参数详解.md`.
- `ONKILLMON` gates `[@OnKillMob]`; `KILLMON` is a map parameter mentioned by the manual but do not substitute it for `ONKILLMON` when auditing kill callbacks.
- Link lines are directional: `sourceMap sourceX,sourceY -> targetMap targetX,targetY`. Coordinates may be comma-separated or space-separated. Never infer a reverse link without a separate reverse line.
- `NORECONNECT(target)` and entry-control flags can create hidden movement paths. For stage gating, audit map links, scripted teleport commands, reconnect targets, item restrictions, and dynamic gates together.
- `FB(...)` creates ectype/fuben map families. Official chapter `052-副本地图相关参数.md` shows that related NPC scripts may omit `$` in file names even when the runtime map name contains `$`.

### `MonGen.txt`

- Official format from `256-脚本刷怪.md`: `地图 X Y 怪物名 范围 数量 间隔 集中刷新坐标机率 名字颜色 内功怪物 国家ID 是否可攻击同国家玩家 不同国家怪物是否PK 能否被同国家人物攻击`.
- The sample commonly uses only the first 7 fields, and appends optional fields only when needed. Do not require all later fields to exist.
- Monster names can include suffix digits, brackets, and spaces around columns. Match exact monster names when linking to `MonItems` or DB rows; do not collapse `牛魔王`, `牛魔王8`, and `牛魔王[BOSS]`.
- Tail fields may include name color and trigger labels per `761-怪物名称颜色自定义功能.md`. Preserve empty middle fields when adding later optional values; the manual warns not to cross-skip optional parameters.

### `MerChant.txt` And `Npcs.txt`

- `MerChant.txt` rows register merchant/NPC scripts: script path, map, X, Y, display name, range, appearance, and trailing flags. The first column maps to `Market_def/<script-path>-<map>.txt` unless dynamic or shared-script rules override it.
- `Npcs.txt` is a similar NPC-definition table for `Npc_def`, with an NPC attribute/type column near the front. Do not merge it with `MerChant.txt` when resolving script files.
- Resolve scripts from the registration table before searching by display name. Display names can differ from script names.

### `MapEvent.txt`

- Official format from `674-地图事件触发.md`: `地图 X Y 范围 标识:值 条件代码:物品:组队 机率 事件类型代码:@QFunctionLabel`.
- `-1 -1` coordinates mean no coordinate check in the sample. Range `0` means exact coordinate when coordinates are used.
- Trigger condition codes include drop, pickup, mine, walk, run, horse walk/run, and death-drop events. The event label is a `QFunction-0.txt` callback, not a local label in `MapEvent.txt`.
- Duplicate map/coordinate/flag/condition combinations are not all active; the official chapter says only the last same setting takes effect. Preserve ordering when editing.

## Automation Tables

### Robot Files

- `Robot.txt` maps robot name to script name, for example `系统控制 AutoRunRobot`.
- `Robot_def/AutoRunRobot.txt` contains schedule rows like `#AutoRun NPC MIN 8 @虎卫检测` or `#AutoRun NPC RUNONDAY 23:59 @清理每日`.
- Scheduled labels are implemented in `Robot_def/RobotManage.txt`. Audit all three files before adding or renaming a scheduled job.

## Item And Monster Lists

### `MonItems/*.txt`

- Traditional drop lines are `rate itemName [amount]`, for example `1/1 金币 5000`. Amount is commonly used for gold.
- New drop format from `821-新爆率格式-.html.md` supports `#CHILD rate [BURSTRATE] [RANDOM] [conditions]` followed by parenthesized child lines.
- Drop files may `#CALL` shared drop modules under `QuestDiary`. Resolve those calls before deciding a monster has no drops.
- File names are monster names. Keep suffix variants as separate files when the sample has them, such as `白野猪.txt`, `白野猪0.txt`, `白野猪8.txt`.

### List Files

- Many root files are one-item-per-line allow/deny/filter lists (`Disable*.txt`, `Deny*.txt`, `*ItemList.txt`). Empty file means no entries, not necessarily unused feature.
- Some list files use columns or embedded separators: `UserCmd.txt` / `UserCmds.txt` map command text to IDs; `MiniMap.txt` maps map ID to minimap number; `StartPoint.txt` has eight safety-zone columns.
- For `StartPoint.txt`, official fields are map, X, Y, forbid-say, range, halo type, PKZONE, and PKFIRE. Negative range values can represent custom-shaped safe zones per `839-自定义安全区形状.md`.

### Item Rule And Set Tables

- `ItemRuleList.txt` is a wide item-name row followed by many positional flags and a `|` separator for another value group. Treat item names as the first token up to the first run of numeric columns; names may contain Chinese punctuation.
- Parse `ItemRuleList.txt` by structure, not by guessed flag names. In the sample, each active row is `itemName 40 numeric flags | 10 numeric extension flags`. If item names might contain spaces, split at `|`, parse the final 40 numeric tokens before `|`, and treat the preceding text as the exact item name.
- `ItemRuleList.txt` is saved from M2 `查看 -> 列表信息2 -> 物品规则`. Official chapters tie that UI to pickup/drop QF triggers, monster drop triggers, body-drop triggers, repair restrictions, gemstone-upgrade blocking, chest prompts, auction allow rules, and see-through drop filtering. A full column schema is not documented in the current manual, so do not rename individual columns from sample position alone.
- For item-rule-triggered scripts, cross-check `knowledge_base/chapters/705-物品捡取和丢弃触发.md`, `706-物品捡取和丢弃触发.md`, `704-物品掉落触发.md`, and `664-人物身上物品掉落触发.md`. `@PickUpItemEX` is explicitly global and does not require item rules; the older item-specific pickup/drop triggers do.
- For operational restrictions controlled by item rules, cross-check the relevant feature chapter before advising: `317`/`454` for repair blocking, `513` for gemstone-upgrade blocking, `735` for chest acquisition prompts, `737` for drop see-through blocking, and `793` for auction allow rules.
- `ItemDescList.txt` is item remark display metadata. Rows are `itemName=color/text\color/text...`; `\` creates additional display lines, and each line can carry its own color prefix. Parse at the first `=` only; item names and text may contain Chinese punctuation, and malformed-looking doubled `==` can appear in real data.
- `ItemDescList.txt` supports the same rich hover syntax documented for item remarks: inline `{text|color}`, `<looks:...>`, `<NewopUI:...>`, `<Img:...>`, `<PlayImg:...>`, and `<ImgNum:...>`. Cross-check `knowledge_base/chapters/099-悬浮式装备信息窗口支持图片显示.md` and `819-镶嵌宝石设置说明.md` before generating visual remark markup.
- Do not treat `ItemDescList.txt` warning text such as `无法交易`, `禁止丢弃`, or `丢弃消失` as enforcement. It is display text. Verify actual behavior in `ItemRuleList.txt`, item state commands such as `GIVESTATEITEM` / `SetItemState`, QFunction triggers, and nearby deny lists like project-specific mail/storage lists.
- `MakeItem.txt` uses `[target item]` sections followed by required material rows.
- `GroupItemList.txt` is tabular but embeds `|`-separated item sets and value arrays inside fields. Do not split only on `|`; first split the outer row columns.
- `GroupItemList.txt` is the authoritative set-effect table. In the sample each active row has 9 outer fields: set ID, required count, set name, `|`-separated item list, three 40-value arrays, one 27-value array, and a remark. Preserve outer tab/spacing and every `|` placeholder.
- `GroupItemSkillPowerList.txt` is an INI-style extension keyed by `GroupItemList.txt` set ID. Sections like `[20]` contain `Attack<skillId>=value` and `Defense<skillId>=value`; only IDs with a matching active set row are meaningful.
- For set skill power, cross-check `knowledge_base/chapters/304-设置技能伤害防御.md`: Attack/Defense entries are skill-ID keyed damage/defense adjustments, not equipment attribute arrays. `SkillPowerItemList.txt` is the adjacent single-item version; `GroupItemSkillPowerList.txt` is the set-ID version.
- `TzItemDescList.txt` / equipment set descriptions use custom delimiters described in `838-装备套装备注.md`: `/`, `|`, `:`, `\`, and inline `{text|color}` all have display meaning.
- `TzItemDescList.txt` is display metadata for set remarks, while `GroupItemList.txt` is the actual set-effect configuration. Cross-check both before claiming a set's real effect.
- In `TzItemDescList.txt`, a row is shaped like `activeColor[,inactiveColor]/setName|requiredCount|itemColor/itemOrGroup|...:descColor/text\descColor/text`. Parenthesized comma groups are alternatives for one visible set slot, not extra required slots.
- Do not parse `TzItemDescList.txt` with a flat split on `/` or `|`. First isolate the leading color segment, then the item/description boundary at `:`, then parse outer item slots while preserving parenthesized alternatives such as `(衣服(男),衣服(女))`.
- Multiple true thresholds can be summarized in one `TzItemDescList.txt` display row, for example separate 5-piece and 8-piece `GroupItemList.txt` effects shown as two `\`-separated remark lines. Treat tooltip text as player-facing explanation, not proof that an effect row exists.
- For `GroupItemList.txt` percentage arrays, cross-check `knowledge_base/chapters/847-调整人物套装属性百分比.md`; for the 27-value new-attribute array, cross-check `knowledge_base/chapters/345-调整物品新增属性.md` and `541-检测人物新增属性.md`. Some sample rows also use a separate 40-value special flag array, so do not collapse all arrays into one attribute family.
- `GroupItemList.txt` item counts and tooltip slot counts may differ. The item list is all acceptable matching item names; `required count` is the trigger threshold. `TzItemDescList.txt` may group same-slot alternatives with parentheses for display, while `GroupItemList.txt` stores the flattened candidate names.

### Effect Tables

- `EffectList.txt` stores custom effect definitions from M2 `查看 -> 列表信息2 -> 特效列表`. Official command chapter `310-设置装备发光特效.md` says `SETITEMEFFECT` uses effect numbers already configured in that list, and `0` clears the effect.
- Treat the first numeric column in `EffectList.txt` as the effect ID used by scripts and item mappings. The sample row `6 ... 锁定特效` is called by `SETITEMEFFECT boxitem0 6` in `QuestDiary/系统功能/老登辅助/辅助.txt`.
- Do not invent a full positional schema for `EffectList.txt` from one sample row. The table is M2-generated, version-sensitive, and has grown options such as three effect positions, ground-item effects, centered drawing, gender independence, normal drawing, and remarks. If field-level edits are required, cross-check a UI export, comments, or a known working row first.
- `EffectImageList.txt` is a one-resource-per-line WIL/PAK resource list. Official UI and effect chapters consistently call this the M2 `列表信息2 -> WIL资源` file-number source. Keep row order stable because numeric resource references depend on this list.
- `EffectItemList.txt` maps item names to effect IDs, in the sample as `itemName effectId`. Parse from the right: the final token is numeric, and everything before it is the exact item name. Cross-check that the referenced effect ID exists in active `EffectList.txt`; historical rows may live only in `EffectList_bak.txt`.
- Nearby files are separate effect families: `PillarOfLightEffect*.txt` is ground light-pillar effect config, while `EffectHintBG*.txt` is item-hover-window background effect config. Do not merge their IDs with `EffectList.txt` without feature-specific evidence.

## INI Files

- `SmartMonster/*.ini`, `UserData/CustomSkill/*.ini`, `Nations/Nations.ini`, and `ItemDropLimit/DropLimitConfig.ini` use INI section/key syntax. Prefer a parser that preserves comments/order if editing is required.
- Custom monster and skill INI files are large and sectioned by behavior surface (`Client`, action frames, attack sections, effects, server rules). Do not infer one section's repeated numeric suffixes apply globally without checking neighboring sections.
- `-1` commonly means disabled image/effect file in visual sections, but confirm by section context before treating it as a universal sentinel.

## Cross-Checks Before Advice Or Edits

1. Identify the file family by path and extension.
2. Read comments at the top of the target file.
3. Search the manual for the exact file name or command/feature name.
4. Read at least one nearby sample row with optional fields populated.
5. Follow registration chains to scripts or data files.
6. Preserve exact names, suffixes, aliases, separators, and optional-field positions.
7. Validate with `lf_kb.py update`, targeted search/inspect, and `lf_kb.py validate`.
