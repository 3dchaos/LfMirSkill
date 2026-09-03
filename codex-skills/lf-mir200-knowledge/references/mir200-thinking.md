# Mir200 Script Thinking

Generated from the live `样本Mir200` scripts.

## Principles

- 先找入口，再看条件，再看动作，最后确认状态回写。
- NPC 脚本常把问答、跳转、奖励和退出放在同一条线里处理。
- 任务脚本常把 UI 交互、背包检测、物品流转和反馈消息绑定在一起。
- 地图事件与自动化脚本常靠定时器、全局变量和场景条件驱动。
- MapInfo 中的 `源地图 源X,源Y -> 目标地图 目标X,目标Y` 是地图链接；玩家踩到源坐标后进入目标坐标。
- `QMission-0.txt` 这类任务页展示脚本不要用 `GOTO @标签` 做当前进度页分发；菜单用 `<文本/@标签>` 直连，进度页把 `#IF / #SAY / #ACT BREAK` 直接写在目标标签里。
- 英雄装备常驻效果要按生命周期处理：登录、穿戴、卸下、死亡、定时续期、受击、攻击都要挂回调，3 秒限时属性必须靠独立 timer 续写，不能靠一次 `ChangeHumAbility` 直接当永久值。
- `LockUpdateAbil` 在这个项目里有副作用，长持锁可能卡住英雄或月灵移动；如果必须使用，就尽量缩短到单次 `UpdateAbil` 的范围内。

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
  - `ChangeState` 是给当前脚本主体加/清人物状态的命令；先判断当前回调主体是谁，再决定是否需要 `M.`、`H.`、`FS.`、`BB.` 等前缀。被打触发里的裸 `ChangeState` 通常落在被打者自己身上。
- 自动化与定时 (47): AutoRun, OnTimer, SetOnTimer, Robot, Gmexecute, #CALL
  - LF script `#IF` starts an independent condition block; use `#ELSEACT BREAK` to stop failed prerequisites from falling through into the next `#IF` block.
  - Variable classes are distinct. `L$` is the documented array/list family: assign with brackets (`MOV L$列表 [0,1,D1002]`), count/search with `GetListVarCount` / `CheckVarInList`, and read with `<$STR(L$列表[<$STR(N$下标)>])>`. `S$` and `N$` are extended string/number variables; `A` is a documented global string family often accepted by file/text commands. Confirm the family before inventing a prefix.
  - 金币条件用 `CHECKGOLD 数量`，例如 `CHECKGOLD 20000`；失败分支写在 `#ELSEACT`。扣金币可沿用本地脚本里的 `GOLDCOUNT - 数量` 风格。不要把金币当普通背包物品用 `CHECKITEM 金币` 检查，也不要在能用 `CHECKGOLD` 的 guard 中传播临时的 `<$GOLDCOUNT>` 数值比较。
  - Random logic has three separate patterns. Use `RANDOM n` only for Mir-style `1/n` condition gates; larger `n` means lower chance. Use documented `RANDOMEX 子 母` for positive percent-style gates, for example `RANDOMEX <$STR(N$触发几率)> 100` when `N$触发几率` stores `15/25/35/45`. Use `MOVR` when a random numeric value must be stored. For an in-script candidate list, use `MOVR N$下标 0 最大下标` plus `L$数组[<$STR(N$下标)>]`; for a file-backed list, use `GetRandomText 文件路径 S/A变量`.
  - 角色级挂机保护这类付费开关用保存型私人变量（如 `U10`）承载状态，辅助面板负责开关和金币门槛，定时器只做扣费/自动关闭。若复用 `TimerEx7` 等已有毫秒级个人定时器，不要随手改原间隔；用计数器把 300ms tick 聚合成约 900ms 或其他目标频率。
  - 攻击触发中读取“被攻击目标”的角色级保护状态时，先用 `CHECKCURRTARGETRACE = 0` 确认目标是人物，再用 `C.` 当前目标语法读取，如 `EQUAL <$C.STR(U10)> 1`。全局变量只适合全服开关，不适合玩家个人保护。
  - Example: `样本Mir200/Envir/MapQuest_def/QManage.txt` (OnTimer, SetOnTimer, Gmexecute, #CALL)
  - Example: `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt` (OnTimer, SetOnTimer, Gmexecute, #CALL)
  - Example: `样本Mir200/Envir/Market_def/QFunction-0.txt` (Gmexecute, #CALL)
- 英雄装备生命周期 (new): HeroTakeOnEx, HeroTakeOffEx, HeroLogin, HeroDie, HeroStruckDamage, HeroAttackDamage, H.CHECKUSEITEM, H.GetItemFieldValue, LockUpdateAbil, UpdateAbil
  - Example: `Mir200/Envir/QuestDiary/系统功能/军鼓BUFF.txt` (hero equip/login/renewal/cleanup chain)
  - Example: `Mir200/Envir/Market_def/QFunction-0.txt` (HeroTakeOnEx, HeroTakeOffEx, HeroDie, HeroStruckDamage, HeroAttackDamage)
  - Example: `Mir200/Envir/MapQuest_def/QManage.txt` (HeroLogin + timer renewal entry)
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

- Treat the manual as syntax authority and `样本Mir200` as practical usage authority. For arrays, the strongest evidence is `knowledge_base/chapters/192-多元数组元素变量.md` plus sample scripts such as `样本Mir200/Envir/Market_def/酒馆/翔天-3.txt` and `样本Mir200/Envir/Market_def/其它区域/踏云尊者-yssd.txt`.
- For any script, write down: entry, guards, actions, state writeback, failure path.
- If a pattern appears in multiple examples, prefer the repeated local style over a one-off shortcut.

## Update Loop

1. Refresh `docs.json` and `sample.json`.
2. Rebuild this summary from the current sample scripts.
3. Rebuild `mir200-training.md` so the learning course follows current examples.
4. Read this file before answering new Mir200 questions.

Source root: `D:\wangsiProject\LF知识库搭建`
