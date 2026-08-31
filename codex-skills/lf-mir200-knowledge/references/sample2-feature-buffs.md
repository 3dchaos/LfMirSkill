# Sample2 Mir200 Feature Buff Patterns

Use this reference when analyzing or designing feature-rich buffs, inscription-like properties, awakening skills, pet contracts, and combat-state systems based on `样本2Mir200`.

## Scope

`样本2Mir200` is a strong example of a build-oriented Mir200 version. Its distinguishing layer is not one table or one NPC, but a chain:

1. NPC entry points expose systems such as flow schools, awakening seals, gem inlay, equipment appraisal, equipment strengthening, and sword-buff washing.
2. Flow-school scripts grant or replace skills and call central stat recalculation labels.
3. Login/QFunction scripts rehydrate persistent timed buffs and recalculate derived stats.
4. Attack triggers apply short debuffs, counters, bleed/curse states, and target-side recalculation.
5. Item remarks, custom property text, set tables, and skill-power tables package the same mechanics as player-facing "hidden property", "gem", "exclusive skill", or "contract" affordances.

Treat this reference as sample-derived practice. Cross-check command syntax against the official manual before writing new scripts.

## Key Files To Read First

- `样本2Mir200/Envir/MerChant.txt`
  - Notable entry points: `[技能大师]\流派`, `[神剑BUFF洗炼]\神剑谱`, `[隐藏属性解封]\装备鉴定`, `[超级属性增幅]\装备强化`, `[合成与镶嵌宝石]\宝石镶嵌`, `洗练觉醒之印`.
- `样本2Mir200/Envir/QuestDiary/游戏登陆/流派BUFF读取.txt`
  - Maps selected flow-school skills to stat readers, skill replacement, pet readers, or buff checks.
- `样本2Mir200/Envir/QuestDiary/游戏登陆/登陆脚本.txt`
  - Central stat-recalculation labels such as `@_@元素读取`, `@_@五维读取`, `@_@攻魔道读取`, `@_@HPMP读取`, `@_@防御读取`, `@_@攻速读取`, `@_@施法速度`, `@_@吸血读取`, `@_@技能威力读取`, `@_@技能等级读取`, `@_@BB读取`, `@_@BUFF检测`.
- `样本2Mir200/Envir/Market_Def/QFunction-0.txt`
  - Global callbacks and state mutation surface. It calls the same stat readers after item use, buff expiry, pickup/equipment changes, and feature interactions.
- `样本2Mir200/Envir/QuestDiary/攻击触发/攻击掉血前触发.txt`
  - Combat debuff and proc examples: `邪爆符`, `咒蛊术`, `体态压迫`, `撕裂`, `失心锁`.
- `样本2Mir200/Envir/CustomMagic/*.ini`
  - Custom skill visuals and server-side attack definitions. Names reveal the build families: `狂暴`, `浴血狂攻`, `秘法暴击`, `极冰魔盾`, `灵蛊秘种`, `魂兽狂化`, `召唤虹魔教主`, `金刚不坏`, etc.
- `样本2Mir200/Envir/CustomItemPropertyTextVarList.txt`
  - Player-facing custom-property text variables for gem/strengthening/hidden property display.
- `样本2Mir200/Envir/ItemDescList.txt`
  - Player-facing remarks for hidden properties, awakening books, exclusive skills, contracts, gems, and special weapons. Do not treat it as enforcement by itself.
- `样本2Mir200/Envir/GroupItemList.txt`, `GroupItemSkillPowerList.txt`, `SkillPowerItemList.txt`, `TzItemDescList.txt`
  - Runtime set effects, set skill-power extensions, single-item skill-power extensions, and display remarks.

## Implementation Patterns

### Central Attribute Readers

This sample avoids scattering final stat math everywhere. Mutating scripts usually change a marker, text line, item state, skill, or timer, then call one or more central readers in `登陆脚本.txt`.

Common reader groups:

- Combat element/added attributes: `@_@元素读取`
- Five-dimensional and hit/evasion style stats: `@_@五维读取`
- Attack/magic/dao totals: `@_@攻魔道读取`
- HP/MP totals: `@_@HPMP读取`
- Defense/magic defense: `@_@防御读取`
- Speed surfaces: `@_@攻速读取`, `@_@施法速度`
- Life steal: `@_@吸血读取`
- Skill scaling: `@_@技能威力读取`, `@_@技能等级读取`
- Pet scaling: `@_@BB读取`

When designing similar features, add or clear state first, then call the smallest set of readers affected by that state. If a state affects multiple derived dimensions, call all of them explicitly.

### Flow-School Buff Dispatch

`流派BUFF读取.txt` groups by class label: `@_@战士BUFF`, `@_@法师BUFF`, `@_@道士BUFF`.

The pattern:

1. Read the selected school via a project function-like variable such as `<$战士流派(<$STR(U1)>,1)>`.
2. Raise or normalize the selected skill level, usually with `SKILLLEVEL`.
3. Branch by exact school name.
4. Either call central readers, replace a base skill, add a companion skill, or kill/reset summons.
5. End each matched branch with `BREAK`.

Examples by behavior:

- Stat-only school: `神准强攻` calls five-dimensional and attack/magic/dao readers.
- Survivability school: `神血铁壁` calls HP/MP and defense readers.
- Speed school: `骤雨` calls attack-speed reader.
- Skill replacement: `玄冰术` deletes `雷电术`; `唤魂术·虎` deletes `诱惑之光`; `召唤虹魔教主` replaces `召唤神兽` while preserving the key binding.
- Pet school: `魂兽狂化`, `御兽术`, `灵心契约` call `@_@BB读取`.

### Timed Buff Rehydration

Persistent timed buffs store expiry or remaining state in saved variables, then rebuild the UI and derived stats on login or feature refresh.

Observed pattern:

1. Store an absolute expiry such as a `U` variable.
2. On login/refresh, compute remaining time with `FORMULATION <expiry>-<$UTCNow>`.
3. Display via `SetArrBuff`.
4. Call affected readers.
5. Use `[@CloseArrBuffX]` to clear the state and recalculate.

Sample buffs:

- `苹果`: HPMP +200, attack/magic/dao upper +12, attack speed +2.
- `满江红`: kill-monster experience multiplier +45%.
- `幸运药水`: temporary luck 9.

Official manual anchor: `knowledge_base/chapters/115-自动排列自定义按钮倒计时触发.md` for `SetArrBuff`, `CloseArrBuff`, and close/click labels.

### Target-Side Debuffs

Attack-trigger debuffs often mutate the target with the `M.` prefix, set a target-side marker, show a target-side `SetArrBuff`, and force target stat recalculation.

Examples:

- `咒蛊术`: sets target `S$咒蛊术`, displays curse buff, and makes curse +3 active for the duration.
- `体态压迫`: sets target marker and calls target HP/MP reader; close label clears the marker.
- `失心锁`: lowers magic evasion through a marker and target five-dimensional recalculation.
- `撕裂`: displays bleed; damage-over-time logic must be audited separately from the display icon.
- `邪爆符`: keeps a hit counter on the target; when threshold is exceeded, clears the buff/counter and applies burst damage.

When reproducing this style, always pair:

- start label: set marker + `M.SetArrBuff` + target recalculation
- close label: clear marker + target recalculation
- anti-stacking guard: check existing target marker or counter before adding again


### Equipment-Slot Driven Persistent Buffs

For buffs driven by an equipped item slot rather than a consumable timer, separate state, UI, and proc feedback.

- Use `CHECKUSEITEM <pos>` plus `GetItemFieldValue <pos> name S$...` before opening or refreshing the buff, and repeat the same confirmation inside combat callbacks before any high-value proc.
- Treat unequip, death, item drop, durability exhaustion, and script-side item removal as the same cleanup problem: close the module, clear markers, close the icon, and let short-duration stat changes expire naturally.
- For the main self icon, the official `SetArrBuff` manual says parameter 5 is countdown time; `-1` means button/persistent icon and values above 0 mean countdown. Use `SetArrBuff ... -1 0 0 0 <tooltip>` when the user expects a non-counting persistent status icon.
- Close auto-arranged icons by button number, not by group plus button. If the icon was opened as `SetArrBuff 1 87 ...`, the project-verified close command is `CloseArrBuff 87`; `CloseArrBuff 1 87` can leave the icon visible in this pattern.
- Cleanup labels should close the icon and stop the refresh timer before clearing current state. Refresh labels should make "no equipped item" an absolute terminal branch that calls cleanup and then `BREAK`, so later refresh logic cannot recreate the stale icon.
- Do not print proc messages merely because a direction branch was reached. Have the module set a success marker such as `N$...触发成功 1` only after an actual damage change, state change, target marker, or heal runs, then let the dispatcher send `SENDMSG` if the user's quiet flag is not set.
- Item remarks for slot-driven buffs should disclose the player contract: equipped slot, build direction, trigger skills or trigger moments, visible effect, quality unlocks, and player feedback. Keep developer contract details such as refresh timers, temporary stat duration, audit/recheck wording, cleanup internals, script recovery, and diagnostic records in implementation docs or comments, not in player-facing `ItemDescList.txt` or buff hover text.
- Validate generated item remarks against the runtime script/config source. `ItemDescList.txt` remains display text: it can explain a feature, but it is not proof that the feature is enforced.

#### Lightweight Timer Checks And Effect Renewal

Treat an explicit time argument on a persistent equipment effect as a renewable lease, not as permanent state. This includes `ChangeHumAbility`, `AddHumNewValue`, `ChangeSpeed`, `ChangeState`, and any other command whose manual defines a duration.

- Split the lifecycle into three paths: full refresh on equip/change/dirty state, lightweight renewal while the same item remains equipped, and cleanup on removal/death/drop. The unchanged timer path must not simply `BREAK` when the active effects have finite durations.
- Keep the renewal interval shorter than the effect duration with enough margin for timer jitter. A 2-second heartbeat renewing 3-second effects is a valid short-lease pattern; skipping one renewal makes the effect visibly disappear.
- Inventory every time-bounded command in module refresh labels and mirror it in the lightweight renewal path. Audit base attributes, route-specific attributes, `ChangeSpeed`, `ChangeState`, and hidden/new values together; checking only MaxHP misses the same regression in speed, life steal, resistances, and other leased effects.
- Restore intentional periodic behavior that previously ran through the full refresh, such as cooldown decrement, pet replacement, or periodic healing. Exclude one-time lifecycle work such as config parsing, icon rebuilding, module initialization, and unconditional state resets.
- Keep the renewal call graph shallow and acyclic. Dispatch only the active class/module, use cached validated configuration values, end each branch with `BREAK`, and avoid re-entering the full refresh from an unchanged-state heartbeat.
- Prefer short leases plus timer shutdown on cleanup when direct clearing would be unsafe. Changing leased effects to online-indefinite values requires complete removal handling, and broad `= 0` cleanup can overwrite another feature that contributes to the same engine attribute.
- Statically validate both sides of the contract: the timer handler reaches the renewal dispatcher, every leased effect has a renewal counterpart, recurring gameplay actions still have a tick path, removal stops the timer, and the renewal graph stays below the configured script-jump budget.

#### 老登军鼓 Reference Pattern

For the 老登 project's 14-slot 军鼓 system, the reusable chain is:

1. `QFunction-0.txt` equipment callbacks refresh or clear the 14-slot feature.
2. `QuestDiary/系统功能/军鼓流派配置.txt` maps exact item names to job, direction, quality, stage, conflict group, and module.
3. `QuestDiary/系统功能/军鼓BUFF.txt` owns lifecycle state, icon refresh, combat confirmation, and feedback dispatch.
4. `QuestDiary/系统功能/军鼓流派/*.txt` modules set temporary stats and proc success markers.
5. `ItemDescList.txt` gives player-facing remarks only.

Reusable rules from that pattern:

- Match all equipment names exactly through the config table. Do not fuzzy-match quality or direction names.
- Before any combat proc, re-read slot 14 and compare the item name against the current cached name. If the item is missing or changed, call refresh/cleanup and stop the proc.
- When Timer87 performs only an equipment-name/dirty-state check, route the unchanged-item branch to a dedicated renewal dispatcher. Renew all 3-second class and direction effects, warrior attack speed, wizard cast speed, Taoist pet replacement cooldown, and intended periodic healing without rerunning config, icon, or module-open chains.
- For the persistent self icon, use `SetArrBuff 1 87 ... -1 ...` and close with `CloseArrBuff 87`.
- Use the local quiet flag for this feature's chat surface. In this project, 军鼓 trigger printing uses `[63]`.
- Player-facing buff text should say what the player can act on: name, class, direction, quality, gameplay, and trigger effects. Keep safety/audit wording out of the hover text.
- Player-facing item text should say position, build direction, trigger skills, visible effect, and quality unlocks. Avoid terms like "复核", "清理", "基础", "机制", "安全", "记录", "2秒定时", "3秒短时", "脚本回收", or "确认14号位仍是当前物品".
### Consumable Social Buffs And Curses

Some sample states are used as social/interactive items, not only combat procs:

- `苗疆蛊毒`: one player can apply a daily all-stat debuff to another, unless prevented by related protection such as `百毒不侵`.
- `伤风感染`: daily all-stat debuff with a narrative counterplay hook: a `百草回春`/`药王` player can attempt early detox.
- `死不瞑目`: death retaliation curse from killed player to killer, with small-logout retention.

These systems combine `SetArrBuff`, saved variables, target-prefixed commands, and recalculation labels. The design lesson is to model a buff as both UI state and stat state.

### Inscription-Like Property Surfaces

`样本2Mir200` does not use one universal "铭文" file. Its inscription-like mechanics are split across:

- `CustomItemPropertyTextVarList.txt`: rich text templates for custom property display.
- `ItemDescList.txt`: hidden-property and exclusive-skill remarks.
- Gem/item scripts and NPCs: actual mutation and material flow.
- Runtime property commands such as `SetCustomItemAbil`, `SetCustomItemValue`, `SetNewItemValueEx`, or nearby feature-specific commands, depending on implementation.

Common property families:

- Critical build: crit chance, crit damage, crit resistance / ignore crit.
- Sustain build: HP/MP, HP/MP regen, potion recovery, life steal.
- Damage targeting: damage to monsters, damage to players, true damage.
- Control and resistance: freeze chance, poison recovery, paralysis/freeze/spider-web immunity, single-hit damage cap.
- Pet build: pet attack, pet HP, pet all attributes, pet crit.
- Skill build: specific skill damage lines such as flame, thunder, ice roar, soul fire, fire rain.

Official manual anchors:

- `knowledge_base/chapters/842-自定义属性说明书.md` for custom item attributes.
- `knowledge_base/chapters/346-调整物品新增属性.md` for new item element attributes.
- `knowledge_base/chapters/819-镶嵌宝石设置说明.md` for gem remark/display concepts when applicable.

### Hidden Properties And Exclusive Skills

`ItemDescList.txt` reveals the build affordances, but it is display metadata. Use it to discover systems, then confirm effects in runtime scripts/tables.

Distinctive examples:

- `弑神剑`: executes low-HP targets.
- `远古契约`, `先祖契约`: pet all-attribute scaling.
- `毒龙之殇`: monster poison proc for warrior/mage and green-poison boost for Taoist; also has a `GroupItemList.txt` buff row.
- `浴血狂攻`: active short burst with HP cost, attack speed, life steal, and crit.
- `魔冥咒`: trades physical attack for true-damage style extra scaling from magic/dao.
- `金刚不坏` and `剑气爆`: mutually exclusive forms.
- `圣心御防诀`: party support buff for defense and attack/magic/dao.
- `灵心契约`, `召唤虹魔教主`, `召唤牛魔王`: pet-contract progression.

### Set And Skill-Power Tables

For sets, separate three layers:

1. `GroupItemList.txt`: runtime required count, item candidates, attribute arrays, new-attribute arrays, and remark field.
2. `GroupItemSkillPowerList.txt`: skill-ID keyed damage/defense additions for a set ID.
3. `TzItemDescList.txt`: player-facing set tooltip only.

Do not infer runtime behavior from tooltip text alone. Preserve every `|` placeholder in fixed arrays and link `GroupItemSkillPowerList` sections by active set ID.

## Design Guidance For Similar Features

- Use exact names. Flow names, skill names, item names, and buff labels are string-matched; do not normalize variants.
- Make one central recalculation surface per attribute family. Feature scripts should mutate state and call readers, not duplicate all math.
- Pair every timed buff with close cleanup. If a `SetArrBuff` changes stats, `CloseArrBuffX` must clear the marker and rerun affected readers.
- Pair every equipment-slot persistent icon with explicit close commands on all equipment-disappearance paths. For auto-arranged self icons, prefer the project-verified `CloseArrBuff <buttonNo>` form, such as `CloseArrBuff 87`.
- Store long-lived timed state in saved variables and rehydrate on login. UI icons alone are not state.
- Use target-prefixed commands deliberately. Debuffs on victims need `M.` or named-player prefixes and victim-side recalculation.
- Treat rich item remarks as discovery clues. Confirm actual enforcement in scripts, custom property commands, set tables, item rules, and QFunction callbacks.
- For pet/contract skills, audit base-skill replacement, key binding preservation, `KillSlave`, and pet stat recalculation together.
- For mutually exclusive forms, explicitly close/clear the competing form before opening the new one.

## Static Validation Checklist

- Search all feature names in `QuestDiary`, `Market_Def/QFunction-0.txt`, `ItemDescList.txt`, `CustomMagic`, and set/skill-power tables.
- For every `SetArrBuff` affecting stats, find the matching `[@CloseArrBuffX]`.
- For every equipment-slot persistent `SetArrBuff`, statically verify a close path for login refresh, timer refresh, unequip, drop, durability loss, script removal, and death checks. Search for stale `CloseArrBuff <group> <button>` forms when the local project expects `CloseArrBuff <button>`.
- For every equipment-driven effect with an explicit duration, compare the full-refresh commands with the unchanged-state renewal label and verify the timer interval is shorter than the lease. Include recurring cooldown, summon, and healing work that depended on the old refresh cadence.
- For every target-side `M.SetArrBuff`, verify `M.` marker writes and target recalculation labels.
- For every player-facing hidden-property remark, locate a runtime source: custom item property table, item new-value command, attack trigger, set table, or skill-power table.
- For player-facing remarks and buff hover text, grep for developer-only terms such as `复核`, `清理`, `基础`, `机制`, `安全`, `记录`, refresh intervals, temporary-duration internals, and script-recovery wording.
- For every flow-school branch, confirm `BREAK` after the intended action and no accidental fall-through into later `#IF` blocks.
- For every skill replacement, preserve shortcut keys before `DELSKILL` and restore them after the replacement when the sample pattern does so.
