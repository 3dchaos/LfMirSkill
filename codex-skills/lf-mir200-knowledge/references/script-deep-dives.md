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
