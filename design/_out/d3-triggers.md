# 摘要：特殊触发功能（60 章）


### GOTOLABEL触发[!]
GOTOLABEL 模式(0,1,2,3) 触发字段 范围(模式等于3时有效)
GOTOLABEL 0 @小组成员触发
GOTOLABEL 1 @行会成员触发
GOTOLABEL 2 @当前地图的人物触发
GOTOLABEL 3 @指定范围人物触发 12
GOTOLABEL 0 @触发字段 5 (最后的数字5表示 以自己坐标为中心指定范围人物触发)
GOTOLABEL 4 @触发字段 5 (最后的数字5表示 以自己坐标为中心指定范围人物触发)
GOTOLABEL 9 @指定范围同一国家人物触发 5 (最后的数字5表示 以自己坐标为中心指定范围人物触发，范围小于1 则表示全地图触发给自己同国家角色)
GOTOLABEL 8 @触发字段 X Y 范围 是否包含自己(0包含/1不包含) 传递的变量(允许为空) 接受的变量(允许为空)
GOTOLABEL 8 @触发字段 <$STR(N1)> <$STR(N2)> 5 1 S1 S2
SENDMSG 6 传递的变量和接受的变量是同一个，对方名称<$STR(S2)>

### 丢弃背包物品前触发
**功能：**
SENDMSG 5 中止丢弃背包内物品【<$CurItemName>(<$G\_CurItemName>)】物品序列号:<$CurItemMakeIndex>
SENDMSG 5 中止丢弃英雄背包内物品【<$H.CurItemName>(<$H.G\_CurItemName>)】物品序列号:<$H.CurItemMakeIndex>

### 摆摊物品购买前触发
**功能：**摆摊物品购买前触发 和 中止购买
CHECKLEVELEX < 50

### 武器被诅咒前触发
**功能：**武器被诅咒前触发使用命令中止诅咒
**格式：**人物触发：@BeginWeaponCurse ，英雄触发@HeroBeginWeaponCurse
**说明：**中止命令StopWeaponCurse

### 人物身上物品掉落触发
功能说明：人物身上掉落触发（人物）-------列表信息二 物品规则 仅对勾选启用的物品生效
GetUserItemName -1 1 1
CompareText S1 偃月
ChangeItemNameColor -1 253
SENDMSG 5 【<$CurUserName>】掉落物品【<$CurItemName>】，位置：<$maptitle> <$ScatterItemX>:<$ScatterItemY>
SENDMSG 0 【<$CurUserName>】掉落物品【<$CurItemName>】，位置：<$maptitle> <$ScatterItemX>:<$ScatterItemY>
ChangeItemNameColor -1 253
SENDMSG 0 【<$CurUserName>】掉落物品【<$CurItemName>】物品位置<$H.CurItemPos>物品序列号:<$CurItemMakeIndex>，位置：<$H.maptitle> <$H.ScatterItemX>:<$H.ScatterItemY>
SENDMSG 5 中止掉落身上物品【<$CurIt …[截断]

### 个人商店购买物品前触发
**功能：**个人商店购买物品前触发
**格式：**购买前触发QF脚本
ISONMAP 3
Messagebox 购买失败\\只能在盟重安全区使用购买功能
CHECKGAMEGOLD > 999
Sendmsg 5 对不起，您的元宝不足。

### 系统商铺赠送物品前触发
**功能：**商铺赠送物品前触发
**格式：**商铺赠送物品前触发
**说明：**商铺赠送物品前触发

### 物品进入背包触发
功能说明:
说明：物品进入背包会触发QF内的 [@AddBag] 标签端
示例：
Sendmsg 6 提示:【<$CurItemName>】进到了你的背包！
示例2：
CHANGEITEMNAMECOLOR -1 253
CHANGEITEMUPGRADECOUNT -1 + 1
UpdateItem -1
Sendmsg 6 提示:【<$CurItemName>】进到了你的背包，物品序列号:<$CurItemMakeIndex>
示例3：
GetItemFieldValue -1 makeindex N1
GetItemFieldValue -1 idx N2
GetItemFieldValue -1 hdc N3
Sendmsg 6 提示:【<$CurItemName>】进到了你的背包，物品序列号:<$STR(N1)>，物品idx:<$STR(N2)>，物品DC2:<$STR(N3)>

### 仓库存取物品前触发
功能说明:
说明：仓库存取物品前触发
示例：
CHECKLEVELEX < 50
SENDMSG 6 等级低于50级无法使用仓库
示例2：
Sendmsg 6 提示:存放物品【<$CurItemName>】进到了你的普通仓库，物品序列号:<$CurItemMakeIndex>
Sendmsg 6 提示:取回物品【<$CurItemName>】进到了你的背包，物品序列号:<$CurItemMakeIndex>

### 货币改变触发
功能说明:
说明：货币改变触发
SENDMSG 6 当前金币发生了变更 ，原来为：<$OldMoney>，改变后为：<$NewMoney>(或者用<$GoldCount>)

### 查看他人装备触发、查看装备触发[!]
功能: 查看他人装备触发、查看装备属性触发
SENDMSG 5 你查看了他人<$UserStateName>的装备
SENDMSG 5 你查看了英雄<$UserStateName>的装备
SENDMSG 5 他人<$CurUserName>查看了你的装备
SENDMSG 5 他人<$CurUserName>查看了你的英雄装备
SENDMSG 5 禁止查看他人<$UserStateName>的装备
SENDMSG 5 禁止查看英雄<$UserStateName>的装备
SENDMSG 5 禁止查看人形怪<$UserStateName>的装备
MOV S1 <$UserStateName>
SetCurrTarget S1
CompareText <$C.USERNAME> S1

### 传送戒指传送触发、坐标传送触发[!]
功能: 传送戒指传送触发、坐标传送触发

### 带上物品时触发[!]
功能: 带上物品时触发 位置0-12
CheckLevelEx >

### 地图魔法系统


### 地图事件触发
; 格式:
; 格式:
SENDMSG 0 【地图:%m】【物品:%s】【坐标(%x:%y】 255 253
SENDMSG 0 【地图:%m】【物品:<$SCATTERITEMNAME>】【坐标(<$SCATTERITEMX>:<$SCATTERITEMY>】 255 253
SENDMSG 7 物品：<$H.SCATTERITEMNAME>，掉落在地图：<$H.maptitle><$H.SCATTERITEMX>,<$H.SCATTERITEMY>
CheckInMapRange 3 354 337 0
SetOffTimer 12
CheckInMapRange 3 354 337 0
OPENPULSE 0 1
CHANGEEXP + 200000

### 定时触发[!]
DelayCall 时间毫秒 触发字段

### 个人商店和人物摆摊
MESSAGEBOX 需要在安全区才能摆摊
MESSAGEBOX 你是否确认要停止摆摊 @确定开始或停止摆摊
MESSAGEBOX 你是否确认要开始摆摊 @确定开始或停止摆摊
MESSAGEBOX 你还没有个人商店，是否创建你的个人商店？\\点击确定创建个人商店。 @创建个人商店 @取消
MESSAGEBOX 你已经有店铺了
CHECKSHOPNAME <$STR(S1)>
MESSAGEBOX <$STR(S1)>店铺名称已经存在，请重新选择一个
CREATEMYSHOP <$STR(S1)>
MESSAGEBOX 失败。店铺名称包含禁用字符

### 个人商店名称过滤触发
**功能：**
**格式：**
MESSAGEBOX 失败。店铺名称包含禁用字符

### 个人商店物品上架触发、下架触发、停止个人商店物品上架、停止个人商店物品下架
功能说明：个人商店物品上架触发、下架触发、停止个人商店物品上架、停止个人商店物品下架
SENDMSG 7 禁止上架物品到商铺<$UserShopName>，物品数据库名：<$CURITEMNAME>；物品名：<$G\_CURITEMNAME>；ID：<$CurItemMakeIndex>；售价：<$CurItemPrices><$CurItemMoneyType>(货币类型值：<$CurItemMoneyTypeValue>)
SENDMSG 7 禁止商铺下架物品：<$UserShopName>，物品数据库名：<$CURITEMNAME>；物品名：<$G\_CURITEMNAME>；ID：<$CurItemMakeIndex>；售价：<$CurItemPrices><$CurItemMoneyType>(货币类型值：<$CurItemMoneyTypeValue>)
SENDMSG 7 禁止上架物品到摊位，物品数据库名：<$CURITEMNAME>；物品名：<$G\_CURITEMNAME>；ID：<$CurItemMakeIndex>；售价：<$CurItemPrices><$Cur …[截断]

### 攻击触发
CHECKCURRTARGETRACE = 0
SENDMSG 6 你被人物【<$CURRRTARGETNAME>】攻击了。使用魔法ID=<$CURRRUSEMAGICID> 255 253
CHECKCURRTARGETRACE = 1
SENDMSG 6 你被英雄【<$CURRRTARGETNAME>】攻击了。使用魔法ID=<$CURRRUSEMAGICID> 255 253
CHECKCURRTARGETRACE = 151
SENDMSG 6 你被分身【<$CURRRTARGETNAME>】攻击了。使用魔法ID=<$CURRRUSEMAGICID> 255 253
SENDMSG 6 你被宝宝【<$CURRRTARGETNAME>】攻击了。。宝宝主人：【<$CurTargetMasterName>】 使用魔法ID=<$CURRRUSEMAGICID> 255 253
SENDMSG 6 你被怪物【<$CURRRTARGETNAME>】攻击了。使用魔法ID=<$CURRRUSEMAGICID> 255 253
CHECKCURRTARGETRACE = 0
SENDMSG 6 你 …[截断]

### 购买个人商店物品触发
功能说明：购买个人商店物品触发，个人商店物品卖出后提款成功触发，个人商店出售物品触发
示例QF触发代码：
EQUAL <$CurItemMoneyTypeValue> 0
GameGold + <$CurItemPrices>
EQUAL <$CurItemMoneyTypeValue> 1
GamePoint + <$CurItemPrices>
EQUAL <$CurItemMoneyTypeValue> 2
GoldCount + <$CurItemPrices>
EQUAL <$CurItemMoneyTypeValue> 3
GameDiamond + <$CurItemPrices>
EQUAL <$CurItemMoneyTypeValue> 4
GameGird + <$CurItemPrices>

### 加入行会成员前触发,中止行会成员添加
SendMsg 5 当前要加入行会的人是：<$JoinGuildHuman>

### 界面帮助按钮触发
格式:

### 聚灵珠使用前触发
功能说明:
说明：聚灵珠使用前触发、聚灵珠使用前中断命令
示例：
CHECKLEVELEX > 50
SENDMSG 6 等级大于50级无法使用聚灵珠

### 连击完成触发，连击释放触发
功能：连击完成触发，连击释放触发
SENDMSG 6 连击施展完成

### 切换地图触发[!]
**功能：**
SENDMSG 5 你已更换地图....
SENDMSG 5 英雄更换地图了....

### 切换攻击模式触发
格式: @AttatckModeChange
说明:切换攻击模式触发（仅限Ctrl+H触发QF字段，不含脚本命令切换攻击模式）
SENDMSG 7 切换攻击模式触发

### 取下身上物品时触发[!]
功能: 取下身上物品时触发,位置0-12
CheckLevelEx >
ChangeItemName -1 新的名称
SENDMSG 0 镶嵌装备已改为“新的名称”
GetItemFieldValue -1 name S3
GetItemFieldValue -1 idx S1
GetItemFieldValue -1 name\_g S2
SendMsg 0 当前操作的装备Idx：<$Str(S1)>；改名名称：<$Str(S2)>，数据库名称：<$Str(S3)>

### 人物大退触发


### 人物当前获得经验触发
SENDMSG 5 ：人物本次获取经验为:<$GetExp>

### 人物和英雄属性发生变更时触发QF脚本[!]
**功能：**
说明：本命令触发属性计算的里面不要修改属性，否则无限死循环引起M2崩溃，可用于刷新战斗力

### 人物取下装备前触发、英雄取下装备前触发
功能说明：人物取下装备前触发、英雄取下装备前触发
CHECKMAPNAME 3
SENDMSG 6 你身上的物品位置<$CurItemPos>，名称：<$CurItemName>，改名名称：(<$G\_CurItemName>)，ID<$CurItemMakeIndex> 在当前地图禁止更换！
EQUAL <$H.CurItemName> 屠龙
SENDMSG 7 禁止英雄脱装备：位置:<$H.CurItemPos>，物品:<$H.CurItemName>(<$H.G\_CurItemName>)，ID:<$H.CurItemMakeIndex>

### 人物升级触发
MessageBox 升级

### 人物死亡
**功能：**
**格式：**
CHECKCURRTARGETRACE = 0
SENDMSG 6 你被人物【<$CURRRTARGETNAME>】杀死了 255 249
CHECKCURRTARGETRACE = 1
SENDMSG 6 你被英雄【<$CURRRTARGETNAME>】杀死了 255 249
CHECKCURRTARGETRACE = 151
SENDMSG 6 你被分身【<$CURRRTARGETNAME>】杀死了 255 249
SENDMSG 6 你被宝宝【<$CURRRTARGETNAME>】杀死了,目标主人：【<$CurTargetMasterName>】 255 249
SENDMSG 6 你被怪物【<$CURRRTARGETNAME>】杀死了 255 249

### 人物死亡时触发
SendMsg 5 玩家
SendMsg 5 怪物 <$MONKILLER> 在%m
SendMsg 5 玩家
SendMsg 5 怪物 <$KILLER> 在%m
KillByHum 检测人物杀死为显示人物，宝宝杀死则为怪物（非人物）
CheckKillByHum 检测为凶手为人物包含人物的任意下属 （含宝宝，英雄和英雄宝宝均检测为人物）
SendMsg 5 玩家 <$KILLER> 在%m 把你干死了!
SendMsg 5 怪物 <$KILLER> 在%m 把你干死了!

### 人物小退触发


### 杀死怪物时触发,杀怪触发
功能: 杀死怪物时触发
说明:
SENDMSG 7 你杀死<$KILLMONNAME>
SENDMSG 7 你英雄杀死<$H.KILLMONNAME>
SENDMSG 7 你杀死<$KILLMONNAMEex>
SENDMSG 7 你英雄杀死<$H.KILLMONNAMEex>

### 杀死人物宝宝时触发[!]
功能: 杀死人物宝宝时触发
CheckKillSlaveName 月灵
SendMsg 5 你把对方的月灵宝宝杀死了.

### 杀死人物触发
MessageBox 你杀人了

### 沙巴克行会触发[!]
功能：沙巴克行会触发

### 套装触发
SENDMSG 0 圣战套装隐藏属性被激发:攻击上限增加5点!
SENDMSG 0 法神套装隐藏属性被激发:魔法上限增加5点!
SENDMSG 0 天尊套装隐藏属性被激发:道术上限增加5点!
SENDMSG 0 圣战套装隐藏属性失效:攻击恢复正常!
SENDMSG 0 法神套装隐藏属性失效:魔法恢复正常!
SENDMSG 0 天尊套装隐藏属性失效:道术恢复正常!
CheckGroupItem 套装编号
CheckGroupItem 1
SENDMSG 7 1号套装生效
SENDMSG 5 1号套装未生效
CheckGroupItem 1
SENDMSG 7 1号套装生效
SENDMSG 5 1号套装未生效

### 退出行会触发[!]
功能：退出行会时触发

### 外挂触发[!]
ChangeModeEx 10 10
SENDMSG 6 使用外挂，锁定10秒

### 物品触发脚本功能
**功能：**

### 物品掉落触发
功能说明：物品掉落触发（怪物）-------列表信息二 物品规则
GetUserItemName -1 1 1
CompareText S1 偃月
ChangeItemNameColor -1 253
SENDMSG 5 【<$CurUserName>】掉落物品【<$CurItemName>】，位置：<$maptitle> <$ScatterItemX>:<$ScatterItemY>

### 物品捡取和丢弃触发
SENDMSG 0 玩家<$USERNAME>在<$MapTitle>坐标<$X>：<$Y>扔掉了力量戒指
SENDMSG 0 玩家<$USERNAME>在<$MapTitle>坐标<$X>：<$Y>捡到<$PICKDROPITEMNAME>
SENDMSG 0 玩家<$USERNAME>在<$MapTitle>坐标<$X>：<$Y>扔掉<$PICKDROPITEM>
**注意：需要使用此触发需要在（选项――》列表信息2――》物品规则――》增加“触发ID”）选择触发物品！**

### 物品捡取和丢弃触发
SENDMSG 0 玩家<$USERNAME>在<$MapTitle>坐标<$X>：<$Y>扔掉了<$PICKDROPITEMNAME>
SENDMSG 0 玩家<$USERNAME>在<$MapTitle>坐标<$X>：<$Y>捡到<$PICKDROPITEMNAME>
SENDMSG 0 玩家<$USERNAME>在<$MapTitle>坐标<$X>：<$Y>捡到<$PICKDROPITEMNAME>

### 限时装备到期(到时间)触发


### 英雄当前获得经验触发
SENDMSG 5 ：英雄本次获取经验为:<$H.GetExp>

### 英雄上线触发
H.CHECKNAMELIST ..\QuestDiary\数据文件\英雄名单.txt
H.DELSKILL 破魂斩
H.DELSKILL 劈星斩
H.DELSKILL 雷霆一击
H.DELSKILL 噬魂沼泽
H.DELSKILL 末日审判
H.DELSKILL 火龙气焰
H.delnamelist ..\QuestDiary\数据文件\英雄名单.txt
H.gender man
H.give 恶魔长袍(男) 1
H.give 骨玉权杖 1
H.TakeOnitem 骨玉权杖 1
H.TakeOnitem 恶魔长袍(男) 0
H.give 超级金创药 4
H.give 超级魔法药 3
SENDMSG 4 恭喜<$USERNAME>您的英雄领取了装备
H.gender WOMAN
H.give 恶魔长袍(女) 1
H.give 骨玉权杖 1
H.TakeOnitem 骨玉权杖 1
H.TakeOnitem 恶魔长袍(女) 0
H.give 超级金创药 4
H.give 超级魔法药 3
SENDMSG 4 恭喜<$USERNAME>您的英雄领取了装备
H.gender man
H.giv …[截断]

### 英雄升级触发
H.give 金条 2

### 英雄死亡
**功能：**
**格式：**
SENDMSG 6 你英雄死亡了 255 249
H.CHECKCURRTARGETRACE = 0

### 英雄学习技能触发
功能说明：英雄学习技能QF触发
SENDMSG 6 英雄学习技能 <$H.LearnMagicID>

### 战斗状态触发
功能说明:
说明：战斗状态禁止退出、进入战斗状态触发、退出战斗状态触发
示例脚本（仅在开启禁止战斗状态退出的地图生效）：
SENDMSG 6 进入战斗状态触发
SENDMSG 6 退出战斗状态触发

### 指定人物触发字段
HCALL 人物名称 触发字段

### 指定人物触发字段[!]
HCALL 人物名称 触发字段

### 装备持久消失时触发
功能: 装备持久消失时触发,位置0-12
SendMsg 5

### 装备升级触发[!]


### 走路触发和跑步触发
**功能：**
**格式：**

### 组队时触发
功能: 创建小组时触发.
说明: 队员的名字放在队长S0变量中.
SendMsg 5 <$STR(S0)>加入了组队.
CheckLevelEx < 25
SendMsg 5 25级之后才可以组队.
功能: 离开队伍时触发.
说明: 被删除的队员名字放在队长的S0变量中.
SendMsg 5 你退出了组队.
功能: 删除小组成员时触发.
说明: 被删除的队员名字放在队长的S0变量中.
功能: 添加小组成员时触发.
说明: 队员名字放在队长的S0变量中....
SendMsg 5 <$STR(S0)>加入了队伍.
功能: 组队杀死怪物时触发.
SendMsg 5 组队杀怪.