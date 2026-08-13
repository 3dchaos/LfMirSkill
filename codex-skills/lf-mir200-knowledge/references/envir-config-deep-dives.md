# Mir200 Envir Config Deep Dives

Use this file for compact lessons learned from named `Envir` configuration files. Keep each entry focused on format, official cross-checks, sample-specific observations, and reusable reading rules. Do not paste whole configuration files here.

## Method

1. Inspect the target config file with encoding-safe tooling.
2. Classify the file family: table, list, sectioned text, INI, schedule, drop list, or mixed format.
3. Read comments in the target file and at least one official chapter for the same feature.
4. Compare the config to adjacent runtime files when the target is display-only or registration-only.
5. Record separators, optional fields, path/name semantics, active vs commented rows, and cross-file dependencies.
6. Promote only durable cross-project rules into `SKILL.md` or `envir-config-rules.md`.

## TzItemDescList.txt

- Source: `样本Mir200/Envir/TzItemDescList.txt`
- Shape: equipment set tooltip/remark display table with one active line per visible remark group. It is display metadata, not the authoritative set-effect table.
- Static report: 13 active lines. Sample groups include `星王降临`, `王者殿堂`, `唯一主宰`, `传奇龙魂`, `初识仙境`, `踏入仙境`, `仙境之力`, `登顶仙境`, and `梦龙`.
- Official chapter to cross-check: `knowledge_base/chapters/838-装备套装备注.md`.
- Nearby config to compare: `样本Mir200/Envir/GroupItemList.txt`, which contains the actual set-effect rows and trigger IDs.
- Format lesson: each active row follows `activeColor[,inactiveColor]/setName|requiredCount|itemColor/itemOrGroup|...:descColor/text\descColor/text`. `/`, `|`, `:`, `\`, commas, and parentheses all carry meaning.
- Color lesson: the first segment before `/` can contain one color or `active,inactive`; sample lines use `223,249`, matching the official active/inactive color form.
- Item-list lesson: after `setName|requiredCount`, each `color/item` segment represents one visible set slot. Parenthesized comma groups such as `(星王战甲(男),星王战甲(女))` are alternatives for that slot, not multiple required slots.
- Slot-count lesson: `requiredCount` is not always equal to every real item name listed when alternatives are expanded. Count outer `|` slot segments, not comma-separated names inside parentheses.
- Description lesson: text after `:` is display-only, with `\` creating additional remark lines. Each remark line can start with its own color prefix, such as `253/...` and `56/...`.
- Cross-file lesson: `TzItemDescList.txt` can combine several `GroupItemList.txt` thresholds into one tooltip. For example, one remark line can describe 5-piece effects and another can describe 8-piece or 9-piece effects. Do not assume a one-to-one mapping between remark rows and `GroupItemList.txt` rows.
- Accuracy lesson: before editing or generating a set remark, verify the displayed item alternatives against `GroupItemList.txt` and verify the actual effect numbers against the true set-effect rows. `TzItemDescList.txt` controls what the player sees; `GroupItemList.txt` controls what actually applies.
- Parsing caution: do not naively split the whole row by `/` or `|` first. Split the row into color/header and description around the first `/` and the first `:` at the item/description boundary, then parse item slots carefully so parenthesized alternatives remain intact.

## EffectImageList.txt / EffectItemList.txt / EffectList.txt

- Sources: `样本Mir200/Envir/EffectImageList.txt`, `样本Mir200/Envir/EffectItemList.txt`, and `样本Mir200/Envir/EffectList.txt`.
- Shape: three related M2 visual-effect tables. `EffectImageList.txt` lists WIL/PAK resources; `EffectList.txt` defines numbered custom effects; `EffectItemList.txt` attaches item names to effect IDs.
- Official chapter to cross-check: `knowledge_base/chapters/310-设置装备发光特效.md`. It documents `SETITEMEFFECT position effectId [effectSlot]`, says `effectId` must already exist in `列表信息2-特效列表`, and says `0` clears the effect. It also documents `H.SETITEMEFFECT` for hero equipment.
- Official history cross-checks: `knowledge_base/chapters/001-翎风引擎历史更新记录.md` records that equipment glow effects can read arbitrary WIL resources and show outer-view, inner-view, and bag effects through `查看-列表信息(二)-物品特效`; later updates extend `SETITEMEFFECT` to three effect IDs, ground-item effects, centered/normal drawing options, no-gender distinction, and remark display.
- WIL-resource cross-check: chapters such as `099-悬浮式装备信息窗口支持图片显示.md`, `179-播放人物效果.md`, `373-在地图上播放魔法效果.md`, and `782-脚本中使用图标功能.md` repeatedly define `F` as the WIL file number edited in M2 `列表信息2-WIL资源`. This supports reading `EffectImageList.txt` as the saved resource list behind those numeric file references.
- `EffectImageList.txt` sample facts: 8 active resource rows: `ld185.pak`, `ui_n.pak`, `ui1.wzl`, `Magic8-16.wzl`, `magicre.wzl`, `Mon26.wzl`, `Magic.wzl`, and `Mon24.wzl`. Each row is a resource file name, not an item/effect definition by itself.
- `EffectItemList.txt` sample facts: 12 active `itemName effectId` rows. Names include `传奇神甲(男) -> 1`, `传奇神甲(女) -> 2`, `主宰神剑 -> 3`, `主宰神甲(男) -> 4`, and `主宰神甲(女) -> 5`, with several upgraded names sharing the same IDs.
- `EffectList.txt` sample facts: 1 active row, effect ID `6`, remark `锁定特效`, and 42 numeric fields before the remark. This active row matches `SETITEMEFFECT boxitem0 6` in `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt`.
- Nearby backup lesson: `样本Mir200/Envir/EffectList_bak.txt` contains older active-looking definitions for IDs `1` through `5` with remarks `传奇甲男`, `传奇甲女`, `主宰剑`, `主宰男`, and `主宰女`. Because it is a backup file, do not treat these rows as active runtime definitions unless the project explicitly restores or imports them.
- Cross-file chain: item default visuals can be configured by `EffectItemList.txt -> EffectList.txt effectId -> EffectImageList.txt resource index/file`, while script-driven item mutation uses `SETITEMEFFECT -> EffectList.txt effectId`. Verify both chains when an item has no visible effect or a script uses an unknown ID.
- Parsing lesson: read `EffectItemList.txt` from the right because the final token is numeric and the item name may contain Chinese punctuation or spaces in other projects. For `EffectList.txt`, split numeric fields from the trailing remark, but preserve the full row order and do not collapse `-1` or blank-looking option positions.
- Accuracy lesson: only IDs present in active `EffectList.txt` are proven usable for `SETITEMEFFECT` in the current sample. IDs found only in `EffectItemList.txt` or `EffectList_bak.txt` are references or history until cross-checked against the active list or M2 export.
- Feature-family caution: adjacent files `PillarOfLightEffect.txt`, `PillarOfLightEffectItemList.txt`, `EffectHintBG.txt`, and `EffectHintBGItems.txt` use similar naming but are separate features. `PillarOfLightEffectItemList.txt` comments say `物品名称 效果编号`, and `EffectHintBGItems.txt` comments identify hover-window background effects, so do not mix those effect numbers with equipment `SETITEMEFFECT` IDs without more evidence.

## GroupItemList.txt / GroupItemSkillPowerList.txt

- Sources: `样本Mir200/Envir/GroupItemList.txt` and `样本Mir200/Envir/GroupItemSkillPowerList.txt`.
- Shape: real equipment set-effect configuration plus an INI-style set-skill-power extension. These are authoritative runtime config, unlike `TzItemDescList.txt`, which is player-facing display text.
- Official display cross-check: `knowledge_base/chapters/838-装备套装备注.md` documents only `TzItemDescList.txt` display syntax, so use it to compare visible descriptions, not to infer actual effect values.
- Official percentage cross-check: `knowledge_base/chapters/847-调整人物套装属性百分比.md` documents set percentage indexes `0-25`, including MaxHP/MaxMP, defense, magic defense, attack, magic, taoism, accuracy, agility, magic dodge, poison dodge/recovery, HP/MP recovery, and newer attack families. This matches sample percentage rows such as `皓宇6件` using nonzero HP/MP and defense percentages.
- Official new-attribute cross-check: `knowledge_base/chapters/345-调整物品新增属性.md` and `541-检测人物新增属性.md` document new-item attributes `0-26`, including anti-paralysis, anti-revival, anti-poison, anti-firewall, anti-freeze, anti-cobweb, critical values, resistances, and kill-exp rate. The sample's 27-value final numeric array matches this index family.
- Official skill-power cross-check: `knowledge_base/chapters/304-设置技能伤害防御.md` documents skill-ID keyed attack/defense percentage or point adjustments and says M2 `列表信息2-技能威力设置` combines global settings with private command settings. `GroupItemSkillPowerList.txt` uses the same `Attack<skillId>` / `Defense<skillId>` naming pattern for set-triggered skill power.
- `GroupItemList.txt` static report: 36 active rows. Every row has 9 outer fields. The observed shape is `setId requiredCount setName itemList pointArray40 percentArray40 baseArray40 newAttributeArray27 remark`.
- `GroupItemList.txt` item lesson: field 4 is a `|`-separated candidate item list. It is not the same as visible slots in `TzItemDescList.txt`; display rows may group alternatives such as male/female armor, while this file stores all acceptable names flattened.
- Threshold lesson: field 2 is the required equipped count. Field 4 may contain more item names than the threshold, for example 33 candidate names for `皓宇6件`, while only 6 equipped matches activate that row.
- ID lesson: field 1 is the set row ID. It links `GroupItemSkillPowerList.txt` sections and is the safest key for cross-file work. Do not link by set name alone because several rows reuse names such as `星王套装属性`.
- Array lesson: fields 5-8 are positional numeric arrays. In the sample, fields 5-7 each have 40 values and field 8 has 27 values. Preserve zeros and order; a single missing `|0` shifts every later attribute.
- Point/percent/base lesson from sample: rows such as `星王` and `王者` put additive combat stats in the third 40-value array, while rows such as `皓宇` and `皓尊` put HP/MP/defense/combat percentages in the second 40-value array. Some rows also use the third 40-value array index 19 for experience multiplier-like values shown by remarks such as `经验倍数为6倍`.
- Special-flag lesson: rows such as `龙纹盾` and `强化麻痹戒指` use the first 40-value array for special binary-style effects. `龙纹盾` has nonzero indexes 9, 10, and 19, matching the remark `防蛛网，防全毒`; `强化麻痹戒指` has index 20 set to `1`, matching the remark `魔道麻痹`. Treat this as a distinct special flag/effect family unless a manual page supplies an exact table.
- New-attribute lesson: shield rows `铁卫盾` through `龙纹盾` use the 27-value array index 13 for anti-paralysis values such as `15`, `30`, `40`, `60`, and `100`. This follows the new-item attribute index family documented by `345`/`541`, where index 13 is anti-paralysis.
- HP/MP recovery caution: manual chapter `124-套装属性体力恢复和魔法恢复百分比.md` says HP/MP recovery percentage needs a base point value in the adjacent point attributes. Do not configure or explain HP/MP recovery percent from the percentage array alone.
- `GroupItemSkillPowerList.txt` static report: 18 sections, all keyed by numeric set IDs that exist in `GroupItemList.txt`. Each section has 154 keys, formed as `Attack<skillId>=value` and `Defense<skillId>=value`.
- Skill-power sample fact: only section `[20]` has nonzero values: `Attack13=10`, `Attack22=10`, and `Attack26=10`. `GroupItemList.txt` row ID `20` is `火焰戒指特殊加成`, and its remark says fire ring effects increase `烈火`, `火墙`, and `火符` damage by 10%, so this section is the actual skill-power payload for that set row.
- Adjacent single-item comparison: `样本Mir200/Envir/SkillPowerItemList.txt` uses `[强化复活戒指]`, `[强化护身戒指]`, and `[强化麻痹戒指]` sections with `Attack<skillId>=20` entries. That file is item-name keyed; `GroupItemSkillPowerList.txt` is set-ID keyed.
- Accuracy lesson: before saying a set grants an effect, read `GroupItemList.txt` by ID and threshold, then read matching `GroupItemSkillPowerList.txt` section, then compare `TzItemDescList.txt` only as display text. If a tooltip and real arrays disagree, the arrays are the runtime evidence and the tooltip may be stale.
- Editing caution: do not reorder rows, rename set IDs, or trim zero-filled arrays by hand. If adding a skill-power section, use an existing section as a shape template so the full skill key set remains present.

## ItemRuleList.txt / ItemDescList.txt

- Sources: `样本Mir200/Envir/ItemRuleList.txt` and `样本Mir200/Envir/ItemDescList.txt`.
- Shape: item behavior-rule table plus item hover/remark display table. `ItemRuleList.txt` is runtime rule configuration from M2 `列表信息2 -> 物品规则`; `ItemDescList.txt` is player-facing explanatory text.
- Official item-rule cross-checks: `knowledge_base/chapters/705-物品捡取和丢弃触发.md` and `706-物品捡取和丢弃触发.md` document item-rule-gated pickup/drop QF triggers and the global `@PickUpItemEX` exception; `704-物品掉落触发.md` documents monster-drop trigger; `664-人物身上物品掉落触发.md` documents body-drop and hero body-drop triggers; `317-特修装备.md` and `454-特修身上装备.md` tie repair blocking to item rules; `513-宝石升级系统.md` ties gemstone-upgrade blocking to item rules; `735-宝箱获取物品触发-宝箱触发.md`, `737-爆率透视.md`, and `793-拍卖行.md` tie other item-rule options to chest prompts, drop see-through, and auction allow rules.
- Official item-remark cross-checks: `knowledge_base/chapters/099-悬浮式装备信息窗口支持图片显示.md` documents item remark syntax, including color lines, inline `{text|color}`, `<looks:...>`, `<NewopUI:...>`, `<Img:...>`, `<PlayImg:...>`, and `<ImgNum:...>`; `819-镶嵌宝石设置说明.md` says `ItemDescList.txt` can be found in the Mir200 directory or M2 list-info UI and gives simple remark examples.
- `ItemRuleList.txt` static report: 25 active rows. Every row has exactly 40 numeric fields before `|` and 10 numeric fields after `|`; all 10 extension fields are zero in this sample.
- `ItemRuleList.txt` parsing lesson: do not parse by a fixed first token if item names may contain spaces in another project. Split at `|`, read the final 40 numeric tokens on the left as the main rule flags, read the 10 numeric tokens on the right as extension flags, and keep everything before those 40 numbers as the exact item name.
- `ItemRuleList.txt` sample-position lesson: active nonzero main positions include 0, 1, 2, 3, 4, 7-11, 13-18, 20, 24, and 31. The common pattern for money and special consumables uses positions 0 and 4; many bound/task-like consumables add positions 1, 13, and 24. Treat these as sample patterns only until matched to M2 column labels or official notes.
- `ItemRuleList.txt` feature caution: the manual proves the table controls several feature switches, but it does not provide a current complete exported-column map. Do not say "column N means X" unless a chapter, UI export, comment, or a controlled comparison row confirms it.
- Script cross-check: `样本Mir200/Envir/Market_def/QFunction-0.txt` uses `[@ItemUpgrade]` to route gemstone-upgrade behavior and `[@BeginUseExpSpiritBeads]` to gate spirit-bead use by level. These are related runtime flows, but not proof of a specific `ItemRuleList.txt` column by themselves.
- Project-list cross-check: `样本Mir200/Envir/QuestDiary/系统功能/禁止邮寄道具.txt` contains many of the same special item names as `ItemRuleList.txt`. This is a separate project deny list, so mail/storage restrictions may be enforced outside item rules too.
- `ItemDescList.txt` static report: 98 active rows. Rows are shaped as `itemName=color/text\color/text...`; sample rows have 1 to 4 display segments. Color `218` is used almost everywhere.
- `ItemDescList.txt` parsing lesson: split only at the first `=`. The sample has `战神油==218/...`, producing a color-like value `=218`; keep malformed-looking data intact when reading or editing unless the user explicitly wants cleanup.
- Display lesson: `\` separates hover remark lines. Each segment may carry its own `color/text`, for example `替死鬼符=218/通过邪恶巨人心脏合成而来的道具\218/死亡后可原地复活一次\218/每次登录只生效一次！`.
- Accuracy lesson: `ItemDescList.txt` often describes restrictions such as `无法交易`, `禁止丢弃`, `丢弃消失`, or usage conditions. These are visible hints, not the enforcement source. Verify actual restrictions in `ItemRuleList.txt`, item state commands like `GIVESTATEITEM` / `SetItemState`, QFunction callbacks, and project-specific deny lists before making balancing or anti-exploit claims.
- Cross-file example: `ItemDescList.txt` says `火焰戒指` increases `烈火`, `火墙`, and `火符` by 10%; actual set skill power was found earlier in `GroupItemList.txt` ID `20` plus `GroupItemSkillPowerList.txt` section `[20]`. Use item remarks as a navigation hint, not final evidence.
- Editing caution: preserve GBK/ANSI encoding, exact item names, line order, the `|` separator in `ItemRuleList.txt`, zero placeholders, and backslash-separated remark segments in `ItemDescList.txt`.
