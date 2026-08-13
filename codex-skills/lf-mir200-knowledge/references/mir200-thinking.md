# Mir200 Script Thinking

Generated from the live `样本Mir200` scripts.

## Principles

- 先找入口，再看条件，再看动作，最后确认状态回写。
- NPC 脚本常把问答、跳转、奖励和退出放在同一条线里处理。
- 任务脚本常把 UI 交互、背包检测、物品流转和反馈消息绑定在一起。
- 地图事件与自动化脚本常靠定时器、全局变量和场景条件驱动。
- MapInfo 中的 `源地图 源X,源Y -> 目标地图 目标X,目标Y` 是地图链接；玩家踩到源坐标后进入目标坐标。
- `QMission-0.txt` 这类任务页展示脚本不要用 `GOTO @标签` 做当前进度页分发；菜单用 `<文本/@标签>` 直连，进度页把 `#IF / #SAY / #ACT BREAK` 直接写在目标标签里。

## Patterns

- 入口与分发 (315): [@main], @main, @Startup, @Help, @start
  - Example: `样本Mir200/Envir/Market_def/比奇城/书店-0104.txt` ([@main], @main, @Help)
  - Example: `样本Mir200/Envir/Market_def/比奇城/武馆教头-0.txt` ([@main], @main, @start)
  - Example: `样本Mir200/Envir/Market_def/比奇城/武馆教头-0137.txt` ([@main], @main, @start)
- 条件守门 (292): #IF, CHECK, LARGE , SMALL , EQUAL , RANDOM , COMPARETEXT, CHECKMAPNAME
  - Example: `样本Mir200/Envir/Market_def/QFunction-0.txt` (#IF, CHECK, EQUAL , RANDOM , COMPARETEXT, CHECKMAPNAME)
  - Example: `样本Mir200/Envir/Market_def/其它区域/踏云尊者-yssd.txt` (#IF, CHECK, LARGE , SMALL , EQUAL , RANDOM )
  - Example: `样本Mir200/Envir/Market_def/盟重城/药店-0160.txt` (#IF, CHECK, LARGE , SMALL , EQUAL , RANDOM )
- 动作执行 (284): #ACT, GIVE , TAKE , GAMEGOLD, GAMEGIRD, MAPMOVE, MonGen, GOTO, BREAK
  - Example: `样本Mir200/Envir/Market_def/白日门/季正-D10061.txt` (#ACT, GIVE , TAKE , MAPMOVE, MonGen, GOTO)
  - Example: `样本Mir200/Envir/Market_def/其它区域/石墓_合成师-R001.txt` (#ACT, GIVE , TAKE , MonGen, GOTO, BREAK)
  - Example: `样本Mir200/Envir/Market_def/盟重城/雪域世界-3.txt` (#ACT, TAKE , GAMEGOLD, MAPMOVE, MonGen, GOTO)
- UI与交互 (277): #SAY, MESSAGEBOX, OPENMERCHANTBIGDLG, ITEMBOX, Text:, Img:, Layout:
  - Example: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt` (#SAY, MESSAGEBOX, OPENMERCHANTBIGDLG, ITEMBOX, Text:, Img:)
  - Example: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/邮箱.txt` (#SAY, MESSAGEBOX, OPENMERCHANTBIGDLG, ITEMBOX, Text:, Img:)
  - Example: `样本Mir200/Envir/Market_def/盟重城/药店-0160.txt` (#SAY, MESSAGEBOX, Text:, Img:, Layout:, MText:)
- 状态回写 (136): SET [, MOV , SetOnTimer, DelTextListLine, AddTextListEx, ReturnBoxItem, UpdateItem, SetCustomItemText
  - Example: `样本Mir200/Envir/MapQuest_def/QManage.txt` (SET [, MOV , SetOnTimer, DelTextListLine, AddTextListEx)
  - Example: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt` (SET [, MOV , SetOnTimer, ReturnBoxItem, UpdateItem)
  - Example: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/邮箱.txt` (MOV , DelTextListLine, AddTextListEx, UpdateItem, SetCustomItemText)
- 自动化与定时 (47): AutoRun, OnTimer, SetOnTimer, Robot, Gmexecute, #CALL
  - Example: `样本Mir200/Envir/MapQuest_def/QManage.txt` (OnTimer, SetOnTimer, Gmexecute, #CALL)
  - Example: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt` (OnTimer, SetOnTimer, Gmexecute, #CALL)
  - Example: `样本Mir200/Envir/Market_def/QFunction-0.txt` (Gmexecute, #CALL)
- 地图链接 (58): ->, MAPMOVE
  - Example: `样本Mir200/Envir/Market_def/其它区域/神秘老人-Q011.txt` (->, MAPMOVE)
  - Example: `样本Mir200/Envir/MapInfo.txt` (->)
  - Example: `样本Mir200/Envir/Npc_def/公告牌-GM001.txt` (MAPMOVE)

## Dominant Categories

- Market_def: 308
- QuestDiary: 46
- Npc_def: 7
- Robot_def: 2
- MapInfo.txt: 1
- MapQuest_def: 1
- Robot.txt: 1

## Reading Discipline

- Treat the manual as syntax authority and `样本Mir200` as practical usage authority.
- For any script, write down: entry, guards, actions, state writeback, failure path.
- If a pattern appears in multiple examples, prefer the repeated local style over a one-off shortcut.

## Update Loop

1. Refresh `docs.json` and `sample.json`.
2. Rebuild this summary from the current sample scripts.
3. Rebuild `mir200-training.md` so the learning course follows current examples.
4. Read this file before answering new Mir200 questions.

Source root: `D:\wangsiProject\LF知识库搭建`
