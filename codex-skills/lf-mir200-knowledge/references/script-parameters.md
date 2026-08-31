# Mir200 Script Parameter Passing

This note records reusable lessons from the LF manual and the local `样本Mir200` scripts about labels written like `@标签(参数)`.

## Official Facts

- `knowledge_base/chapters/787-扩展NPC脚本点击触发带参数-NPC标签带参数.md` documents NPC/dialog links such as `<麻痹戒指/@购物(20,麻痹戒指)>`. The target label reads values through `<$SCRIPTPARAM1>`, `<$SCRIPTPARAM2>`, and so on.
- The same chapter documents `CHECKSCRIPTPARAM` as a whitelist guard. Use it to reject forged or unexpected parameter combinations before charging currency, taking items, giving rewards, changing jobs, teleporting, or mutating stored state.
- The manual warns that script parameters only live in the current dialog label. Once the flow jumps to another label, including `GOTO @xxx`, parameters can be cleared. Copy needed values into normal variables before any possible jump or callback.
- `knowledge_base/chapters/163-GOTO将传递参数返回值保存到变量-脚本参数回调.md` documents `GOTO @标签(参数1,参数2|返回变量1,返回变量2)` plus `RETURN 值1 值2`. `RETURN` also ends the current script segment.
- `knowledge_base/chapters/808-添加对话框-可用于主界面任务引导.md` documents that `AddDlg` content can use parameterized button links such as `<按钮点击/@1(22,33,44)>`, and the QFunction callback label can read those values with `<$scriptparam1>`, etc.
- `knowledge_base/chapters/782-脚本中使用图标功能.md` documents that clickable `Img`/`ImgEx`/`PlayImg` style UI elements trigger labels, and their input-list parameter is for submitting `<$NPCINPUT(id)>`. When combining UI clicks and parameters, trace both the clicked label and any submitted input IDs.

## Sample Evidence

- `样本Mir200/Envir/Market_def/其它区域/皓月熔炉-FOX03.txt:260` uses one generic forge label. Many UI links pass `(物品名,消耗数量)`, then `[@皓月]` checks `皓月晶石 <$SCRIPTPARAM2>`, takes that cost, gives `<$SCRIPTPARAM1>`, and reports the crafted item.
- `样本Mir200/Envir/Market_def/其它区域/王马夫-FOX02.txt:82` and `:101` use two generic upgrade labels. The five parameters mean source item, target item, currency cost, source count, and material count. The sample uses these values directly in `CHECKITEM`, `TAKE`, `GAMEGIRD -`, `GIVE`, and player messages.
- `样本Mir200/Envir/Market_def/云隐宗师.txt:65` uses `@重生(0/1/2)` to choose target class. The label immediately converts the numeric parameter into `S$转职`, then later performs destructive actions such as `CHANGEJOB`, `RENEWLEVEL`, `CLEARSKILL`, and storage deletion. This is the safer shape: normalize branch choice to a variable before the complex flow.
- `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/辅助.txt:159` uses `@召唤配置(宝宝名,数量)` for four similar setting rows. Each branch validates the first parameter with `EQUAL <$SCRIPTPARAM1> 名称` plus `CHECKMAGICNAME`, then writes only the second parameter into the corresponding saved setting variable.
- `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存仓.txt:1` uses `@自动存仓(页码)` for paging. It copies the page parameter into `N$选择内容`, uses that to calculate display offsets, and later calls `GOTO @自动存仓(<$str(n$选择内容)>)` after list mutation to redraw the same page.
- `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存仓.txt:92` uses `@点击(物品标识)` from `itemshow` rows. The label toggles that value in `L$存仓数组`, then persists the list back to the per-player text file.
- `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/回收目录.txt:1` uses `@回收目录1(目录名)` for category selection. It treats a missing parameter as the default category, otherwise copies `<$SCRIPTPARAM1>` into `S$选择内容` and loads the matching category file.
- `样本Mir200/Envir/QuestDiary/系统功能/老登辅助/存储仆从.txt:36` passes `(宝宝名,槽位)` into the slot label. The first parameter decides whether the slot is empty or holds a pet; the restore label later uses the pet-name parameter in `RECALLMOB` and removes it from `L$存宝`.
- `样本Mir200/Envir/MapQuest_def/QManage.txt:326` uses `Gmexecute 开始提问 @归队(<$USERNAME>)`; `[@归队]` reads `<$SCRIPTPARAM1>` and compares it with saved teammate name fields before `CreatGroup`. This shows parameters are also used outside ordinary merchant menu links when the command triggers a label with arguments.
- A static scan found no active `CHECKSCRIPTPARAM` in `样本Mir200`. That makes the sample useful for idioms, but the official whitelist recommendation should be added when writing new sensitive flows.

## Practical Patterns

Use parameterized labels when one handler differs only by a small data tuple:

```mir200
<铸造皓月战刃/@皓月(皓月战刃,50)>

[@皓月]
#OR
CHECKSCRIPTPARAM 皓月战刃,50
CHECKSCRIPTPARAM 皓月权杖,50
#ELSEACT
SENDMSG 6 非法的参数
BREAK

#IF
CHECKITEM 皓月晶石 <$SCRIPTPARAM2>
#ACT
TAKE 皓月晶石 <$SCRIPTPARAM2>
GIVE <$SCRIPTPARAM1> 1
BREAK
#ELSEACT
MESSAGEBOX 皓月晶石不够。
BREAK
```

Normalize parameters before branching into longer work:

```mir200
[@重生]
#IF
EQUAL <$SCRIPTPARAM1> 0
#ACT
MOV S$转职 warrior

#IF
EQUAL <$SCRIPTPARAM1> 1
#ACT
MOV S$转职 Wizard

#IF
EQUAL <$SCRIPTPARAM1> 2
#ACT
MOV S$转职 Taoist

#IF
EQUAL <$STR(S$转职)>
#ACT
SENDMSG 6 非法的参数
BREAK
```

Use `GOTO ... | ...` when the target label should behave like a small same-file function with return values:

```mir200
[@run]
#ACT
GOTO @计算(1,2|N$返回1,S$返回2)
SENDMSG 7 <$STR(N$返回1)>,<$STR(S$返回2)>

[@计算]
#ACT
FORMULATION <$SCRIPTPARAM1>*2 N$结果
MOV S$文本 参数2=<$SCRIPTPARAM2>
RETURN <$STR(N$结果)> <$STR(S$文本)>
```

## Guardrails

- Treat parameters as untrusted input, even when the only visible entry is a button. The manual explicitly frames `CHECKSCRIPTPARAM` as protection against forged data.
- Do not read `<$SCRIPTPARAM*>` after a label jump unless the current label was itself entered with parameters. Copy to `S$`/`N$`/`L$` first if the value must survive `GOTO`, callback-style commands, or another interaction.
- Match parameter arity and meaning consistently. If `@升级马` uses five values, keep every link in that order: source item, target item, currency cost, source count, material count.
- Use numeric variables for math and comparisons (`N$选择内容`, `N$费用`) and string variables for names/paths (`S$选择内容`, `S$转职`). Cross-check variable lifetime with `628-程序变量说明.md`.
- Do not let parameters become raw file-path authority without whitelisting. Category patterns such as `回收目录1(垃圾装备)` should restrict the accepted category names before using the value to build a file path.
- If a parameter value is a list or serialized array, prefer `L$` and pass `<$STR(L$变量)>` only as a short hop. `192-多元数组元素变量.md` shows arrays can be passed into a parameter, but the receiving label should still copy or parse them before complex flow.
- For `#CALL`/`#CALLEX`, the confirmed manual chapter only documents selecting the target file/label, not direct `#CALL [file] @label(args)` parameter passing. If cross-file logic needs arguments, store them in scoped variables before the call, or keep the parameterized hop in a confirmed `GOTO`/dialog-trigger path.
- Keep sample quirks out of new code. For example, `样本Mir200/Envir/Market_def/其它区域/王马夫-FOX02.txt:71` appears to have an incomplete parameter list in one UI link; do not copy that line as syntax proof.

