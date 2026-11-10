# 摘要：兼容其它引擎的命令（107 章）


### 宝宝立即叛变
功能:
格式: GetCallMob
功能: 指定宝宝立即叛变的脚本命令
格式: GetCallMob 宝宝名字
GetCallMob 宝宝名字 数量 (0为所有相同名字宝宝都叛变 1为只叛变一个.2为叛变2个 其它类堆) 分身是否保留(0:不保留收回分身/1:保留分身叛变)
GetCallMob 无参数形式 所有的宝宝立即叛变(分身收回)
CheckSlaveCount > 0 <$UserName> 1
GetCallMob <$USERNAME> 1 1
SENDMSG 5 你没有分身

### 不允许宝石升级
功能: 当前宝石升级装备失败
格式: SetUpgradeFail
说明:
Take 金币

### 查看动态地图链接点
说明:
格式: GetMapRouteInfo 链接标示 查看方式(0-1) 坐标X
GetMapRouteInfo 1 0 A0 G0
GetMapRouteInfo 1 1 A1 G2 G3
SendMsg 5

### 拆解物品
功能:
格式: OpenItemBoxEx 标号(1-1000) 是否回收(0,1) 提示信息
说明:
注意:
相关检测脚本命令:EQUAL  CheckTextList
EQUAL S0
Give 力量戒指 3
EQUAL S0
Give 泰坦戒指 3
EQUAL S0
Give 紫碧螺

### 穿人模式
功能: 改变当前人物的穿人,穿怪模式.
格式:
THROUGHHUM 模式 时间(秒)
ThroughHum 1 60
SendMsg 5

### 创建目录
功能:
格式: ForceDirectories 目录

### 打开网站地址
功能: 游戏中打开网站.
格式: OpenWebSite 网站

### 打开游戏商铺
功能: 打开游戏中商铺窗口.

### 地图随机物品
使用说明: 添加的物品可自动出现在指定地图的指定范围内.
添加格式: 物品名称 出现地图 坐标X:坐标Y 几率:范围:时间:数量

### 动态修改地图名字
功能: 动态修改地图显示名字.
格式:
ChangeMapDesc 新名字 是否保存(0,1)
说明:
ChangeMapDesc 新盟重

### 读取文本内容到变量[!]
功能: 读取文本文件中的内容到变量中.
格式:GetListString 文件路径 行号(行号从0开始) 变量1 变量2 是否绝对路径(0,1)
说明: 变量2可以不需要,当读取变量2时文本单行的内容必须是以下格式:
GetListString ..\QuestDiary\测试.txt 5 A10 N10

### 改变宝宝名字颜色
功能: 改变人物宝宝名字颜色.
格式:
ChangeSlaveNameColor 宝宝名字 颜色(0-255)

### 改变人物的模式
格式: ChangeModeEx 模式(1-10)  时间(1-65535)
说明: 1=无敌 2=隐身 3=HP  4=MP  5=攻击力 6=魔法力 7=道术力 8=攻击速度 9=禁止攻击
ChangeModeEx 1
ChangeModeEx 5 60

### 改变物品的持久
功能:
格式: ChangeItemDura 装备位置(0-12) 操作符(+,-,=) 持久(0-65000) 是否修改最大持久 (0或空为当前持久。1为修改最大持久)
ChangeItemDura 0 - 1000
ChangeItemDura 0 + 1000 1

### 改变衣服翅膀效果
说明:客户端需要有HumEffect.wil
ChangeDressEffect 特效编号 绘制方式(留空或0:特效绘制；1:普通绘制)

### 改变用户模式
格式: ChangeModeEx 模式(1-10) 时间(1-65535) 附加值(1-21e)
说明: 1=无敌 2=隐身 3=HP 4=MP 5=攻击力 6=魔法力 7=道术力 8=攻击速度 9=禁止攻击 10=锁定 11=护身 12=防麻痹 13=破复活 14=传送 15=防止冰封
ChangeModeEx 1 60
ChangeModeEx 5 60 20

### 改变指定行会的掌门人


### 给予带绑定状态装备[!]
功能：
格式：
格式:GiveStateItem 装备位置(-1~13,-1时为OK框中物品)
GiveStateItem 物品名称 项目1 项目2 项目3 项目4 项目5 项目6(0为正常,1为绑定)
GiveStateItem 木剑 1 0 0 0 0 0
SENDMSG 6 给你一个绑定木剑并且禁止扔

### 给字符串增加空格
格式: SetStringBlank 变量(S,A) 长度(1-100) 格式(0, 1)?
说明: 可支持人物S变量或者全局A变量,格式0=前面,1=后面
注意: 第二个参数长度是指增加空格后整个字符串的长度,例如字符串MirYQ引擎长度是9,
注意: 英文字母和数字占用1个字节(长度),汉字占用2个字节(长度).
MOV S10 MirYQ引擎
SetStringBlank <$STR(S10)> 15 0
SendMsg 5 <$STR(S10)>
MOV S10 MirYQ引擎
SetStringBlank <$STR(S10)> 15 1
SendMsg 5 <$STR(S10)>

### 关闭大对话框模式
功能: 关闭大对话框模式. (专用登录器)
格式:

### 获取对面人物的名字
说明: 获取对面人物的名字
格式: GetOppositeHumName
GetOppositeHumName S0
SendMsg 5 你对面的人物是:

### 获取玩家名字
功能:
格式:
GetUserName 0-99之间的数字,或者范围是0-99之间的数值型变量.

### 建立新行会
说明: 第二个参数等于Self时掌门是自己.否则是在线玩家.
AddGuild 华山派

### 建立一个文本文件
注意:文件保存在 \Envir目录中.

### 禁言、恢复发言
Gmexecute Shutup Self 888888
SendMsg 5 您被禁言了.
Gmexecute ReleaseShutup Self
SendMsg 5 您可以正常聊天了.

### 排序人物自定义变量[!]
功能: 排序人物自定义变量.
格式: SortHumVarToListEx 变量名 变量路径 排序模式(0,1) 保存路径 保存模式(0,1) 变量文件是否绝对路径(0,1) 保存文件是否绝对路径(0,1)
说明: 排序模式
QQQQ ..\QuestDiary\测试.txt 0 ..\QuestDiary\测试A.txt
QQQQ ..\QuestDiary\测试.txt 0 ..\QuestDiary\测试A.txt 1

### 排序在线人物自定义变量[!]
功能: 排序在线人物自定义变量.
格式: SortHumVarToList 变量类型(HUMAN,GUILD,GLOBAL) 变量名 保存路径 排序模式(0,1)
说明: 排序模式 0=升序,1=降序
注意: 此脚本命令只排序在线人物的变量
HUMAN QQQQ ..\QuestDiary\测试.txt
HUMAN QQQQ ..\QuestDiary\测试.txt 0

### 屏幕中间显示公告
功能: 在专用登录器屏幕的中间显示公告.
格式:
SendCenterMsg 前景色 背景色 消息文字 模式 显示时间 倒计时标签 是否替换模式（0或空为不替换，不等于0为替换模式) X坐标
说明:
SendCenterMsg 180 251
SendCenterMsg 180 251
SendCenterMsg 180 251 还剩余%d发放新手奖励. 0 30
Give 裁决之杖 1
Give 圣战戒指 2
Give 圣战手镯 2
Give 圣战头盔 1
Give 天魔神甲
SendCenterMsg 180
SendCenterMsg 180 251 还剩余%d离开本地图. 5 600
SendCenterMsg 180 25 …[截断]

### 强制攻击模式
功能: 强制人物的攻击模式
格式: SetHumAttackMode 攻击模式(0-7)
说明: 0=全体模式 1=和平模式
CheckPkPoint 2
SetHumAttackMode 1 3600
CheckPkPoint 2
SetHumAttackMode 1 3600 3
CheckPkPoint 2
SetHumAttackMode 1 3600 \*

### 清除宝石升级属性
功能: 清除使用宝石升级的装备属性.
格式: ClearStoneUpgrade 位置(0-14)
注意:

### 取得随机字符串
功能: 从文件中随机获取一行字符串
格式:
GetRandomText 文件路径 变量(S0--S99) 指定行(1-10000)
说明:
SendMsg 5
SendMsg 5

### 取下人物身上装备
格式: TakeEx (0-51)
TakeEx 1

### 取装备名字
格式: GetUserItemName
说明: S变量是人物私有变量(0-99) 参数3是否只取DB中的名称(0:若改名以改名为准； 1：只取DB中的名称）
GetUserItemName 1 10
SendMsg 5

### 取字符串在列表中的位置
功能: 取字符串在列表中的下标.
格式: GetStringPos 路径 字符串 是否绝对路径(0,1)
说明:
返回值放在人物的N0变量中,如果值=9999999说明没有找到.
返回值可以通过EQUAL做条件检测
SendMsg 5

### 人物聊天文字变色
功能: 改变人物公聊时的文字信息颜色.
格式: ChangeHearMsgColor 时间(分钟) 颜色(0-255)
ChangeHearMsgColor 10

### 杀死地图中的怪物
功能: 随机杀死地图中的怪物.
格式: RandomKillMon 地图 怪物名字 数量(1-255)
说明: 地图=Self时表示当前地图.
RandomKillMon Self 稻草人

### 杀死人物的宝宝
说明:把自己的宝宝杀死.
格式:KillCallMob 名字
KILLCALLMOB 神兽
KILLCALLMOB 白野猪

### 删除地图动态链接点
功能: 删除使用AddMapRoute设置的地图链接点.
格式:
DelMapRoute 动态链接标示(1-65535)
DelMapRoute 1

### 设置人物伤害吸收
说明:设置人物可吸收收到的攻击伤害.
格式: SetSuckDamage 操作符(+ - =) 总吸收值(1-2000000000)
CheckGold 10000
SetSuckDamage = -1 800 100

### 设置人物商铺购买价格比例
功能: 设置人物商铺购买物品的价格比例.
格式:
SetShopItemPriceRate 比例(1-100)
注意: 人物下线后状态消失.
SetShopItemPriceRate 90

### 设置英雄伤害吸收
说明:设置英雄可吸收收到的攻击伤害.
格式: SetHeroSuckDamage 操作符(+ - =) 总吸收直(1-2000000)
CheckGold 10000
SetHeroSuckDamage + 1000 200 95
Take 金币
H.SetSuckDamage = -1 800 100

### 设置装备绑定状态[!]
功能：设置装备绑定状态。
格式：SetItemState 装备位置(-1~13,-1时为OK框中物品) 项目(0-5) 属性(0为正常,1为绑定)
CheckItemState 0 0
SENDMSG 6 该装备已经设置过禁止扔
SENDMSG 6 没有绑定禁止扔掉
CheckItemState 0 0
SENDMSG 6 该装备已经设置过禁止扔
SetItemState 0 0 1
SENDMSG 6 该装备禁止扔
CheckItemState 1 7
SENDMSG 6 该装备已经设置过取下
SetItemState 1 7 1
SENDMSG 6 该装备禁止取下

### 设置装备发光
功能: 设置装备发光
说明: 衣服,武器和头盔不支持次功能.
格式: SetItemsLight 位置(0-12) 值(1=发光效果1 2=发光效果2 0=不发光).
SetItemsLight 3
SetItemsLight 3
SetItemsLight 3 0

### 收回人物的英雄
功能: 收回人物的英雄.
格式:
功能: 收回人物的英雄.
格式:

### 随机验证码
CheckLevelEx > 0

### 所有行会同时攻城
功能:所有行会在当晚同时攻城
AddAttackSabukAll 城堡号(0)

### 特修身上装备
CHECKREPAIRALLGOLD <$STR(N99)>

### 调整英雄的PK值[!]
ChangeHeroPkPoint +
ChangeHeroPkPoint -
ChangeHeroPkPoint =

### 调整英雄的忠诚度
格式: ChangeHeroLoyal 操作符(+ - =) 数值(0 -- 10000)
注意: 第二个参数+1那么英雄增加0.01点忠诚+100那么英雄增加1点忠诚
ChangeHeroLoyal + 100
SendMsg 5 您的英雄忠诚度增加[1]
功能: 检测英雄当前的忠诚度
格式: CheckHeroLoyal 操作符(< = >) 数值(0 -- 100)
CheckHeroLoyal > 50
SendMsg 5 您的英雄忠诚度大于50%.

### 调整英雄等级[!]
ChangeHeroLevel 操作符(+ - =) 级别(1-65535)
ChangeHeroLevel =

### 调整英雄职业
格式: ChangeHeroJob 职业(0,1,2)

### 物品合成系统
使用说明: 以合成逆火麻痹戒为例:
GiveFoundryItem 逆火麻痹戒
SendMsg 5 缺少合成物品<%Item>
SendMsg 5 合成
CheckFoundryItem %FoundryItem
GiveFoundryItem %FoundryItem
SendMsg 5 合成 <%Item>
SendMsg 5 合成 <%Item>

### 写入指定文本文件
功能: 把字符串写入到指定的文本文件中,可以指定写入行.
格式: AddTextListEx 路径 字符串 行(0-65535) 是否绝对路径

### 新的装备改名
功能: 新的装备改名
格式: ChangeItemName
ChangeItemName 1
H.ChangeItemName 1
Changeitemname 1 屠龙[强化+<ImgNum:1:10:1:0:0:0>]
Changeitemname 1 屠龙<img:74:79:0:0>
注意设置装备名字颜色如果使用了PlayImg 参数8(指定鼠标指向后提示信息的高度):参数9(指定鼠标指向后提示信息宽度) ，不用PlayImg的话可以无视！！
Changeitemname 1 {我|70}是彩色的{极品|249}<PlayImg:1:520:10:100:0:0:0:20:20>

### 延时执行脚本
DelayCall S Label (S单位毫秒,
DelayCall 5000 @Kick

### 移动怪物到新坐标
功能: 移动指定坐标的怪物到新的位置.
格式: MoveMonToPos
CheckRangeMonCountEx K004 魔王弓箭手 51 43
MoveMonToPos 魔王弓箭手 K004 51 43 48

### 移动某地图全部人物到另外一个地图
MoveMapPlay 0 3 333

### 英雄登录器荣誉
格式:
ChangeHumCreditEx 操作符(+ - =)
ChangeHumCreditEx +

### 英雄增加以及删除技能
H.ADDSKILL 英雄治愈术 3
SENDMSG 4 恭喜<$USERNAME>您的英雄学习了英雄治愈术三级
H.DELSKILL 英雄治愈术
SENDMSG 4 恭喜<$USERNAME>您的英雄英雄治愈术技能已经被删除
注意:如果清除后英雄技能依然显示存在,那么请更新最新登录器.

### 增加限次使用物品的次数
说明:
CheckLevelEx <
ChangeLevel +
CheckLevelEx <
ChangeLevel +
AddFunItemDura 100 ;持久增加100

### 召唤自己的分身
格式:RecallSelf 分身有效时间 数量 继承人物属性百分比 分身颜色(0-255;0不改变颜色) 改变分身衣服外观(0或空为不改变) 改变分身武器外观(0或空为不改变) X坐标 Y坐标
RecallSelf 60 3 150 251 1 1

### 自定义颜色文字发送
功能说明:
格式: GuildNoticeMsg 255 233 发送自定义颜色的文字信息.
参数一是前景颜色,参数二是背景颜色,参数三是要发送的文字信息,参数四等于'Self'时只发送给自己,

### 自动穿戴装备
功能:自动穿背包中的装备
CheckLevelEx > 1
Give 怒斩 1
AutoTakeOnItem 怒斩

### 自动寻路
功能: 自动移动到指定坐标,专用登录器.
格式: GotoNow X
IsOnMap 3
GotoNow 330

### 检测被自己杀死宝宝的名字
注意:此命令只检测直属宝宝,例如道士英雄召唤的神兽不属于直属宝宝.

### 检测本月的天数
功能: 检测是否是本月的第几天.
格式:
DAYOFMONTH 天数(1-31) 天数(1-31)
说明: 第二个参数可省略.

### 检测当前宝石升级装备的名字
功能: 检测当前通过宝石升级装备的名字
格式: CheckUpgradeItemName
说明: 位置0=升级装备的名字 1=左边一格宝石的名字
注意:
CheckUpgradeItemName 0 裁决之杖
Take 金币

### 检测服务器最高属性人物命令
**功能：**
**格式：**    ISHIGH
SENDMSG 0
SENDMSG 0
SENDMSG 0
SENDMSG 0
SENDMSG 0

### 检测人物的攻击模式
说明: 检测人物的攻击模式
格式:
CheckAttackMode 模式(0-7)

### 检测人物的伤害吸收
说明:
格式: CheckSuckDamage
CheckSuckDamage >
SendMsg 5

### 检测人物是否挂机
功能:检测人物是否是离线挂机
格式:CheckOffline

### 检测物品持久
功能:检测人物身上物品持久.
格式:CheckItemDura 位置(0-12) 操作法(> = <)
说明:默认模式=0表示检测物品持久下限,模式=1时检测物品持久上限.

### 检测物品纯度
功能:
格式: CheckMine 物品名称 数量(1-45) > = < 纯度(1-65)
CheckMine 黑铁矿石 5 =

### 检测新属性
功能: 检测当前装备是否附加了新属性. 专用登录器.
格式: CheckNewItemValue 位置(0-18) 属性(0-5)
说明: 属性 0=致命一击 1=攻击伤害增加
CheckNewItemValue 1 0 >
CheckNewItemValue 1 1 >
CheckNewItemValue 0 5 >

### 检测英雄的PK值
CheckHeroPkPoint >

### 检测英雄的伤害吸收
说明: 检测英雄的伤害
格式: CheckHeroSuckDamage
CheckHeroSuckDamage >
SendMsg 5

### 检测英雄的忠诚度
功能: 检测英雄当前的忠诚度
格式:
CheckHeroLoyal 操作符(< = >) 数值(0 -- 100)
CheckHeroLoyal >
SendMsg 5 您的英雄忠诚度大于50%.

### 检测英雄登录器荣誉
格式: CheckHumCreditEx 操作符(> = <)
CheckHumCreditEx <
ChangeHumCreditEx = 10

### 检测英雄职业


### 检测月份
功能:
格式: MONTHOFYEAR 月份(1-12) 月份(1-12)
说明:
MONTHOFYEAR 7 8

### 检测装备的附加属性总和[!]
功能: 检测装备的附加属性总和(武器的诅咒不在计算范围之内).
格式: 格式: CheckItemAddValueEx 位置(0-51 -1升级框 ，boxitem0 -boxitem7自定义OK框) 操作符(> = <) 附加值(0-65000) 新属性(0,1)
说明: 第四个参数只在英雄M2下有效,1时计算附加的致命一击等属性.
CheckItemAddValueEx 1 > 5 1

### 检测装备名字颜色
功能:
格式: CheckItemNameColor 位置(0-13)
CheckItemNameColor 1

### 检测字符串长度命令
**功能：**
**格式：**
CheckStringlength 字符串 操作符(<,>,=) 位数
说明：一个汉字位数为2, "》"也为2个字符
CheckStringlength lfm2 > 3

### 检查宝宝数量
**功能：**
**格式：**CHECKSLAVECOUNT  控制符  <.=.>
CHECKSLAVECOUNT =
CHECKSLAVECOUNT >
CHECKSLAVECOUNT <
格式：
CHECKSLAVECOUNT 控制符 <.=.> 数量
CHECKSLAVECOUNT 控制符 <.=.> 数量 宝宝名字 是否检查名称数字(0:不检查名称数字[骷髅1,骷髅2都按包骷髅算], 1:算数字)

### 检查宝宝最高等级
命令格式:
CHECKSLAVELEVEL 控制符(=,>,<)  等级数(7)< /FONT>
CHECKSLAVELEVEL =
CHECKSLAVELEVEL >
CHECKSLAVELEVEL <

### 检查地图中的人物是否属于同一个行会
格式: MapHumIsSameGuild 是否忽略没有加人行会的人物(0-1)

### 检查人物被踢次数


### 检查人物杀死怪物的名字
功能:检查人物杀死怪物的名字
格式:CheckKillMonName 名字
说明:是否清除参数可以不需要默认0,为了避免杀死某个怪物可重复执行脚本是设置1.
CheckKillMonName 白野猪 1

### 检查人物是否学习了某项魔法


### 检查人物是否在指定范围内
功能: 检测人物是否在指定范围之内
格式: CheckHumInRange 地图
说明: 地图=Self时表示当前地图.
CheckHumInRange 3 330 330 5

### 检查人物所在地图是否允许使用记忆,夫妻,师徒传送


### 检查是被人物还是怪物杀死的
SendMsg 5 玩家
SendMsg 5 怪物 <$MONKILLER> 在%m
SendMsg 5 玩家
SendMsg 5 怪物 <$KILLER> 在%m
KillByHum 检测人物杀死为显示人物，宝宝杀死则为怪物（非人物）
CheckKillByHum 检测为凶手为人物包含人物的任意下属 （含宝宝，英雄和英雄宝宝均检测为人物）
SendMsg 5 玩家 <$KILLER> 在%m 把你干死了!
SendMsg 5 怪物 <$KILLER> 在%m 把你干死了!

### 检查是否有英雄


### 检查一个范围内怪物数
**功能：**
**格式：**CheckRangeMonCount 地图号 X坐标 Y坐标 范围 控制符(=,>,<)
CheckRangeMonCount 3 330 330 10 <

### 检查英雄等级
格式: CheckHerolevel 操作符(> = <)
CheckHerolevel =

### 检查正在穿身上装备的名字名字
格式:  CheckTakeonItem 物品名字
格式:  CheckTakeOffItem 物品名字

### 检查正在攻击中的怪物名字
说明: 检查正在被自己攻击的怪物的名字.
注意: 地图参数中加入
CHECKHITMONNAME 白野猪

### 检查正在取下身上装备的名字
格式:  CheckTakeOffItem 物品名字
格式:  CheckTakeonItem 物品名字

### 检查指定范围内人物数量
功能: 检测指定范围内人物数量
格式: 格式:
CheckRangeHumCount 地图 坐标X 坐标Y 范围 操作符(>= <) 数量
说明: 地图=Self时表示当前地图
CheckRangeHumCount 3 330 330 10

### 检查指定人物背包空格数量
CheckHumBag <$STR(S1)> >

### 检查装备升级次数
功能: 用来检测通过宝石升级装备的次数.
格式: CheckItemupgradeCount
说明:
CheckItemUpgradeCount 1 1 >

### 检查自己和宝宝之间的距离[!]
功能: 检测自己和宝宝之间的距离
格式: CheckSlaveInRange 名字
说明: 此命令的主要作用是配合128类型的宝宝使用(可模仿押镖任务).
CheckSlaveInRange 月灵

### 摆摊触发脚本
说明:允许摆摊的地图需要在MapInfo.txt中增加地图参数MyShop

### 购买商铺物品时触发
功能说明: 人物通过商铺购买物品成功时触发(英雄M2).
SendMsg 5
SendMsg 5 购买了商铺物品<$str(S0)>，商品总价<$str(M0)>货币名称<$str(S1)>（货币类型<$str(M1)>)，商铺物品数量<$str(M2)>，批量购买数量<$str(M3)>

### 技能触发脚本功能
说明:
SendMsg 5
SendMsg 5
SendMsg 5 给怪物加血.

### 宝石升级系统[!]
说明:1.打开人物背包点右下脚的升级按钮进行升级.也可使用OpenUpgradeDialog命令打开界面.
Take 金币
注意:此类宝石只增加防御和魔御.
注意:此类宝石只增加攻击,魔法,道术.
注意:升级失败后如果Need小于100那么随机清除某项或者多项附加属性.

### 毒素武器[!]
格式: 武器名称 成功几率 减HP值 基本时间 扩展时间