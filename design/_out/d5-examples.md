# 摘要：部分脚本实例（93 章）


### 53类宝石(封印)介绍[!]
**功能：**
**功能：石头拥有气血石功能 Anicount=1,2,3 分别对应三种石头的回血功能.**
说明

### 神佑袋
| Overlap值 | 位置 |
| --- | --- |
| 0 | 只允许穿身上 |
| **1** | **只允许穿身上 【基础位置】** |
| **2** | **只允许首饰盒【基础位置】** |
| **4** | **只允许神佑【基础位置】** |
| **8** | **只允许时装首饰盒【基础位置】** |
| **16** | **只允许时装神佑【基础位置】** |
| 25 | 1+8+16；身上+时装首饰盒+时装神佑 |
命令格式：**ShowGodBless** 0/1(0:隐藏;1:显示)  是否时装神佑0/1(0:普通神佑;1:时装神佑)
命令格式：**OpenGodBless** 格子位置(0-11, all) 是否时装神佑0/1(0:普通神佑;1:时装神佑)
命令格式：**CloseGodBless** 格子位置(0-11, all) 是否时装神佑0/1(0:普通神佑;1:时装神佑)
命令格式 …[截断]

### 登录游戏时的聊天框最上方显示公告
**功能：**登录游戏时的聊天框最上方显示公告
格式：脚本放入QManage.txt
SENDMSG 1 在登录后“攻击模式”提示前面显示文字<$USERNAME>

### NPC对话框调用背包物品信息（支持物品图片以及展示属性）
**功能：**NPC对话框调用背包物品信息
**说明：** NPC对话框按照物品唯一序列号调用背包物品信息
参数说明：

### CallEx支持多个同样的@地址
功能说明:
示例脚本：
说明：原CALL使用以上脚本全部读取一个脚本的@充值链接，CALLEX读取准确路径中的@充值链接

### IF多条件检测[!]
功能: #IF 多条件检测，#if(3) // 如果众多条件中只需要满足3个条件，即可执行#act , #say.....等
ISONMAP 0
ISONMAP 3
ISONMAP 5
CheckLevel 51
CHECKGAMEGOLD > 19
SENDMSG 满足条件

### LineNotice.txt彩色滚动公告[!]
格式1：[253,0]聊天框公告 0为背景色 253前景色
格式2：<252,255,190> 窗口顶部滚动公告,255为背景色 252前景色 190为背景条颜色（背景条颜色留空为不显示）
格式3：<252,255> 9 公告内容 255为背景色 252前景色，9(9两边用tab键隔开)为公告字体大小(9号不加粗)
格式4：<252,255,190> 10b 公告内容 255为背景色 252前景色 190为背景条颜色，10b(10b两边用tab键隔开)为公告字体大小(10号加粗)

### NPC标签备注功能[!]
**功能：**
**格式：**
SENDMSG 6 按钮事件触发成功

### Npc对话框绝对坐标元素
**功能：**
**功能：Npc对话框元素，多个元素前增加&，命令中原有的偏移坐标加了&后表示绝对坐标**

### NPC对话框内倒计时
说明：NPC对话框内倒计时显示
格式：<COUNTDOWN:倒计时时间(秒):次数(0无限次):颜色:X:Y:M/@触发>
参数M为显示格式：
SendMsg 5 倒计时结束触发
格式：<IMGCOUNTDOWN:倒计时时间(秒):次数(0无限次):开始图片:数字图片间隔:X:Y:M/@触发>
说明：数字图片读取Newopui.pak中的开始图片(图片顺序为0-9:) 第10张图为：号图，以下面示列计算图片编号1330为：号图片，素材自行添加
注意:当在ADDDLG 、ADDDLGEX对话框中需要使用COUNTDOWN倒计时的话，那么触发脚本就不在NPC中，则在QF中，触发字段必须为ADDDLG的专用触发字段
SendMsg 5 倒计时结束触发

### NPC对话框调用身上装备信息（支持物品图片以及展示属性）
参数说明：

### NPC对话框调用装备信息（支持物品图片以及展示属性）
参数说明：

### NPC获取文件行数命令
**功能：**
**功能：NPC获取文件行数命令**
GetTextLineCount ..\QuestDiary\装备回收.txt N$行数
Sendmsg 5 提示:装备回收.txt文件共有<$STR(N$行数)>行内容

### NPC命令打开装备栏及其他页面[!]
**功能：**NPC命令打开任务和英雄的装备栏，属性栏，技能栏，时装栏，称号栏，出战栏
**格式：**命令 参数1 参数2 参数3
OpenHumDlg 5

### Npc文字Text使用
**功能：**
**功能：设置文字在对话框中坐标、颜色、字体大小、字体、粗体显示.**
说明：
格式：Text:文字:提示:X:Y{FCOLOR=250;FSIZE=14;FNAME=黑体;FBOLD=1}/@测试
参数说明:
AUTOCOLOR 彩色字体设置
FSIZE 字体大小
FNAME 字体类型
FBOLD 字体加粗
FCOLOR 字体颜色

### ThrowItem在放置物品之前修改物品的来源
功能说明：使用ThrowItem命令放置物品之前修改物品的来源
说明：本命令只对设置后的一条ThrowItem生效。执行一次ThrowItem后，设置还原。
SetThrowItemFrom 4 3 白野猪 杀人者 2021-01-11 10:00:00
ThrowItem <$map> <$x> <$y> 1 屠龙 1|0
SetThrowItemFrom 4 3 白野猪 杀人者 <$Date> <$Time>
THROWITEM <$MAP> <$KILLMONX> <$KILLMONY> 1 力量戒指 1|120 2 1
SENDMSG 6 当前日期：<$Date>；当前时间<$Time>

### 百分比检测
**格式：CheckHpPer 操作符(>/=/<) 占比类型(留空或0百分比/1千分比/2万分比)**
CheckHpPer > 30
AddhpPer + 30
GuildNoticeMsg 250 0 你的血增加了30% self
**格式：CheckMpPer 操作符(>/=/<) 占比类型(留空或0百分比/1千分比/2万分比)**
CheckMpPer > 30
AddMpPer + 30
GuildNoticeMsg 250 0 你的MP增加了30% self----------------------------------以下2个带EX的命令为当前剩余HP和当前剩余MP，非总HP和MP，，------------------------------------------------------------------------按当前HP值的比例来加减HP**格式：AddHpPerEx 操作符(+/-/=) 比 …[截断]

### 变量支持数字单位
**功能：**
Mov N0 1234567891234567
Mov N1 10000000000

### 创建副将英雄脚本
HAVHERO TRUE
Mov M0 1
OPENPLAYDRINK 2 晨星 DRINK
PLAYDRINKMSG 1 <$USERNAME>，酒之道也可以算作我修行的一部\分，让我看看你的表现吧。
PLAYDRINKMSG 2 嘿嘿……我可不会比你先醉倒，保管陪\你喝爽了！
PLAYDRINKMSG 1 这点酒量，我怎么放心让我的弟子\跟随你啊！
PLAYDRINKMSG 2 惭愧惭愧，我一定努力!\<招幕英雄/@CrHero>
PLAYDRINKMSG 1 好！
PLAYDRINKMSG 2 就这坛了！请前辈来喝!
PLAYDRINKMSG 1 ……
PLAYDRINKMSG 2 就这坛了！我自己喝！
PLAYDRINKMSG 1 就这坛了！你来喝吧！
PLAYDRINKMSG 2 谢谢前辈！
PLAYDRINKMSG 1 就这坛了！我来喝！
PLAYDRINKMSG 2 前辈尽管喝！
PLAYDRINKMSG 1 那再 …[截断]

### 创建行会脚本


### 创建主将英雄脚本
SENDMSG 6 恭喜您领练习内功！！
SENDMSG 6 恭喜您领取合击必备物品火龙之心成功！！
SENDMSG 6 恭喜您领取战士+战士英雄合击[破魂斩]成功！！
SENDMSG 6 恭喜您领取道士+道士英雄合击[噬魂沼泽]成功！！
SENDMSG 6 恭喜您领取法师+法师英雄合击[火龙气焰]成功！！
SENDMSG 6 恭喜您领取战士+法师英雄合击[雷霆一击]成功！！
SENDMSG 6 恭喜您领取道士+法师英雄合击[末日审判]成功！！
SENDMSG 6 恭喜您领取战士+道士英雄合击[劈星斩]成功！！
MESSAGEBOX 对不起，您没有英雄！
MESSAGEBOX 对不起，您的英雄不在线！
CHECKHEROJOB WARRIOR
H.ADDSKILL 英雄基本剑术 3
H.ADDSKILL 英雄攻杀剑术 3
H.ADDSKILL 英雄刺杀剑术 3
H.ADDSKILL 英雄半月弯刀 3
H.ADDSKILL 英雄野 …[截断]

### 达到多少人在线不允许离线挂机脚本
ISONMAP 0
ISONMAP 3
ISONMAP 5
MessageBox 此地图挂机人数已满，请选择其他地图挂机!
OFFLINE 60 2000

### 打开个人店铺（摆摊）
**功能：**
**格式：**

### 大退游戏命令


### 当前目标变量取值操作[!]
功能: 当前目标变量取值操作C. （C.变量必须目标不为空且对象为人物）
CHECKCURRTARGETRACE = 0
SetHumVar <$C.USERNAME> S1 S2
SENDMSG 6 把我的S2变量值传递给当前对象的S1变量里
CHECKCURRTARGETRACE = 0
MOV <$STR(N1)> <$C.STR(N1)>
SENDMSG 6 把对方的的N1变量值传递给我的的N1变量里，使用“C.STR”代表当前对象的变量比自己的“STR”前面多一个“C.”
MOV S1 <$UserStateName>
SetCurrTarget S1
CompareText <$C.USERNAME> S1

### 动态地图连接[!]
ADDMAPGATE 连接名称(为了区别其他连接) 地图号 X(小于0时随机坐标) Y(小于0时随机坐标) 范围 到达地图号 到达地图坐标X(小于0时随机坐标) 到达地图坐标Y(小于0时随机坐标) 有效时间秒(时间到了自动删除该连接,该参数为空时不限时间)
DELMAPGATE 连接名称 地图号
GETMAPGATE 连接名称 地图号 变量1(保存X坐标) 变量2(保存Y坐标) 变量3(保存到达地图号) 变量4(保存到达地X坐标) 变量5((保存到达地Y坐标))
AddMapGate 连接 3 335 330 1 0 335 268 30
GetMapGate 连接 3 <$STR(G10)> <$STR(G11)> <$STR(S10)> <$STR(G12)> <$STR(G13)>
SENDMSG 6 增加地图新连接30秒后删除:[<$STR(G10)>:<$STR(G11)>]到达地图:<$STR(S10)>到达坐标[< …[截断]

### 发送聊天框固顶信息
SENDTOPCHATBOARDMSG 发送模式(0发送给所有人,1发送给自己) 字体颜色 背景颜色 时间(秒) 信息
SENDTOPCHATBOARDMSG 0 149 235 30 %s:聊天框固顶信息

### 复活触发[!]
**功能：**
**说明：QFunction-0.txt脚本触发**
Sendmsg 6 剩余复活时间 <$RevivalTime>
SendMsg 5 你复活了！
SendMsg 5 你的英雄复活了！

### 副本地图相关参数
**功能：**
**格式：**
CANMOVEECTYPE 此命令为检测是否已经创建副本 格式：CANMOVEECTYPE 副本名称
CREATEECTYPE 此命令为创建副本，格式：CREATEECTYPE 副本名称 有效时间
CANMOVEECTYPE 白日门副本
SENDMSG 5 你已创建了一个白日门副本，不能重复创建....
CREATEECTYPE 白日门副本 5[@gon111]
CANMOVEECTYPE 镜像副本
SENDMSG 5 你已创建了一个镜像副本，不能重复创建....
CREATEECTYPE 镜像副本 3[@gon12]
MOVEECTYPE 白日门副本 38 42[@gon112]
MOVEECTYPE 镜像副本 331 270[@CreateEctype\_NoExists]
MESSAGEBOX 创建副本地图失败，副本不存在！[@CreateEctype\_Fail]
MESSAGEBOX 创 …[截断]

### 改变人物状态脚本
**功能：**
**说明：TestStatus 此命令可在M2自定义修改为你需要的命令**
TestStatus 0 0 (参数0为状态类型、参加2为时间 0为清空所有颜色)
Gmexecute TestStatus 5 1

### 会员系统详解
**相关脚本命令**
**相关脚本会员物品**
ADDNAMEDATETIMELIST ..\QuestDiary\会员名单.txt 30 2 3
SENDMSG 6 增加30天2小时3分 255 253
CHECKNAMEDATETIMELIST ..\QuestDiary\会员名单.txt 1 S1 N1 N2 N3
SENDMSG 6 你的会员到期时间是<$STR(S1)>【剩余天数=<$STR(N1)>】【剩余小时=<$STR(N2)>】【剩余分钟=<$STR(N3)>】 255 253
SENDMSG 6 你不是会员或已过期，请及时充值！ 255 253
CheckOnline <$STR(S1)>
ADDNAMEDATETIMELIST ..\QuestDiary\会员名单.txt 30 2 3
SENDMSG 6 <$STR(S1)>充值成功，增加30天2小时3分！ 255 253
SENDMSG 6 <$STR( …[截断]

### 获取徒弟列表
GetMasterList 变量名
GetMasterList S1

### 获取徒弟数量
GetMasterCount 变量名
GetMasterCount P1

### 获取指定位置的物品数量
GetItemCount 位置(0:背包;1:装备; 2:首饰; 3:神佑; 4:普通仓库; 5:无限仓; 6:摆摊) 物品名称 变量
GetItemCount 0 屠龙 N0

### 获取组队成员数量(组队相关命令)
GETGROUPCOUNT 变量名 范围(当范围为空或0时，获取所有队员数量，当范围>0时，获取队长指定范围内队员的数量）
GETGROUPCOUNT P1
GETGROUPCOUNT P1 5
SENDMSG 6 你已经主动离开了队伍
DELETEGROUPMENBER 成员名
SENDMSG 6 你被队长踢出了队伍！

### 机器人脚本
**功能：**
相关配置目录:
相关文件:
机器人配置文件格式:
脚本格式:
实例：
Test Test
SENDMSG 0
MISSION 3 330 330
PARAM1 360
PARAM2 340
PARAM3 10
PARAM4 1
MISSION 3 330 330
PARAM1 360
PARAM2 340
PARAM3 10
PARAM4 5
PARAM5 国家
PARAM6 同国家名玩家是否可攻击(0,1)
PARAM7 不国家名怪物是否PK(0,1)
MOBPLACE 半兽勇士

### 记忆石设置方法[!]
功能演示：
SHAPE 值:1
TAGMAPMOVE 1
TAGMAPMOVE 2
TAGMAPMOVE 3
TAGMAPMOVE 4
TAGMAPMOVE 5
TAGMAPMOVE 6
TAGMAPINFO 1
GOTO @StdModeFunc99
TAGMAPINFO 2
GOTO @StdModeFunc99
TAGMAPINFO 3
GOTO @StdModeFunc99
TAGMAPINFO 4
GOTO @StdModeFunc99
TAGMAPINFO 5
GOTO @StdModeFunc99
TAGMAPINFO 6
GOTO @StdModeFunc99

### 技能栏升级强化技能[!]
**功能：**
**格式：技能数据库 CanUpgrade字段设置0或留空则不显示升级按钮 ，设置1允许升级，设置2不允许升级（显示升级按钮） MaxupgradeLv字段为强化多少重后不再显示升级按钮**
CheckSkill 雷电术 > 8 1
Sendmsg 7 强化雷电术已升至最高等级九级，无法继续升级！
MESSAGEBOX 是否确定使用10张书页，升级强化雷电术至下一等级？ @确定11 @取消
SKILLLEVEL 雷电术 + 1 1
MESSAGEBOX 提示：恭喜您的雷电术又熟练提升了1级

### 假人登录脚本实例
GETRANDOMLINETEXT ..\QuestDiary\智能陪练\假人配置文件列表.txt <$STR(S10)>
SETDUMMYCONFIGFILENAME <$STR(S10)>
MOVR D0 6
ChangeAttatckMode <$STR(D0)>
GETRANDOMLINETEXT ..\QuestDiary\智能陪练\假人英雄配置文件列表.txt <$STR(S11)>
GETDUMMYNAME <$STR(S11)> 1 1
SETDUMMYHERONAME <$STR(S11)>
H.SETDUMMYCONFIGFILENAME <$STR(S11)>

### 假人自动摆摊
CREATEMYSHOP <$USERNAME>

### 检测地图坐标是否可以到达
检测地图坐标是否可以到达格式：
CHECKMAPMOVE 地图名 X坐标 Y坐标==============================================
CHECKMAPMOVE 3 333 333

### 检测人物多少时间没有移动
**功能：**
**格式：**
CHECKSTATIONTIME 控制符(<、>、 =) 分钟
**示例一：**
CHECKSTATIONTIME > 50
**示例二**
CHECKSTATIONTIME > 50
DelayCall 5000 @Kick[@Kick]
Kick 1

### 检查人物的职业 [!]
**功能：**
**格式：**
CheckJob Warrior
CheckJob Taoist
CheckJob Wizard

### 脚本初始化
**格式：**
**说明：**
**示例：**
INC G35 20

### 脚本发送屏幕震动[!]
**功能：**
**格式：**
SceneShake 0 3
SceneShake 1
SceneShake 2 1 1
SceneShake 3
SceneShake 4 0

### 脚本控制怪物攻城
**功能：**
**格式：**
MISSION  地图名 座标X 座标Y
PARAM2 Y
PARAM4 范围
MISSION 3 330 330
PARAM1 360
PARAM2 340
PARAM4 5
MISSION 3 330 330
PARAM1 360
PARAM2 340
PARAM3 10
PARAM4 5
PARAM5 1 国家编号
PARAM6 同国家名玩家是否可攻击(0,1)
PARAM7 不国家名怪物是否PK(0,1)
PARAM8 怪物名字颜色
PARAM9 禁止相同国家的人员攻击怪物（1：禁止；0：不禁止）用禁止可以保留以前的逻辑
MOBPLACE 半兽勇士
格式: MISSION 地图 x1;x2;x3...xn y1;y2;y3...yn (x和y的数量要一致）
MISSION 1v1 141;173;190;206;201 135;102;85;85;70
PARAM1 102
PARAM2  …[截断]

### 脚本增加自定义按钮[!]
**功能：**
**格式：命令 参数1 参数2 参数3 参数4 参数5 参数6 参数7 参数8 参数9 参数10**
ADDBUTTON 3 1 283 284 285 10 200 1 -1 自定义按钮1\测试增加按钮
参数说明：
参数1为WIL补丁序号，此序号在M2-查看-列表信息二-WIL资源 里面编辑
参数2为按钮点击后的脚本触发序号，触发QF里面的[@ButtonClickX]X即为触发序号
参数3为按钮默认图片
参数4为鼠标经过图片
参数5为按钮按下图片
参数6为距离窗口左边的距离(此参数建议用分辨率宽变量计算)
参数7为距离窗口顶边的距离(此参数建议用分辨率高变量计算)
参数8为按钮是否可以移动0=不能移动1=可以移动2=人物装备栏3=人物背包栏4=英雄装备栏5=英雄背包栏6=聊天框左侧龙界面7=聊天框右侧等级界面8=商铺界面9=时装界面,10=英雄时装，11=技能栏，12=英雄技能栏，13=称号栏，14=英雄称号 …[截断]

### 结婚脚本


### 经验怪、经验猪


### 酒神弟子完整脚本[!]
MESSAGEBOX 你还想再学习?
MESSAGEBOX 没有玛法内功心法,你还想学习?
MESSAGEBOX 英雄还想再学习?
H.checkitem 玛法内功心法 1
H.take 玛法内功心法 1
MESSAGEBOX 没有玛法内功心法,你还想学习?

### 开通元宝寄售服务
功能: 开通元宝寄售服务
格式: OPENYBDEAL 数字 //开通元宝交易，数字表示需要的元宝数量 永久使用,保存入人物数据里
QUERYYBSELL //查询正在出售的物品
QUERYYBDEAL //查询可以的购买物品
OPENYBDEAL 1

### 捆药绳[!]
**功能：**
**格式：将多件物品捆绑为一件物品**
CHECKITEM 强效太阳水 6
TAKE 强效太阳水 6
GIVE 太阳水包 1
AddFunItemDura 1000

### 离线挂机[!]
OFFLINEPLAY 100 100 100
功能: 挂机命令
格式:ISDUPMODE (0或空时检测所有对象，1只检测人物)

### 聊天框自定义颜色
聊天框信息颜色自定义格式：
SENDMSG 5 {<$USERNAME>|254:253}翎风引擎官方网站：http://www.lfm2.com
SENDMSG 5 {<$USERNAME>|250:0:1}翎风引擎官方网站：http://www.lfm2.com
SENDTOPCHATBOARDMSG 0 149 235 30 {<$USERNAME>|250:0}翎风引擎官方网站：http://www.lfm2.com
注意请在网关上设置过滤{信息|F:B}中任意字符，防止玩家发送彩色聊天信息

### 魔王岭脚本
MOV A14 <$USERALLNAME>\天下第一战士

### 强制组队脚本
**功能：**
MESSAGEBOX 输入数据中包含了非法字符,请重新编辑![@开始组队]
CheckOnline <$STR(S10)>
CreatGroup <$STR(S10)>

### 清除当前人物的拜师信息
**功能：**
**格式：**    DELMASTER 徒弟序号(为空表示大徒弟、师傅清除指定徒弟使用，徒弟清除师傅以下是示例脚本)

### 人物登录脚本
**功能：**
**格式：**在目录 Envir\MapQuest\_def\ 中建立文件名为QManage.txt的脚本，按以下格式编写脚本：
CHANGEMODE 2 1
CHANGEMODE 3 1
SENDMSG 5

### 人物显示一个放大的虚影[!]
**功能：**
**格式：**
SHOWPHANTOM 255 10

### 人物颜色发型
HAIRSTYLE 0
HAIRSTYLE 1

### 人物转生[!]
**功能：**
**格式：**    RENEWLEVEL 转次数 转后等级
RENEWLEVEL 1 28
**功能：**    检测转生等级检测英雄等级命令：H.checkrenewlevel
**格式：**
**功能：**
**格式：**;==========================================
H.checkrenewlevel < 9
H.RENEWLEVEL 1
MESSAGEBOX 英雄转生次数已经<$H.RELEVEL>级了！
**功能：**
**格式：**

### 任务脚本
RefreshMissPage 页面名
OpenMissionDlg X坐标 Y坐标

### 沙城主公告


### 设置雕像有效时间[!]
**功能：**
**说明：使用：SetNpcImageTime 设置雕像有效时间，到时间后破碎，时间单位：分钟**
SetNpcImageTime 操作符（=，+，-） 时间（为空，小于或等于0为永久有效，大于0为指定分钟） ，附：不用此命令为无限制时间，因为符合了小于0或等于0或为空
注意此命令只可以在ARP为273的NPC使用！！！！
SetNpcImageTime + 600
SendMsg 5 雕像维护成功，时间增加10小时！

### 神佑袋
| Overlap值 | 位置 |
| --- | --- |
| 0 | 只允许穿身上 |
| **1** | **只允许穿身上 【基础位置】** |
| **2** | **只允许首饰盒【基础位置】** |
| **4** | **只允许神佑【基础位置】** |
| **8** | **只允许时装首饰盒【基础位置】** |
| **16** | **只允许时装神佑【基础位置】** |
| 25 | 1+8+16；身上+时装首饰盒+时装神佑 |
命令格式：**ShowGodBless** 0/1(0:隐藏;1:显示)  是否时装神佑0/1(0:普通神佑;1:时装神佑)
命令格式：**OpenGodBless** 格子位置(0-11, all) 是否时装神佑0/1(0:普通神佑;1:时装神佑)
命令格式：**CloseGodBless** 格子位置(0-11, all) 是否时装神佑0/1(0:普通神佑;1:时装神佑)
命令格式 …[截断]

### 使用脚本命令解毒[!]
**功能：**
**格式：**
SENDMSG 6 提示：解毒成功！

### 收徒脚本
SENDMSG 6 提示：师傅触发！[@UnMasterEnd1]
SENDMSG 6 提示：徒弟触发！

### 刷新包裹的命令
功能：
示例：
MESSAGEBOX 刷新包裹成功！
MESSAGEBOX 英雄刷新包裹成功！

### 挑战功能
说明:没有等级限制,只在双方面对面,即可挑战,挑战时间5分钟,在挑战时间内没有分出胜负的,直接随机传送.
相关脚本命令:
功能:移动到挑战地图
格式:CHALLENGMAPMOVE 地图名 X Y
功能:没有挑战地图可移动,则退回抵押的物品
格式:GETCHALLENGEBAKITEM
CHECKMAPHUMANCOUNT EM029A =
CHALLENGMAPMOVE EM029A 14 15
EM029B = 0
CHALLENGMAPMOVE EM029B 14
CHECKMAPHUMANCOUNT EM029C = 0
EM029C 14 15
CHECKMAPHUMANCOUNT EM029D =
CHALLENGMAPMOVE EM029D 14 15
EM029E = 0
CHALLENGMAPMOVE EM029E 14
CHECKMAPHUMANCOUNT EM029F = 0
EM029F 14 15
CH …[截断]

### 跳转，延迟
DELAYGOTO 时间(毫秒) 触发字段 换地图是否删除此延时(0或为空时=不删除 1=删除)
DELAYGOTO 20 @火龙珠 表示20毫秒
实例：
GIVEONGROUND 屠龙 5
DELAYGOTO 3

### 卧龙山庄配置
格式: OPENBOOKS 序号(0--5)
说明: 0表示卧龙书页,1-5表示笔迹.
CheckLevelEx > 39
OPENBOOKS 0
MAPMOVE HERO1 215 206
Give 回城卷 1

### 新的公告
SuperMoveMsg 1 251 0 20 100 3 这个是个人屏幕信息~坐标在100|欢迎使用翎风引擎|引擎官方网站：|http://www.lfm2.com#if
SuperMoveMsg 0 251 0 20 200 5 这个是全局屏幕信息~坐标在200|欢迎使用翎风引擎|引擎官方网站：|http://www.lfm2.com
SuperMoveMsg 1 251 0 20 100 3 这个是{个人|253:0:1}屏幕信息~坐标在100，<Text:文字内容{FCOLOR=250;FSIZE=14;FNAME=黑体}>||图片数字测试<ImgNum:9:1234333:-3:0:0>看看效果|| 引擎官方网站：||http://www.lfm2.com
SendNewLineMsg 0 251 0 15 100 10 2 带透明框绘制测试|欢迎使用翎风引擎|官方网站：www.lfm2.com
SendNewLine …[截断]

### 新增触发说明
SENDMSG 0 提示：沙巴克老大<$USERNAME>要换人了
SENDMSG 5 你所在的行会丢失沙巴克
SENDMSG 5 你所在的行会已占领沙巴克
SENDMSG 6 提示：师傅触发！[@UnMasterEnd1]
SENDMSG 6 提示：徒弟触发！
SENDMSG 6 提示：开始挂机！[@StopAutoOnline]
SENDMSG 6 提示：停止挂机！---------------------------------------------------**20170407增加加入行会触发**[@JoinGuild]
SENDMSG 6 你已经加入了<$GUILDNAME>行会！
SendCenterMsg 180 251你已经加入了<$GUILDNAME>行会 0 30

### 新转职业变性脚本
CHECKGAMEGOLD > 19
GAMEGOLD - 20
CHANGEGENDER 0
MESSAGEBOX 对不起，您的元宝已经不足20颗。
CHECKGAMEGOLD > 19
GAMEGOLD - 20
CHANGEGENDER 1
MESSAGEBOX 对不起，您的元宝已经不足20颗。
CHECKJOB warrior
CHECKJOB wizard
CHECKJOB taoist
CHECKGAMEGOLD > 49
GAMEGOLD - 50
CHANGEJOB warrior
ADDSKILL 基本剑术
ADDSKILL 攻杀剑术
ADDSKILL 刺杀剑术
ADDSKILL 半月弯刀
ADDSKILL 野蛮冲撞
ADDSKILL 烈火剑法
ADDSKILL 狮子吼
SKILLLEVEL 基本剑术 + 3
SKILLLEVEL 攻杀剑术 + 3
SKILLLEVEL 刺杀剑术 + 3
SKILLLEVEL  …[截断]

### 怪物颜色修改功能
SetMonColor 地图名 怪物名 颜色(1~255) 时间(秒) 类型(0/1)
| 参数 | 说明 |
| --- | --- |
| 地图名 | 要修改怪物的地图名称 |
| 怪物名 | 要修改颜色的怪物名称 |
| 颜色 | 1-255之间的颜色值 |
| 时间 | 颜色持续时间(秒)，0表示永久有效 |
| 类型 | 0=固定颜色，1=七彩变色 |
CheckMapSameMonCount D2083 火龙教主 > 0
SetMonColor D2083 火龙教主 151 0 1
SendMsg 5 D2083地图的火龙教主已经修改为七彩变色！
CheckMapSameMonCount D2083 火龙教主 > 0
SetMonColor D2083 火龙教主 151 0 0
SendMsg 5 D2083地图的火龙教主已经修改为黄色！
SetMonColorEx 地图名 X Y 范围 怪物名 颜色(1~255)  …[截断]

### 修改人体颜色,改变人体颜色
**功能：**
**说明：SetBodyColor 颜色(1~255) 时间(秒) 类型（0、1） 【时间设置为0则为无限制，类型0或留空为 指定颜色 。1则为转生设置的颜色在人物身体上进行变色】**
SetBodyColor 151 120 0
SendMsg 5 你身体颜色更改为黄色，有效时间120秒！
SetBodyColor 151 120 1
SendMsg 5 你身体颜色更改为七彩变色，有效时间120秒！
SetBodyColor 151 0 1
SendMsg 5 你身体颜色更改为七彩变色，时间为在线永久有效！
H.SetBodyColor 151 0 1
SendMsg 5 你英雄的身体颜色更改为七彩变色，时间为在线永久有效！

### 悬浮式装备信息窗口支持图片显示
格式：<looks:N:X:Y:Z>
说明：N=图片位置；X=X偏移；Y=Y偏移 Z=是否显示物品背景框(0,1)
格式：<NewopUI:N:X:Y>
说明：N=图片位置；X=X偏移；Y=Y偏移
格式：<Img:N:F:X:Y>
格式: <PlayImg:F:N:C:T:X:Y:M>

### 循环脚本
SMALL N1 2000
Inc N1 1
SendMsg 6 > $STR(N1)>
GOTO @111
While N1 < 1000
SendMsg 6 <$STR(N1)>
Inc N1 1
SendMsg 6 aaaaaa

### 烟花脚本实例[!]
SHOWEFFECT 类型(79~86)
Gmexecute showeffect 79
SENDMSG 0 <$USERNAME>在:%m%x:%y处放烟花咯、大家快去欣赏哦。
Gmexecute showeffect 80
SENDMSG 0 <$USERNAME>在:%m%x:%y处放烟花咯、大家快去欣赏哦。
Gmexecute showeffect 81
SENDMSG 0 <$USERNAME>在:%m%x:%y处放烟花咯、大家快去欣赏哦。
Gmexecute showeffect 82
SENDMSG 0 <$USERNAME>在:%m%x:%y处放烟花咯、大家快去欣赏哦。
Gmexecute showeffect 83
SENDMSG 0 <$USERNAME>在:%m%x:%y处放烟花咯、大家快去欣赏哦。
Gmexecute showeffect 84
SENDMSG 0 <$USERNAME>在:%m%x:%y …[截断]

### 一键回收包裹物品[!]
格式：
TakeBagItem 物品名称(支持多个物品) 收取数量 增加元宝值 增加金币值 增加泡点值 增加经验值 变量(保存实际回收的物品数量) 聚灵珠经验(为空或0时不增加聚灵珠经验 1时同时聚灵珠经验) 是否显示提示信息(0或空：显示；1：不显示） 颜色值(空或\*回收所有；0-255回收对应颜色物品,支持多个颜色值) 是否回收极品(为空或0回收；1不回收）是否回收改名(0或空回收;1不回收) 回收指定等级以下物品（0或空不限等级）
TakeBagItem 木剑|布衣(男)|布衣(女) 46 0 0 0 10000 N1 0
SENDMSG 6 成功回收<$STR(N1)>个木剑，布衣(男)，布衣(女)，价格为10000经验
TakeBagItem <$STR(S99)> 46 0 1000 0 0 N99 0
GetListString ..\QuestDiary\装备.txt 0 S1
TakeBagItem <$ST …[截断]

### 英雄攻击触发
H.CHECKCURRTARGETRACE = 0
SENDMSG 6 你的英雄被人物【<$H.CURRRTARGETNAME>】攻击了。使用魔法ID=<$H.CURRRUSEMAGICID> 255 253
H.CHECKCURRTARGETRACE = 1
SENDMSG 6 你的英雄被英雄【<$H.CURRRTARGETNAME>】攻击了。使用魔法ID=<$H.CURRRUSEMAGICID> 255 253
H.CHECKCURRTARGETRACE = 151
SENDMSG 6 你的英雄被分身【<$H.CURRRTARGETNAME>】攻击了。使用魔法ID=<$H.CURRRUSEMAGICID> 255 253
SENDMSG 6 你的英雄被怪物【<$H.CURRRTARGETNAME>】攻击了。使用魔法ID=<$H.CURRRUSEMAGICID> 255 253
H.CHECKCURRTARGETRACE =  …[截断]

### 元宝转账


### 召唤某个玩家到自己身边
**功能：**
**格式：**     RECALLHUMAN

### 召唤指定怪物为宝宝,脚本召唤宝宝
**功能：**
**格式：**RecallMobEx 怪物名称 X坐标 Y坐标 等级 数量 叛变时间 颜色类型(0:固定颜色,1:自动变色) 颜色值(0-255;0不改变颜色)
CHECKSLAVECOUNT < 5
RECALLMOBEX 神兽 <$X> <$Y> 7 5 30 1

### 祝福语脚本


### 转生触发
**功能：**
SENDMSG 6 转生成功了
SENDMSG 6 英雄转生成功了

### 转职业变性脚本
CHANGEGENDER 1
CHANGEJOB Warrior
CHANGEJOB Wizard
CHANGEJOB Taoist

### 装备加速功能
**功能：**
**说明：**

### 装备名称自定义系统
功能：
格式：
SETSCRIPTFLAG 1 1

### 自定义按钮倒计时触发
**功能：**
**格式：**
SetClientBuff WIL文件序号 序号(1~200) 图片序号 倒计时间(-1时按钮，大于0是倒计时) X坐标 Y坐标 文字备注 (开启)
CloseClientBuff 序号(1~200) (关闭命令)
ShowClientBuff 1-200 显示/隐藏(1：显示；0隐藏）
ShowClientBuff 0 显示/隐藏(1：显示；0隐藏）
示例：
ShowClientBuff 0 0
ShowClientBuff 0 1
ShowClientBuff 5 0
ShowClientBuff 5 1
SetClientBuff 支持1-200，点击触发：[@ClientBuffClickX] X表示序号;

### 自定义命令输入参数[!]
MOV N9 0
MOV S9
GOTO @字符过滤
SENDMSG SENDMSG 7 提示：您的金币不足1W。
SENDMSG 7 提示：该信息包含敏感字符
LARGE N9 50
TAKE 金币 10000
SendCenterMsg 180 251 <$USERNAME>:<$STR(S9)> 0 30
INC N9 1
SENDMSG 6 现在N9=<$Str(N9)>, S9=<$Str(S9)>
GOTO @字符过滤

### 自定义使用多级脚本
CHECKVAR HUMAN GJZY = 1 ;检测自己
CHANGEPKPOINT + 500
SENDMSG 7 玩家【<$USERNAME>】杀死了【<$CURRRTARGETNAME>】
M.CHECKLEVELEX > 10 ;检测被杀者等级
CHECKVAR HUMAN GJZY = 1 ;检测自己
M.CHECKVAR HUMAN GJZY = 1 ;检测被杀
CHANGEPKPOINT + 500
SENDMSG 7 玩家【<$USERNAME>】杀死了【<$CURRRTARGETNAME>】
L.CHECKVAR HUMAN GJZY = 1 ;检测杀人者的阵营
CHECKVAR HUMAN GJZY = 1 ;检测自己的阵营
L.CHANGEPKPOINT + 100 ;给杀人者加PK值
L.GAMEGLORY + 2 ;给杀人者加荣誉
SENDMSG 6 你被[<$KILLER>]杀死了![<$KILLE …[截断]

### 自动排列自定义按钮倒计时触发
示例：
SetArrBuff 1 1 1 130 10 3 130 4 测试倒计时功能
SetArrBuff 1 2 1 130 100 10 130 4 测试倒计时功能
SetArrBuff 1 3 1 130 80 10 130 4 测试倒计时功能
SetArrBuff 1 4 1 130 60 10 130 4 测试倒计时功能
SetArrBuff 1 5 1 130 30 10 130 4 测试倒计时功能
SetArrBuff 支持1-200，点击触发: [@ArrBuffClickX]X表示序号 (点击触发，不管是按钮还是倒计时都可以点击触发)