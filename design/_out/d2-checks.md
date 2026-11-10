# 摘要：脚本检测命令（98 章）


### or检测命令
CHECKLEVEL 85
SendMsg 5 检测通过

### 行会成员人数
功能:
格式:
CheckGuildMemberCount 控制符
CheckGuildMemberCount  >

### 获取NPC坐标
**功能：**
FindNpcPoint 地图名 NPC名称 X坐标变量 Y坐标变量
**说明：**
FindNpcPoint 3 盟重老兵 N1 N2
SendMsg 6 盟重省中npc盟重老兵的坐标为<$STR(N1)>,<$STR(N2)>

### 获取当前镖车名称和坐标
功能说明:
说明：获取当前镖车名称和坐标（仅限押镖期间）
示例脚本：
CHECKLEVELEX > 0

### 获取地图怪物坐标
**功能：**
FindMonPoint 地图名 怪物名称 X坐标变量 Y坐标变量
**说明：**
FindMonPoint 3 采集怪 N1 N2
SendMsg 6 最近的盟重采集怪坐标为<$STR(N1)>,<$STR(N2)>

### 获取行会人数脚本命令
功能:
格式:
GETGUILDMEMBERCOUNT  参数1  参数2  参数3
参数1:行会名称
参数2:保存变量 行会不存在返回0
参数3:0或空为行会总人数，1为行会当前在线成员人数
GETGUILDMEMBERCOUNT <$guildname> N$人数

### 获取自定义怪物攻击类型
功能说明:
说明：被自定义怪物攻击时，获取自定义怪物攻击类型
示例脚本：
CHECKCURRTARGETRACE = 156
CHECKCURRTARGETRACE = 156
CHECKCURRTARGETRACE = 156
CHECKCURRTARGETRACE = 156
CHECKCURRTARGETRACE = 156
CHECKCURRTARGETRACE = 156
EQUAL <$CURRRTARGETFULLNAME> MON120
EQUAL <$CURRRUSEMAGICID> 0
SENDMSG 6 MON120对你施展了普通攻击
EQUAL <$CURRRTARGETFULLNAME> MON120
EQUAL <$CURRRUSEMAGICID> 1
SENDMSG 7 MON120对你施展了攻击1
EQUAL <$CURRRTARGETFULLNAME> MON120
EQUAL <$CURRRUSEMAGICID> 2
SENDMSG 7 MON120对你施展了攻击2
EQUAL <$CURRRTARGETFULLNAME> MON120
EQUAL  …[截断]

### 检测包裹中满经验聚灵珠数量
功能说明:
说明：给予一个满经验聚灵珠、检测包裹中满经验聚灵珠数量
命令格式：GIVE 物品名 数量 参数3 参数4 参数5 参数6 参数7 参数8 参数9
参数3-8对应物品位置的0-5极品属性（其他位置无效）。参考下面的极品属性
参数9: 物品持久值(0或空保持当前，视物品而定; -1:给满持久)；\*\*\*\*\*\*\*注意：参数9仅对非叠加物品有效
参数3： 是否判断满持久(0:不判断； 1：判断）\*\*\*\*\*\*\*注意：参数3仅对非叠加物品有效
格式: GetBagItemCount 物品名称 保存变量 排除OK框中的物品(0或空:计算OK框的物品，1：不算OK框中的物品) 是否判断满持久(0:或空不判断； 1：判断）
GetBagItemCount 聚灵珠 N1 0 1
SENDMSG 6 你的背包中共有<$STR(N1)>个满经验的聚灵珠
格式：take 物品 数量 是否检测装备改名（0或空：不检测，1：检测） 物品名匹配方式(0或空：完整匹配，1：部分匹配） 是否回收自定义OK框物品(0或空:回收; 1:不回收) 检测持久（0或空：不检测 ，-1检测为满持 …[截断]

### 检测背包是否包含文件中的物品
**功能：**
CheckBagItems 文件名 物品名变量 数量变量
CacheCheckBagItems 文件名 物品名变量 数量变量
**说明：**
CheckBagItems d:\a.txt S1 N1
SendMsg 6 检测到背包中有d:\a.txt的物品，物品名为<$STR(S1)>，数量为<$STR(N1)>
SendMsg 6 未检测到背包中有d:\a.txt的物品
CheckBagItems ..\QuestDiary\回收系统\赤月装备.txt S1 N1
SendMsg 6 检测到背包中有赤月装备物品，物品名为<$STR(S1)>，数量为<$STR(N1)>
SendMsg 6 未检测到背包中有赤月装备物品

### 检测背包是否有指定物品[!]
功能: 检测背包是否有指定物品
格式:checkitem 名字 数量 参数3（空或0，名称完全匹配。 不等于0部分匹配）参数4(是否检测改名的装备0：否; 1: 是）
CheckItem 麻痹 1 1
SendMsg 5 你背包有包含麻痹文字的装备
CheckItem 麻痹戒指 1
SendMsg 5 你背包有麻痹戒指
格式:checkitems 参数1名字 参数2数量 参数3检测身上相同（包含检查装备，首饰，神佑）装备总量
SENDMSG 5 你身上有2个传送戒指....

### 检测被自己杀死宝宝的名字
注意:此命令只检测直属宝宝,例如道士英雄召唤的神兽不属于直属宝宝.

### 检测当前目标类型
格式: CHECKCURRTARGETRACE 控制符(=,>,<) 数据库Race值
CHECKCURRTARGETRACE = 0
CHECKCURRTARGETRACE = 1
CHECKCURRTARGETRACE = 150
CHECKCURRTARGETRACE = 151

### 检测地图范围怪物数量
格式: CHECKRANGEMONCOUNTEX 地图代码 怪物名 X坐标 Y坐标 范围 控制符(=,>,<) 数量 宝宝是否计算在内
CHECKRANGEMONCOUNTEX 3 半兽人 333 333 10 > 100
CheckRangeMonCountEx <$MAP> 半兽人 51 43 0 > 0 1

### 检测地图相同怪物数
格式: CheckMapSameMonCount 地图名称 怪物名称 控制符(<,>,=) 数量 是否忽略怪物名称后面的数字(留空或0=检测数字,1=不检测数字)
CheckMapSameMonCount 3 稻草人 > 10
CheckMapSameMonCount 3 圣兽A > 2

### 检测地图坐标是否可以到达
功能：
格式：
CHECKMAPMOVE 地图名 X坐标 Y坐标
CHECKMAPMOVE 3 333 333

### 检测对象状态
功能说明:
说明：CheckStateValue 状态值
示例脚本：
CheckStateValue 1

### 检测行会可以容纳多少成员
格式: CHECKGUILDMEMBERMAXLIMITCOUNT 行会名称(SELF表示检测自己所在的行会) 检测符(<,>,=) 数量
CHECKGUILDMEMBERMAXLIMITCOUNT > 100

### 检测会员剩余时间
格式: 检测会员剩余时间 文件名称 过期是否删除(0不删除 1删除) 变量1(到期时间 字符变量) 变量2(剩余天数 数字变量) 变量3(剩余小时 数字变量) 变量4(剩余分钟 数字变量)
CHECKNAMEDATETIMELIST ..\QuestDiary\会员名单.txt 1 <$STR(S1)> <$STR(N1)> <$STR(N2)><$STR(N3)>
SENDMSG 6 你的会员到期时间是<$STR(S1)>【剩余天数=<$STR(N1)>】【剩余小时=<$STR(N2)>】【剩余分钟=<$STR(N3)>】 255 253
SENDMSG 6 你不是会员或已过期，请及时充值！ 255 253
ClearNameList 文件名 是否绝对路径（0或空：相对路径；1：绝对路径）
AddNameDateList 文件名 是否绝对路径（0或空：相对路径；1：绝对路径）
DelNameDateList 文件名 是否绝对路径（0或空：相对路径；1：绝对路径）

### 检测技能修炼点数
**功能：**
**格式：**
CHECKTRANPOINT 技能名称 控制符(=,>,<)
CHECKTRANPOINT 刺杀剑术   >
H.CHECKTRANPOINT 刺杀剑术   >

### 检测魔法盾是否启用
功能:
格式:
参数1(0:武力盾;1:魔法盾;2:道力盾)
CheckShieldStateOpen 0
CheckShieldStateOpen 1
CheckShieldStateOpen 2

### 检测骑马状态
功能:
格式:

### 检测人物PK值
**功能：**
**格式：**
CHECKPKPOINTEX 控制符(=,>,<)
CHECKPKPOINTEX  >

### 检测人物宝宝名字[!]
功能：
格式：
CHECKSLAVENAME 翎风引擎
SENDMSG 5 提示:你的宝宝叫翎风引擎
SENDMSG 5 提示:你的宝宝不叫翎风引擎

### 检测人物荣誉
格式: CHECKGAMEGLORY (<,>,=) 值
CHECKGAMEGLORY = 100

### 检测人物是否挂机
功能:检测人物是否是离线挂机
格式:CheckOffline

### 检测人物是否佩带指定物品
**功能:** 检测当前人物是否佩带指定物品
**格式:**
CHECKITEMW  物品名 数量 是否装备名部分匹配（空或0，完全匹配。 不等于0部分匹配）
CHECKITEMW  力量戒指 1
CHECKITEMW 力量 1 1
COMPARETEXT <$DRESS> 布衣(男)

### 检测人物新增属性
格式: CHECKNEWITEMVALUE 位置(-1时是OK框中的装备, 0-18时是穿在身上的装备,boxitem0 - boxitem7 对应8个自定义OK框) 属性(0-10) 检测符(>,<,=) 值(1-100)
CHECKNEWITEMVALUE 0 0 > 10
GETNEWITEMVALUE 0 0 <$STR(M10)>
CheckNewItemValue -1 0 > 10 检查升级框装备暴击几率增加 > 10
CheckNewItemValue 0 0 > 10 检查衣服暴击几率增加 > 10
CheckNewItemValue boxitem0 0 > 10 检查OK框0暴击几率增加 > 10

### 检测人物幸运值
**功能：**
**格式：**
CheckLuckPoint 控制符(=,>,<)
CheckLuckPoint   >
**格式：**
CheckLuckPointy 控制符(=,>,<)
CheckLuckPointy   >

### 检测人物在线时长[!]
功能：
格式：
ONLINELONGMIN (> < =) 支持变量操作
ONLINELONGMIN > 10

### 检测杀人者是人物还是怪物
**功能：**
**格式：**
CHECKCURRTARGETRACE = 0
SENDMSG 6 你被人物【<$CURRRTARGETNAME>】杀死了 255 249
CHECKCURRTARGETRACE = 1
SENDMSG 6 你被英雄【<$CURRRTARGETNAME>】杀死了 255 249
CHECKCURRTARGETRACE = 151
SENDMSG 6 你被分身【<$CURRRTARGETNAME>】杀死了 255 249
CHECKCURRTARGETRACE = 10
CHECKCURRTARGETRACE = 15
SENDMSG 6 被NPC命令杀死了
SENDMSG 6 你被怪物【<$CURRRTARGETNAME>】杀死了 255 249
KillByHum 检测人物杀死为显示人物，宝宝杀死则为怪物（非人物）
CheckKillByHum 检测为凶手为人物包含人物的任意下属 （含宝宝，英雄和英雄宝宝均检测为人物）
SendMsg 5 玩家 <$KILLER> 在%m 把你干死了!
SendMsg 5 怪物 <$KILLER> 在%m 把你干死了!

### 检测是不是在摆摊
格式: CHECKSHOPSTALLSTATUS

### 检测是否进入攻城的范围
格式: CHECKCASTLEWARAREA 城堡名称
CHECKCASTLEWARAREA 沙巴克

### 检测是否正在攻城
格式: CHECKUNDERWAR 城堡名称
CHECKUNDERWAR 沙巴克

### 检测玩家是否在线
**功能：**
**格式：**    CheckOnline

### 检测物品的附加属性值
格式: 格式: CHECKITEMADDVALUE 装备位置(-1时是升级OK框中的装备, boxitem0 -boxitem7为自定义OK框，0-51时是穿在身上的装备) 属性位置(0-18) (符号 < > =) 值 保存变量
CheckItemAddValue 0 0 > 1
GETITEMADDVALUE 0 0 <$STR(M10)>

### 检测在安全区


### 检测指定范围内的人物数量
CheckRangeHumCount 地图名称 X Y 范围 (<,>,=) 数量

### 检测装备名字颜色
功能:
格式: CheckItemNameColor 位置(0-13)
CheckItemNameColor 1

### 检测装备星星数量
功能:
格式:
CheckUpgradeCount 物品位置 (<,>,=) 星星数量
H.CheckUpgradeCount 物品位置 (<,>,=) 星星数量
示例：
CheckUpgradeCount 5 > 1

### 检测组队人数[!]
功能：
格式：
CHECKGROUPMEMBERCOUNT (<,>,=) 数量
CHECKGROUPMEMBERCOUNT > 10

### 检查宝宝数量
**功能：**
**格式：**CHECKSLAVECOUNT  控制符
CHECKBBCOUNT 控制符
CHECKSLAVECOUNT =
CHECKSLAVECOUNT >
CHECKSLAVECOUNT <
格式：
CHECKSLAVECOUNT 控制符 <.=.> 数量
CHECKSLAVECOUNT 控制符 <.=.> 数量 宝宝名字 是否检查名称数字(0:不检查名称数字[骷髅1,骷髅2都按包骷髅算], 1:算数字)

### 检查宝宝最高等级
命令格式:
CHECKSLAVELEVEL 控制符(=,>,<)  等级数(7)
CHECKSLAVELEVEL =
CHECKSLAVELEVEL >
CHECKSLAVELEVEL <

### 检查城堡占领天数
**功能：**    检查沙巴克占领天数
**格式：

### 检查城堡战争天数
**功能：**
**格式：**    CASTLEWARAY

### 检查城门状态
**功能：**
**格式：**;==========================================
CHECKCASTLEDOOR 损坏
CHECKCASTLEDOOR 开启

### 检查当前所在地图的名字
**功能：**
**格式：**CHECKMAPNAME 地图名称
CHECKMAPNAME 3

### 检查登录帐号与IP是否匹配
**功能：**
**格式：**CHECKACCOUNTIPLIST
**列表文件格式:**此文件们于目录：Mir200\Envir\

### 检查地图怪物数量
**功能：**
**格式：**CheckMonMap 地图号

### 检查地图怪物数量
**功能：**
**格式：**CheckMapMonCount 地图号 检测符号
**格式：**CheckMapMonCount 地图号 检测符号<、 =、 >

### 检查对面人物的等级
**功能：**
**格式：**CHECKPOSELEVEL 控制符(=,>,<)  等级数(1 -
CHECKPOSELEVEL =
CHECKPOSELEVEL >
CHECKPOSELEVEL <

### 检查对面人物的性别
**功能：**
**格式：**CHECKPOSEGENDER

### 检查对面人物站的位置
**功能：**
**格式：**CHECKPOSEDIR

### 检查行会名称
**功能：**    检查行会名称
**格式：

### 检查行会是否在列表中
**功能：**
**格式：

### 检查会员时间
相关命令：
DELUSERDATE  会员.txt

### 检查金刚石数量
**功能：**
**格式：**    CHECKGAMEDIAMOND  控制符(<、>、 =)
GAMEDIAMOND (+,-,=) 值
**功能：**    检查灵符数量。
**格式：**    CHECKGAMEGIRD  控制符(<、>、 =)  点数
GAMEGIRD (+,-,=) 值
CHECKGAMEGIRD >
**功能：**    检查荣誉数量。
**格式：**   CHECKGAMEGLORY  控制符(<、>、 =)  点数
GAMEGLORY (+,-,=) 值
CHECKGAMEGLORY >

### 检查人物HP值
**功能：**用来检查人物HP值的上限及下限值
**命令格式：**    CHECKHP 控制符(<、>、 =) 攻击下限
CHECKHP > 30 >

### 检查人物MP值
**功能：**用来检查人物MP值的上限及下限值
**命令格式：**    CHECKMP 控制符(<、>、 =) 攻击下限
CHECKMP > 30 >

### 检查人物背包空格数
**功能：**
CheckBagSize 数量
CHECKBAGSIZE  5

### 检查人物当前经验值
**功能：**
**格式：**
CHECKEXP =
CHECKEXP >
CHECKEXP <

### 检查人物道术
**功能：** 用来检查人物道术的上限及下限值
**命令格式：**    CHECKSC 控制符(<、>、 =) 攻击下限
CHECKSC > 30 >

### 检查人物的会员等级
**功能：**
**格式：**CHECKMEMBERLEVEL 类型(1-65535)
CHECKMEMBERLEVEL 2 =
CHECKMEMBERLEVEL 2 >
CHECKMEMBERLEVEL 2 <

### 检查人物的会员类型
**功能：**
**格式：**CHECKMEMBERTYPE
CHECKMEMBERTYPE =
CHECKMEMBERTYPE >
CHECKMEMBERTYPE <

### 检查人物的游戏点数
**功能：**
**格式：**    CHECKGAMEPOINT  控制符(<、>、 =)
CHECKGAMEPOINT >
**功能：**    检查当前人物身上有多少游戏币。
**格式：**    CHECKGAMEGOLD  控制符(<、>、 =)  点数
CHECKGAMEGOLD >

### 检查人物的游戏点数
**功能：**
**格式：**    CHECKGAMEPOINT  控制符(<、>、 =)
CHECKGAMEPOINT >
**功能：**    检查当前人物身上有多少游戏币。
**格式：**    CHECKGAMEGOLD  控制符(<、>、 =)  点数
CHECKGAMEGOLD >

### 检查人物的转生等级
**功能：**    检查人物的转生等级
**命令格式:**    CHECKRENEWLEVEL
CHECKRENEWLEVEL =
CHECKRENEWLEVEL >
CHECKRENEWLEVEL <

### 检查人物登录IP
**功能：**
**格式：**

### 检查人物登录帐号
**功能：**
**格式：**

### 检查人物等级（改进）
**功能：**
**格式：**CHECKLEVELEX 控制符(=,>,<)  等级数(1 -
CHECKLEVELEX =
CHECKLEVELEX >
CHECKLEVELEX <

### 检查人物附加属性点数
功能：
格式：
CHECKBONUSPOINT 控制符(=,>,<)  点数
相关命令：

### 检查人物攻击力
**功能：**用来检查人物攻击力的上限及下限值
**命令格式：**    CHECKDC 控制符(<、>、 =) 攻击下限
CHECKDC > 30 >

### 检查人物技能(扩展)
功能：
格式：
CHECKSKILL 技能名称 检测符(>,<,=) 等级 是否检测强化技能(0或为空时为技能等级,1为强化技能等级)
CHECKSKILL 冰咆哮 = 0 1
SKILLLEVEL 冰咆哮 = 1 1
SENDMSG 6 冰咆哮已修炼到强化一重
相关命令：

### 检查人物名称是否与IP匹配
**功能：**
**格式：**CHECKNAMEIPLIST NameIPList.txt
**列表文件格式:**此文件们于目录：Mir200\Envir\

### 检查人物魔法力
**功能：**用来检查人物魔法力的上限及下限值
**命令格式：**    CHECKMC 控制符(<、>、 =) 攻击下限
CHECKMC > 30 > 40

### 检查人物身上指定位置是否戴物品
**功能：**

### 检查人物身上装备类型
**功能：**用来检查人物身上戴物品类型，因为不同类型物品的附加属性值位置不一样，在升级装备物品性时用来控制指定属性值。
**命令格式：**    CHECKITEMTYPE 物品位置

### 检查人物声望点
**功能：**
**命令格式:**
CHECKCREDITPOINT 控制符(=,>,<)  声望点数(1 - 255)<
CHECKCREDITPOINT =
CHECKCREDITPOINT >
CHECKCREDITPOINT <

### 检查人物是否付费
CHECKPAYMENT 2

### 检查人物是否加入行会
**功能：**
**格式：

### 检查人物是否为管理员
**功能：**
**格式：**;==========================================

### 检查人物是否为行会掌门人
**功能：**
**格式：

### 检查人物是否为沙城成员
**功能：**
**格式：

### 检查人物是否为沙城城主
**功能：**
**格式：

### 检查人物是否为新人
**功能：**
**格式：

### 检查人物是否在攻城区域[!]
功能: 检查人物是否在攻城区域
格式:

### 检查人物在列表中的位置
**功能：**
**格式：**
CHECKNAMELISTPOSITION List.txt  (> < =

### 检查是否为组长
功能：
格式：
相关命令：

### 检查是否在某地图
ISONMAP 地图名称

### 检查一个地图内人数
**功能：**
**格式：**CheckMapHumanCount 地图号  ('<' '>'

### 检查一个范围内怪物数
**功能：**
**格式：**CheckRangeMonCount 地图号 X坐标 Y坐标 范围 控制符(=,>,<)
CheckRangeMonCount 3 330 330 10 <

### 检查字符串是否在指定文件中[!]
CHECKTEXTLIST ..\QuestDiary\充值系统\10元卡号.txt <$STR(S2)>
CHECKTEXTLIST ..\QuestDiary\充值系统\10元卡号.txt <$STR(S2)> <$STR(S3)>
CHECKTEXTLIST ..\QuestDiary\列表.txt <$SERVERNAME>
CHECKTEXTLIST ..\QuestDiary\列表.txt <$USERNAME>
MOV S1 Da11
CHECKTEXTLIST ..\QuestDiary\列表.txt <$STR(S1)>
MOV S1 T001
CHECKTEXTLIST ..\QuestDiary\列表.txt <$STR(S1)>
MOV S1 D001
CHECKTEXTLIST ..\QuestDiary\列表.txt <$STR(S1)>
CHECKTEXTLIST ..\QuestDiary\列表.txt T001
MOV S1 A001
CHECKTEXTLIST ..\QuestDiary\列表.txt A001
CHECKTEXTLIST ..\Qu …[截断]

### 脚本检测命令取反NOT[!]
格式:NOT 命令 > 50 //检测人物物品算不大于50
NOT CHECKGAMEGOLD > 50 //检测人物元宝算不大于50
SENDMSG 5 你身上没有50元宝
NOT CHECKLEVELEX > 80 //检测人物等级不大于80级
SENDMSG 5 你的等级不足80级
NOT EQUAL P0 5 //检测变量P0是否不等于5
SENDMSG 5 <$STR(P0)>变量不等于5
NOT H.CHECKLEVELEX > 80 //检测英雄等级不大于80级
SENDMSG 5 你的英雄等级不足80级

### 脚本性能原子钟，检测脚本运行时间
参数1如下：
示例：
PrintUseTime 1
PrintUseTime 2 N0 S0
Sendmsg 6 提示:脚本执行耗时<$STR(N0)>微秒，自动单位为<$STR(S0)>
PrintUseTime 1
MOV N0 0
MOV N1 1
WHILE N1 < 10000
INC N0 N1
INC N1 1
PrintUseTime 2 N2 S2
Sendmsg 6 提示:脚本执行耗时<$STR(N2)>微秒，自动单位为<$STR(S2)>

### 扩展check支持批量检测个人标识
格式：check [1,2,4-6,8] 1
SENDMSG 6 1,2,4,5,6,8全为1
格式：
SET [1,2,4-6,8] 1
SET [1,2,4-6,<$STR(N$变量)>] 1

### 判断对面对象的类型
功能说明:
说明：CheckPoseActor 参数1(0:人物;1:英雄;2:分身;3:怪物(含宝宝/宠物))
示例脚本：
CheckPoseActor 0

### 战斗状态禁止退出
**功能：战斗状态禁止退出：**
SENDMSG 6 处于战斗状态
SENDMSG 6 非战斗状态

### 字符串比较处理
功能：
格式：
CheckContainsText 字符 字符串检查 //检查字符串是否包涵在另外一个字符串中.
CompareText 字符 字符 // 比较两个字符串是否一样
CheckContainsText www.lfm2.com lfm2.com
CompareText www.lfm2.com www.lfm2.com

### 坐标范围检测
CheckInMapRange 3 354 337 0
SetOffTimer 12
CheckInMapRange 3 354 337 0
CHANGEEXP + 200000