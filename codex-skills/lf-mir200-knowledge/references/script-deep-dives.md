# Mir200 Script Deep Dives

Use this file for compact lessons learned from one named script. Keep each entry short: record the structure, official chapters to verify, and durable script-writing lessons. Do not paste whole scripts here.

## Method

1. Run `python <skill-dir>\scripts\lf_kb.py learn-script "<relative-script-path>"`.
2. Inspect the target script and every `#CALL` target relevant to the user's question.
3. Inspect each manual chapter listed in `manual_topics`.
4. Write down: entry labels, dispatch links, guards, actions, state writeback, failure path, and external dependencies.
5. Promote only durable cross-script rules into `SKILL.md`; keep script-specific observations here.

## 老登辅助 / 辅助.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt`
- Shape: composite helper panel with a big dialog, toggle flags, parameterized labels, delegated feature scripts, personal timers, input controls, item-box mutation, and currency conversion.
- Static report: 64 labels, 7 `#CALL` targets, 34 personal flags, 9 NPC input references, 1 `ITEMBOX`, 3 timer IDs (`10`, `84`, `3`), and variable families `N$`, `N`, `S`, `T`, `U`, `A`, `G`.
- Official chapters to cross-check: `028-CallEx支持多个同样的@地址.md`, `787-扩展NPC脚本点击触发带参数-NPC标签带参数.md`, `163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`, `624-NPC对话框内默认输入框.md`, `205-个人定时器.md`, `608-扩展check支持批量检测.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`.
- Dispatch lesson: `辅助功能` builds the panel; most feature labels toggle a flag then `goto @辅助功能`, while heavier flows delegate through `#CALL` to sibling scripts.
- Parameter lesson: labels such as `召唤配置(骷髅,1)` rely on `<$SCRIPTPARAM1>` and `<$SCRIPTPARAM2>`. The manual warns parameters are label-local and can be cleared by later jumps, so copy them to variables before a flow can jump away.
- Flag lesson: UI checkmarks use `<$flag(n)>`; action labels use `check [n] 0/1`, `SET [n] 1/0`, and sometimes `reset [75] 19`. Treat these as personal feature switches and map each flag to its UI row before editing.
- Timer lesson: feature toggles pair `SetOnTimer n seconds` with `SetOffTimer n`. The corresponding runtime labels live in `MapQuest_def/QManage.txt` as `[@OnTimer<n>]`, so changing timers requires checking both files.
- Item-box lesson: `装备锁定` uses `ITEMBOX` and then `SetUpgradeItem 0`, `ChangeItemName boxitem0`, `SETITEMSTATE`, `SETITEMEFFECT`, `UpdateItem boxitem0`, and `ReturnBoxItem 0`. Always check that every failure path returns the box item.
- Variable lesson: `N$边框色值*` are temporary UI color variables, `U9/U13/U22/U23` are saved numeric player settings, `T5/T50-T53` are saved string player settings, `A687/A688` pass global follow-request state, and `G3` gates hero features. Choose variable families by lifetime from `628-程序变量说明.md`.
- Static caution: several `#CALL` lines are commented out. Treat commented calls as design clues, not active execution paths.

## 云隐宗师 / 云隐宗师.txt

- Source: `样本Mir200/Envir/Market_def/云隐宗师.txt`
- Shape: rebirth and class-reset panel with menu dispatch, hero-side handling, attribute reset, rebirth, class change, and downgrade flow.
- Static report: 5 labels, no `#CALL`, no timers, `G3`, `N$资源编号`, `N$削减等级`, `N$转生等级`, `N$转生次数属性点`, `N$转生属性点`, `N$聚灵珠小`, and `S$转职`.
- Official chapters to cross-check: `084-人物转生.md`, `393-转换职业.md`, `102-一键回收包裹物品.md`, `159-删除仓库物品.md`, `298-删除所有技能.md`, `163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`.
- Lesson: copy branch data into variables before any jump or destructive action, then check hero state, bag space, level caps, and resource items before `CHANGEJOB`/`RENEWLEVEL`/`CLEARSKILL`/storage cleanup.
- Lesson: hero-specific operations need the `H.` prefix where the manual requires it; do not assume the player-side command also affects the hero.

## 火龙将军 / 火龙将军-0.txt

- Source: `样本Mir200/Envir/Market_def/比奇城/火龙将军-0.txt`
- Shape: staged mirror-map gate with wild-map entry, single/team branch, ownership flag, cleanup, scripted spawn, and daily attempt gating.
- Static report: 10 labels, 1 `#CALL` to `系统功能\老登辅助\特效.txt@播放礼花`, flags `251` and `422`, `G0`, `J3`, `N$火龙成功判断`, and `N$火龙一刷新次数`.
- Official chapters to cross-check: `635-动态创建镜像地图.md`, `351-通过脚本建立一个NPC-动态创建NPC.md`, `175-编组地图传送.md`, `256-脚本刷怪.md`, `608-扩展check支持批量检测.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`, `163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`.
- Lesson: `AddMirrorMap`'s last argument is a variable name, not a literal value; clear old mirror state before rebuilding and pair instance flow with explicit cleanup.
- Lesson: dynamic NPC scripts belong in `Market_def`, and team travel should use `GROUPMAPMOVE` rather than ad hoc teleport branches when the whole party must move together.

## 冶炼金矿 / 冶炼金矿.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/冶炼金矿.txt`
- Shape: UI-driven smelting loop with a task entry, branch labels for single/batch handling, reward counters, and a completion flag.
- Static report: 6 labels, flag `5`, `N$边框色值1-3`, `N$金矿数`, `N$资源编号`, `N$循环次数`, `N$获得金币`, `N$获得金条`, `N$获得金砖`, and `N$获得金盒`.
- Official chapters to cross-check: `163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`, `608-扩展check支持批量检测.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`.
- Lesson: initialize loop counters before entering `While`-style reward logic, keep preconditions separate from the random branch, and write counters back explicitly for each reward outcome.
- Lesson: if a cost or item check is part of the flow, keep the guard visible in its own branch so the reward loop stays easy to audit later.

## 存仓 / 存仓.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存仓.txt`
- Shape: persistent per-player auto-storage list with menu entry, selection handling, list rebuild, and file-backed writeback.
- Static report: 6 labels, `L$存仓数组`, `S$显示内容`, `N$选择内容`, `N$数组数量`, `N$物品循环开始`, and saved timer/state field `T0`.
- Official chapters to cross-check: `192-多元数组元素变量.md`, `418-读取文本内容到变量.md`, `460-写入指定文本文件.md`, `299-删除文本指定行.md`, `787-扩展NPC脚本点击触发带参数-NPC标签带参数.md`, `163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`.
- Lesson: prefer `L$` for in-script list processing, then persist the per-player list through text-file read/write when the data must survive sessions.
- Lesson: the rewrite pattern here is `GetListString` -> mutate list state -> `DelTextListLine`/`AddTextListEx`; keep the rendered `S$` text separate from the underlying storage list.

## QManage / QManage.txt

- Source: `样本Mir200/Envir/MapQuest_def/QManage.txt`
- Shape: central player lifecycle and timer hub with startup initialization, login cleanup, follow coordination, UI refresh, auto-repair, auto-pick, activity calls, hero login/logout, and external account check.
- Static report: 25 labels, 10 `#CALL` targets, flags `30/31/59/63/65/66/67/68/95/98/99/100/116`, timer IDs `2/3/4/5/9/10/84/117`, and variable families `A`, `G`, `T`, `N$`, `L$`.
- Official chapters to cross-check: `205-个人定时器.md`, `141-毫秒级个人定时器.md`, `028-CallEx支持多个同样的@地址.md`, `192-多元数组元素变量.md`, `407-字符检测命令GetStringPosEX.md`, `418-读取文本内容到变量.md`, `460-写入指定文本文件.md`, `628-程序变量说明.md`.
- Lesson: timer features are two-file systems: feature scripts set flags or `SetOnTimer`, while `QManage` owns `@OnTimerX` and usually delegates to focused helper scripts.
- Lesson: login code is also state repair code; it clears stale flags, rebuilds UI buttons, initializes per-player text files, and rebinds hero/player synchronized systems.

## 踏云尊者 / 踏云尊者-yssd.txt

- Source: `样本Mir200/Envir/Market_def/其它区域/踏云尊者-yssd.txt`
- Shape: NPC equipment-element release flow with stage flags, unlock material, `ITEMBOX`, random cost, `L$` candidate elements, element cap scan, item binding, mutation, update, and return/failure handling.
- Static report: 8 labels, flags `255` and `256`, `ITEMBOX:6`, `U19`, `L$元素属性表`, and `N$元素上限`, `N$次数上限`, `N$随机消费熔炼值`, `N$熔炼几率`, `N$元素位置`.
- Official chapters to cross-check: `397-自定义OK框.md`, `192-多元数组元素变量.md`, `263-扩展MOVR使用方法.md`, `345-调整物品新增属性.md`, `541-检测人物新增属性.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`.
- Lesson: use `L$` as a mutable candidate set, delete saturated element slots while scanning, then `MOVR` a remaining index instead of hardcoding many random branches.
- Lesson: OK-box mutation must bind the box item with `SetUpgradeItem`, apply item changes, `UpdateItem`, and deliberately return or consume the item on every path.

## 邮箱 / 邮箱.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/邮箱.txt`
- Shape: file-backed mail UI that renders inbox state, accepts recipient/message input, stores item metadata and full equipment attributes, then reconstructs the item on receive.
- Static report: 5 labels, input IDs `4` and `5`, `ITEMBOX` groups `#B1~#B2` and `#L1~#L2`, arrays `L$物品属性数组`, `L$禁邮道具`, `L$道具具体数据`, and many `S$`/`N$` fields for display and item metadata.
- Official chapters to cross-check: `397-自定义OK框.md`, `624-NPC对话框内默认输入框.md`, `192-多元数组元素变量.md`, `418-读取文本内容到变量.md`, `460-写入指定文本文件.md`, `299-删除文本指定行.md`, `172-绑定给予的装备进行命令操作.md`, `643-扩展GIVE命令.md`, `752-对捡取的物品进行关联.md`.
- Lesson: mail is not just `GIVE` plus text; it serializes the mail header separately from item data, then rebuilds add-values, element values, source fields, and custom text after `LINKGIVEITEM`.
- Lesson: UI text assembly belongs in `S$显示内容`; authoritative mail state belongs in per-player text files and item detail files keyed by makeindex.

## QFunction / QFunction-0.txt

- Source: `样本Mir200/Envir/Market_def/QFunction-0.txt`
- Shape: engine callback router for UI buttons, map events, group creation, item use, kill/death/level triggers, bag entry, attack hooks, gem upgrade, custom commands, shop creation, and item package effects.
- Static report: 59 labels, 25 `#CALL` targets, flags `4/66/97/99/422`, and callback labels such as `@ButtonClick2`, `@CustomButtonClick`, `@MinMapCustomButtonClick2`, `@AddBag`, `@ItemUpgrade`, `@StdModeFuncXX`, `@StartAutoOnline`, and `@StopAutoOnline`.
- Official chapters to cross-check: `070-脚本增加自定义按钮.md`, `398-自定义UI中自定义按钮使用-预留按钮.md`, `820-小地图边框.md`, `667-物品进入背包触发.md`, `409-不允许宝石升级.md`, `513-宝石升级系统.md`, `696-杀死怪物时触发-杀怪触发.md`, `679-攻击触发.md`, `703-物品触发脚本功能.md`, `007-31类物品扩展设置.md`.
- Lesson: QFunction labels are engine contracts, not ordinary NPC labels; identify the trigger source before editing behavior or renaming labels.
- Lesson: keep callback bodies thin when possible: guard, normalize variables, then `#CALL` a focused helper script. This keeps event-triggered logic auditable and reduces accidental fall-through.

## 帮助菜单 / 帮助菜单.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/帮助菜单.txt`
- Shape: mixed helper/admin panel with public gift/CDK links, `ISADMIN`-guarded GM probes, one external `#CALL`, dynamic NPC creation, item repair test flow, password-file lookup, and one-time reward pickup.
- Static report: 14 labels, 1 `#CALL` to `\典狱长功能\典狱长CDK.txt@典狱长CDK`, flags `255` and `47`, variables `S$盾牌名`, `N$距离平方`, `N$X距离平方`, `N$Y距离平方`, `A41/A42`, `P11/P12`, and no timers or item boxes.
- Official chapters to cross-check: `028-CallEx支持多个同样的@地址.md`, `351-通过脚本建立一个NPC-动态创建NPC.md`, `314-数学表达式运算命令.md`, `418-读取文本内容到变量.md`, `407-字符检测命令GetStringPosEX.md`, `299-删除文本指定行.md`, `217-回收指定位置装备.md`, `401-自动穿取装备.md`, `773-获取物品属性值.md`, `628-程序变量说明.md`.
- Lesson: do not treat every label in helper menus as production flow. First separate public links from `ISADMIN` branches, commented probes, and temporary GM repair/test labels.
- Lesson: file-backed one-time rewards can use `GetStringPosEX` to find the player's line, `GetListString` to split reward fields, `GIVE` to pay, and `DelTextListLine` to consume the entry. Audit path relativity and line numbering before reusing this pattern.
- Lesson: position-based equipment repair should read the current item (`GetItemFieldValue` / display variable), remove or replace the worn item by position (`TakePosW`, `TakeOnItem`), and charge the currency in a guarded branch.

## 探测 / 探测.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/探测.txt`
- Shape: locator service with `INPUTTEXT` player lookup, equipped-item requirement, durability consumption, exhausted-item cleanup, and multi-boss coordinate display.
- Static report: 6 labels, input ID `7`, no `#CALL`, no timers, `S$...坐标` display variables, `D606/D024/D515`, and `P1-P18` coordinate variables.
- Official chapters to cross-check: `624-NPC对话框内默认输入框.md`, `540-检测人物是否佩带指定物品.md`, `421-改变物品的持久.md`, `217-回收指定位置装备.md`, `519-获取地图怪物坐标.md`, `628-程序变量说明.md`, `782-脚本中使用图标功能.md`.
- Lesson: an input panel is a two-step contract: render `INPUTTEXT:id`, then read `<$NPCINPUT(id)>` only from the submit label that names that ID; still validate the input server-side.
- Lesson: consumable equipped tools should be checked with `CHECKITEMW`, mutated with `ChangeItemDura` on the exact equipment position, refreshed with `UpdateItem`, and removed by `TakePosW` only after a durability guard.
- Lesson: locator pages should initialize every result string to a fallback like `未知`, then run independent `FindMonPoint` checks. Use explicit `#OR` branches for variant monster names when suffixes matter.

## 装备转移 / 装备转移.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/装备转移.txt`
- Shape: big-dialog two-slot equipment transfer with type compatibility, custom-text risk marker, currency cost, random success/failure, source destruction for fragile items, add-value transfer, element-value transfer, item-state copying, refresh, return, and close.
- Static report: 8 labels, two custom OK boxes (`ITEMBOX:4` and `ITEMBOX:5`), `N$转移几率`, `N$易碎数`, `S1/S2`, add-value scratch variables `N80-N93`, and element-value scratch variables `N60-N70`.
- Official chapters to cross-check: `186-打开NPC大对话框.md`, `397-自定义OK框.md`, `360-修改物品的附加属性值.md`, `345-调整物品新增属性.md`, `842-自定义属性说明书.md`, `628-程序变量说明.md`, `163-GOTO将传递参数返回值保存到变量-脚本参数回调.md`.
- Lesson: treat transfer as a transaction, not a single mutation command. Validate both boxes, charge once, compute random outcome, then either delete/return terminal items or perform the full read-clear-write-refresh-return sequence.
- Lesson: the source item's normal add-values and element/new-item values are separate ranges. Read both, clear both from the source, write both to the target, then explicitly copy item states/custom text if the design requires them.
- Static caution: after `GOTO @其他属性`, lines below that jump in the same `#ACT` block may be unreachable depending on engine flow. When editing similar scripts, verify whether refresh/return happens after the jumped label or must be moved before the jump.

## 存储仆从 / 存储仆从.txt

- Source: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存储仆从.txt`
- Shape: wizard-only pet storage panel with saved `T1` list, `L$` rendering into five display slots, input-based pet name submission, forbidden-name guard, pet removal, persisted writeback, and pet restoration.
- Static report: 4 labels, input ID `3`, array `L$存宝`, display variables `S$宝宝0-S$宝宝4`, skill/capacity counters `N$诱惑之光等级`, `N$诱惑数量`, `N$存宝数量`, `N$取出数量`, and saved string field `T1`.
- Official chapters to cross-check: `192-多元数组元素变量.md`, `223-获取技能信息命令.md`, `537-检测人物宝宝名字.md`, `380-在线修改宝宝名字.md`, `290-杀死人物的宝宝.md`, `390-召唤指定怪物为宝宝.md`, `787-扩展NPC脚本点击触发带参数-NPC标签带参数.md`, `624-NPC对话框内默认输入框.md`, `628-程序变量说明.md`.
- Lesson: saved scalar fields can hold serialized `L$` lists for small per-player state. On entry, copy `T1` into `L$`, count it, render slot variables, and write `MOV T1 <$STR(L$存宝)>` after every mutation.
- Lesson: pet storage needs both character constraints and runtime pet constraints: class gate, skill-derived capacity, current slave count, forbidden pet names, `CHECKSLAVENAME`, `KillCallMob`, then `RECALLMOB` with explicit level/time/color/skill parameters on restore.
- Lesson: parameterized slot labels pass both pet name and slot index. Treat `<$SCRIPTPARAM*>` as volatile label-local values if the flow may jump away.

## RobotManage / RobotManage.txt

- Source: `样本Mir200/Envir/Robot_def/RobotManage.txt`
- Shape: scheduled automation hub for daily cleanup, scrolling announcements, monster respawn maintenance, stage-gated boss events, and random invasion selection.
- Static report: 13 labels, no `#CALL`, no dialog inputs, no item boxes, variables `G0` and `I11`, and commands such as `CLEARNAMELIST`, `SENDMOVEMSG`, `CheckMapSameMonCount`, `MonGenEx`, `CheckMonMap`, `CLEARMAPMON`, `RandomKillMon`, `PARAM1-PARAM3`, and `MONGEN`.
- Official chapters to cross-check: `272-清除列表内容.md`, `193-发送屏幕滚动信息.md`, `528-检测地图相同怪物数.md`, `638-国战系统命令汇总.md`, `443-杀死地图中的怪物.md`, `628-程序变量说明.md`.
- Lesson: robot labels are scheduled environment actions. Check `Robot.txt` and `AutoRunRobot.txt` for the trigger schedule, then read the matching `[@label]` in `RobotManage.txt`; do not analyze it like a player-clicked NPC page.
- Lesson: spawn maintenance should guard against duplication by checking existing monster counts before `MonGenEx`, and stage-gated events should `BREAK` early when global progress such as `G0` is too low.
- Lesson: random event selection is implemented as ordered `#IF RANDOM n` branches with `BREAK` after each success and a final fallback branch. Changing probabilities requires reading branch order, not only the numeric literals.
