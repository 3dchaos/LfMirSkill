# 摘要：功能操作命令（276 章）


### GetPlayInfo命令使用大全
说明: GetPlayInfo命令使用大全(部分可能无效，按需使用)
GetPlayInfo Name S1
SENDMSG 6 玩家名<$STR(S1)>
GetPlayInfo IDE S1
SENDMSG 6 玩家机器硬盘序列号<$STR(S1)>
GetPlayInfo NIC S1
SENDMSG 6 玩家机器网卡序列号<$STR(S1)>
GetPlayInfo VER S1
SENDMSG 6 当前登录器版本号<$STR(S1)>
GetPlayInfo ID S1
SENDMSG 6 玩家账号<$STR(S1)>
GetPlayInfo IP S1
SENDMSG 6 玩家登录IP<$STR(S1)>
GetPlayInfo IPLOCAL S1
SENDMSG 6 玩家IP所在地<$STR(S1)>
GetPlayInfo Map S1
SENDMSG 6 玩家当前地图编号<$STR(S1)>
GetPlayInfo MapName S1
SENDMSG 6 玩家当前地图描述<$STR(S1)>
GetPlayInfo X N1
SENDMSG 6 玩家当前X坐标<$STR(N1)>
GetPlayInfo Y N1
SENDMSG 6 玩家当前Y坐标<$STR(N1)>
GetPlayInfo H.Dir N1
SENDMSG 6 玩家英雄当前方向<$STR(N1)>
GetPlayInfo Dir N1
SENDMSG 6 玩家当前方向<$STR(N1)>
GetPlayInfo Job N1
SENDMSG 6 玩家当前职业<$STR(N1)>
GetPlayInfo sex N1
SENDMSG 6 玩家性别<$STR(N1)>
GetPlayInfo Hair N1
SENDMSG 6 玩家发型<$STR(N1)>
GetPlayInfo Gold N1
SENDMSG 6 玩家金币数量<$STR(N1)>
GetPlayInfo GameGird N1
SENDMSG 6 玩家灵符数量<$STR(N1)>
GetPlayInfo Level …[截断]

### 技能图标设置命令说明
AddScreenMagicButton 技能ID/技能名称 坐标X 坐标Y
| 参数 | 说明 | 示例 |
| --- | --- | --- |
| 技能ID/技能名称 | 可以使用数字ID或技能名称 | 26 或 "烈火剑法" |
| 坐标X | 图标在屏幕上的X坐标 | 30 |
| 坐标Y | 图标在屏幕上的Y坐标 | 400 |
DelScreenMagicButton 技能ID/技能名称
AddScreenMagicButton 26 30 400
DelScreenMagicButton 26
AddScreenMagicButton 烈火剑法 30 400
AddScreenMagicButton 野蛮冲撞 50 350
AddScreenMagicButton 半月弯刀 80 320
AddToMagicBar 技能ID/技能名称
DelFromMagicBar 技能ID/技能名称
AddToMagicBar 26
DelFromMagicBar 26
AddScreenMagicButton 烈火剑法 30 400
AddScreenMagicButton 野蛮冲撞 60 400
AddScreenMagicButton 半月弯刀 90 400
AddToMagicBar 烈火剑法
AddToMagicBar 野蛮冲撞
DelScreenMagicButton 烈火剑法
DelScreenMagicButton 攻杀剑术
DelFromMagicBar 烈火剑法
DelFromMagicBar 攻杀剑术
SendMsg 5 "已清理所有技能图标"
AddScreenMagicButton 烈火剑法 30 400
AddScreenMagicButton 逐日剑法 60 400
AddScreenMagicButton 半月弯刀 90 400
AddScreenMagicButton 野蛮冲撞 120 400
AddToMagicBar 开天斩
AddToMagicBar 十步一杀

### 怪物标识系统详解与高级应用
SetRangeMonAddByte 地图 X坐标 Y坐标 范围 怪物名称(*代表所有) 标识号(0-9) 值(0-255) 有效时间(秒;0或空为一直有效)
SetRangeMonAddByte self <$X> <$Y> 10 * 0 100
SetRangeMonAddByte self <$X> <$Y> 5 野猪 1 50
M.SetMonAddByte 标识号(0-9) 值(0-255) 有效时间(秒;0或空为一直有效)
M.SetMonAddByte 2 200
M.CheckMonAddByte 标识号(0-9) 比较符号(<,>,=) 检测数值(0-255)
M.CheckMonAddByte 3 > 50
**注意：**必须攻击怪物后才能检测，不能直接读取。
M.GetMonAddByte 标识号(0-9) 保存变量
M.GetMonAddByte 0 N1
SendMsg 5 这个怪物的标识0值是：<$STR(N1)>
M.SetMonAddByte 1 1
M.CheckMonAddByte 1 = 1
Give 金条 1
SendMsg 5 你击杀了精英怪，获得了额外奖励！
SetRangeMonAddByte self <$X> <$Y> 8 白野猪 1 1
SendMsg 5 已标记附近的精英白野猪！
M.CheckMonAddByte 1 = 1
SendMsg 5 你正在攻击一只精英怪！
M.HumanHP - 20 0 0 0 0 1
M.CheckMonAddByte 1 = 1
Give 屠龙 1
SendMsg 5 恭喜！你击杀了精英怪，获得了屠龙！

### 修理沙巴克城墙城门
**功能：**可在任何时间对沙巴克城门和城墙进行修理
RepairWall 1
RepairWall 2
RepairWall 3
SendMsg 6 沙巴克城墙和城门已全部修复.

### 自动穿戴指定物品唯一ID的物品到身上
**功能：**通用物品唯一ID自动穿戴装备到身上
**格式：**AutoTakeOnItemEx 物品唯一ID 穿戴位置
**说明：**自动穿戴指定序列号的物品（佩戴类型要和位置相符合，不能衣服穿到其它位置）
ChangeItemIndex 23123789 1
| 物品位置代码 | 物品位置说明 (所有装备位置参考如下） |
| --- | --- |
| -1 | 升级框 |
| boxitem0-boxitem7 | OK框 |
| 0 | 盔甲 |
| 1 | 武器 |
| 2 | 照明物（蜡烛，此物品属性升级无效） |
| 3 | 项链 |
| 4 | 头盔 |
| 5 | 左手镯 |
| 6 | 右手镯 |
| 7 | 左戒指 |
| 8 | 右戒指 |
| 9 | 护身符 |
| 10 | 腰带 |
| 11 | 鞋子 |
| 12 | 宝石 |
| 13 | 斗笠 |
| 14 | 军鼓 |
| 15 | 马牌 |
| 16 | 盾牌 |
| 17 | 灵玉 |
| 18 | 时装衣服 |
| 19 | 时装武器 |
| 20 | 时装项链 |
| 21 | 时装头盔 |
| 22 | 时装左手镯 |
| 23 | 时装右手镯 |
| 24 | 时装左戒指 |
| 25 | 时装右戒指 |
| 26 | 时装勋章 |
| 27 | 时装腰带 |
| 28 | 时装靴子 |
| 29 | 时装宝石 |
| 30-35 | 首饰盒 |
| 40-51 | 生肖盒 |
| 70-75 | 时装生肖盒 |
| 80-91 | 时装生肖盒 |
| **200-249** | **自定义装备框** |

### 将指定位置物品转换为数据库对应的IDX物品
**功能：**将指定位置物品转换为数据库对应的IDX物品
**格式：**ChangeItemIndex 装备位置 数据库物品Idx
**说明：**该命令可以将指定位置物品的附加属性（含自定义属性）平移到新的物品中
ChangeItemIndex 1 19
| 物品位置代码 | 物品位置说明 (所有装备位置参考如下） |
| --- | --- |
| -1 | 升级框 |
| boxitem0-boxitem7 | OK框 |
| 0 | 盔甲 |
| 1 | 武器 |
| 2 | 照明物（蜡烛，此物品属性升级无效） |
| 3 | 项链 |
| 4 | 头盔 |
| 5 | 左手镯 |
| 6 | 右手镯 |
| 7 | 左戒指 |
| 8 | 右戒指 |
| 9 | 护身符 |
| 10 | 腰带 |
| 11 | 鞋子 |
| 12 | 宝石 |
| 13 | 斗笠 |
| 14 | 军鼓 |
| 15 | 马牌 |
| 16 | 盾牌 |
| 17 | 灵玉 |
| 18 | 时装衣服 |
| 19 | 时装武器 |
| 20 | 时装项链 |
| 21 | 时装头盔 |
| 22 | 时装左手镯 |
| 23 | 时装右手镯 |
| 24 | 时装左戒指 |
| 25 | 时装右戒指 |
| 26 | 时装勋章 |
| 27 | 时装腰带 |
| 28 | 时装靴子 |
| 29 | 时装宝石 |
| 30-35 | 首饰盒 |
| 40-51 | 生肖盒 |
| 70-75 | 时装生肖盒 |
| 80-91 | 时装生肖盒 |
| **200-249** | **自定义装备框** |

### 获取武器修炼次数
**功能：**获取武器修炼次数，检测装备修炼次数，修改武器修炼次数
**格式：**GetItemTrainingCount 装备位置 保存变量
**说明：**获取武器修炼次数，检测装备修炼次数，修改武器修炼次数
命令格式：ChangeItemTrainingCount 装备位置 操作符(+-=) 修炼次数
GetItemTrainingCount 装备位置 保存变量
格式:CheckItemTrainingCount 物品位置 (<,>,=) 修炼次数
CheckItemTrainingCount 1 < 4
ChangeItemTrainingCount 1 + 1
GetItemTrainingCount 1 N1
Sendmsg 6 你装备的武器修炼次数为<$STR(N1)>

### 查看人物/英雄装备
**功能：**查看人物/英雄装备
**说明：**一共两条命令,其中无论目标人物是否在线均可查看,按需使用
功能：查看在线人物/英雄装备
格式：QueryUserState 用户名/英雄名
说明：当用户/英雄不在线时，会触发 当前Npc 中的@QueryUserStateFail
QueryUserState dddd
功能：查看人物/英雄装备（无论是否在线均可查看）
格式：QueryUserStateEx 用户名/英雄名
说明：当用户不存在时，会触发 当前Npc 中的@QueryUserStateExFail
QueryUserStateEx dddd

### 取两个时间之间的相差
**功能：**取两个时间之间的相差（时间2-时间1）
**说明：** GETINTERVAL 时间1 时间2 (0:年 1:月 2:星期 3:天 4:时 5:分 6:秒) 保存变量
功能: 取两个时间之间的相差（时间2-时间1）
格式: GETINTERVAL 时间1 时间2 (0:年 1:月 2:星期 3:天 4:时 5:分 6:秒) 保存变量
GETINTERVAL <$datetime> <$YEAR>-<$MONTH>-<$DAY>,23:59:59 6 S$时间
SENDMSG 0 距离当天结束还剩余<$STR(S$时间)>秒
注意：服务器的时间格式修改为:yyyy-M-d,否则会提示该命令的时间格式错误

### 毫秒级个人定时器
**功能：**毫秒级个人定时器
**说明：** 由于人物运行间隔在200毫秒+，计时器在250毫秒内可能无法做到很精确
格式：
SETONTIMEREX 定时器索引(0-9) 定时间隔（单位为毫秒）执行次数（留空为无限制执行，需使用停止定时器方可关闭，填写3为执行3次后自动关闭定时器）
SETOFFTIMEREX 定时器索引(0-9) //停止定时器
SETONTIMEREX 0 300
SENDMSG 1 OnTimerEx0
SETOFFTIMEREX 0

### 忽视目标防御
**功能：**同时忽视目标防御和魔御
**说明：**本命令支持按照数值或百分比同时忽视目标防御和魔御，当和元素忽视目标防御冲突时，优先命令操作后的防御属性再进行元素忽视
格式：SetIgnoreTargetDefense 值类型(0:百分比;1:固定值) 值 时间(单位秒,0为在线一直有效)
SetIgnoreTargetDefense 1 80 20
SENDMSG 6 忽视目标防御80点，20秒有效
SetIgnoreTargetDefense 0 50 10
SENDMSG 6 忽视目标防御50%，10秒有效

### 调整人物属性百分比
**功能：**调整人物属性百分比
**格式：**ChangeHumAbilityPercentage 属性(1-29) 操作符(+ = -) 数值 时间秒
说明: 属性1-29分别对应值
ChangeHumAbilityPercentage 2 + 10 60
M.ChangeHumAbilityPercentage 2 = 90 10

### 改变技能特效
**功能：**改变技能特效
**格式：**无
**说明：**持久性技能特效暂未支持
SetMagicEffect 雷电术 33
Sendmsg 6 雷电术变为冰咆哮特效了
SetMagicEffect 火球术 11
Sendmsg 6 火球术变为雷电术特效了
SetMagicEffect 刺杀剑术 66
Sendmsg 6 刺杀剑术变为开天斩特效了
SetMagicEffect 烈火剑法 25
Sendmsg 6 烈火剑法变为半月特效了

### 开启跑步幻影效果
**功能：**幻影移动
**格式：**SetShadowShow 开启/关闭(1:开;0:关) 开启时间(单位:秒；为0时表示在线一直生效)
格式：SetShadowShow 开启/关闭(1:开;0:关) 开启时间(单位:秒；为0时表示在线一直生效)
示例：
SetShadowShow 1 60

### 设置假人捡物品列表
**功能：**设置假人捡物品列表
格式：自定义设置假人捡物品列表
SetDummyPickItemFile 捡取列表文件名(一行一个物品名) 是否优先捡取(0或空：优先捡取列表;1:允许捡取列表）
SetDummyPickItemFile D:\假人捡垃圾1.txt
SetDummyPickItemFile D:\假人捡垃圾2.txt 1

### 开启关闭假人捡物品功能
**功能：**开启/关闭假人捡物品功能
格式：开启/关闭假人捡物品
SetDummyPickItem 1/0(1:开假人捡物; 0:关假人捡物)
SetDummyPickItem 1

### 获取身上物品限时剩余时间
**功能：**获取身上限时物品剩余时间
**获取身上物品限时剩余时间格式：**GetItemRemainingTime 物品位置 保存变量(为-1时，表示非限时装备)
**获取身上称号限时剩余时间格式：**GetFengHaoRemainingTime 称号名称 保存变量(为-1时，表示非限时装备)
格式：GetItemRemainingTime 物品位置 保存变量(为-1时，表示非限时装备)
GetItemRemainingTime 1 N1
CheckUseItem 1
GetItemRemainingTime 1 N1
SendMsg 6 武器剩余时间为：<$STR(N1)>分钟
格式：GetFengHaoRemainingTime 称号名称 保存变量(为-1时，表示非限时装备)
GetFengHaoRemainingTime 沙巴克城主 N1
CheckFengHao 沙巴克城主
GetFengHaoRemainingTime 沙巴克城主 N1
SendMsg 6 沙巴克城主剩余时间为：<$STR(N1)>分钟

### 交易前触发
**功能：**交易前触发和中止交易
**格式：**交易前触发@BeginDealTry
**说明：**中止交易命令StopDealTry
格式：简易例子
SendMsg 6 脚本禁止交易

### 键值对字典
功能说明: 字典
格式：{key1:value1,key2:value2}
GetDictKeyCount 字典名 变量
GetDictItems 字典名 字段类型(0:Keys;1:Values) 保存变量
GetDictMaxValue 字典名 Key变量 Value变量
GetDictMinValue 字典名 Key变量 Value变量
CheckDictAllDigit 字典名
;格式：CheckInDict 字典变量 待检查的值 参数3
MOV D$测试 {张三:100,李四:200,王五:300}
Mov D$测试[周八] 600
Inc D$测试 赵六:400
Inc D$测试 孙七:500
Dec D$测试 赵六
GetDictKeyCount D$测试 N1
GetDictItems D$测试 0 L$Keys
GetDictItems D$测试 1 L$Values
CheckInDict D$测试 张三 0
SendMsg 7 Key:张三在字典中
CheckInDict D$测试 200 1
SendMsg 7 Value:200在字典中
CheckDictAllDigit D$测试
GetDictMaxValue D$测试 S1 N1
GetDictMinValue D$测试 S1 N1
MOV D$测试 {}

### 通过技能ID获取技能数据库字段
**功能：**通过技能ID获取技能数据库字段
**格式：**GetDBMagicIDFieldValue 技能ID 字段名 保存变量
**说明：**GetDBMagicIDFieldValue 技能ID 字段名 保存变量
格式：GetDBMagicIDFieldValue 技能ID 字段名 保存变量
GetDBMagicIDFieldValue <$CURRRUSEMAGICID> 元素技能变量 s$元素技能变量值
GetDBMagicIDFieldValue <$CURRRUSEMAGICID> 攻元素怪物对应元素 S$怪物对应元素
GetDBMagicIDFieldValue <$CURRRUSEMAGICID> 攻元素人物对应元素 S$人物对应元素

### 伤害吸收装备设置
**功能：**使用脚本命令开启行会战命令
**格式：**如需掌门人才可以用的话请加入检测脚本命令
**说明：**GuildWar 参数1(目标行会名字) 任何有行会的玩家都可以使用(无行会则无效)
GuildWar 测试测试

### 获取宝宝所在位置信息
**功能说明: 获取宝宝所在位置**
格式：GetSlavePosition 名字 保存变量Map 保存变量X 保存变量Y 是否只匹配显示名(0不检测数字 1检测数字)
GetSlavePosition 神兽 S$地图 N$X坐标 N$Y坐标
Sendmsg 5 提示：您的神兽在<$STR(S$地图)>坐标(<$STR(N$X坐标)>,<$STR(N$Y坐标)>)

### 打印个人标识
**功能说明: 打印个人标识**

### 设置物品悬浮框背景特效
功能说明:
说明：设置物品悬浮框背景特效
SetItemWindowEffectIndex 物品位置 特效位置(0-2) 特效编号(0为关闭)
SetItemWindowEffectIndex 1 0 1
SetItemWindowEffectIndex 1 1 3
SetItemWindowEffectIndex 1 2 10

### 获取全身装备的原始数据字段合计值
功能说明:
说明：获取全身装备的原始数据字段指定值总和
格式：
GetAllDBItemFieldValue 字段名 变量
示例：
GetAllDBItemFieldValue LFM2 N1
SendMsg 6 提示:你身上装备LFM2字段值总和共有<$STR(N1)>点！

### 不掉落身上装备
功能说明:
说明：不掉落身上装备（含背包物品）
SetNoDropItemCount (+,-,=) 次数 下线是否保存 爆出选项(0:身上及背包都不会爆出；1时:仅身上装备不爆出)
GetNoDropItemCount 变量1(次数) 变量2(下线是否保存,0或空不保存)
SetNoDropItemCount = 5 1
SendMsg 6 你有5次机会死亡不掉任何装备
GetNoDropItemCount N1 N2
Sendmsg 6 你有<$STR(N1)>次机会死亡不掉装备；下线是否保存:<$STR(N2)>
H.SetNoDropItemCount (+,-,=) 次数 下线是否保存 爆出选项(0:身上及背包都不会爆出；1时:仅身上装备不爆出)
H.GetNoDropItemCount 变量1(次数) 变量2(下线是否保存,0或空不保存)
H.SetNoDropItemCount = 5 1
SendMsg 6 你英雄有5次机会死亡不掉装备
H.GetNoDropItemCount N1 N2
Sendmsg 6 你英雄有<$STR(N1)>次机会死亡不掉装备；下线是否保存:<$STR(N2)>

### TAKE收回背包物品
功能说明:
格式：take 物品 数量 是否检测装备改名（0或空：不检测，1：检测） 物品名匹配方式(0或空：完整匹配，1：部分匹配） 是否回收自定义OK框物品(0或空:回收; 1:不回收) 检测持久(0或空:所有; -1:满持久; -2:未持久)
示例：
SENDMSG 6 收回背包物品：大手镯，数量：1

### 删除仓库物品
功能说明:
说明：DelStorageItem 仓库类型(0:普通仓; 1:无限仓) 依据值的类型(0:物品唯一ID; 1:物品数据Idx; 2:物品名称) 值
格式：DelStorageItem 仓库类型(0:普通仓; 1:无限仓) 依据值的类型(0:物品唯一ID; 1:物品数据Idx; 2:物品名称) 值
示例：
DelStorageItem 0 1 0
DelStorageItem 1 2 屠龙
DelStorageItem 0 2 \*

### 获取仓库物品数量
功能说明:
格式：GetStorageItemCount 仓库类型(0:普通仓; 1:无限仓) 依据值的类型(0:物品唯一ID; 1:物品数据Idx; 2:物品名称) 值 变量
格式：GetStorageItemCount 仓库类型(0:普通仓; 1:无限仓) 依据值的类型(0:物品唯一ID; 1:物品数据Idx; 2:物品名称) 值 变量
示例：
GetStorageItemCount 0 1 0 N1
GetStorageItemCount 1 2 屠龙 N1
GetStorageItemCount 0 2 \* N1

### MobFireBurn地图光环效果
功能说明:
格式：MOBFIREBURN 地图号 坐标X 坐标Y 光环效果 持续时间(秒) 伤害值 是否百分比（0或空为值 ，1为MAXHP百分比， 2为当前HP百分比）
格式：MOBFIREBURN 地图号 坐标X 坐标Y 光环效果 持续时间(秒) 伤害值 是否百分比（0或空为值 ，1为MAXHP百分比， 2为当前HP百分比）
示例：
MOBFIREBURN 3 320 348 5 60 50 2
MOBFIREBURN 3 320 349 5 60 50 2
MOBFIREBURN 3 320 350 5 60 50 2
MOBFIREBURN 3 320 351 5 60 50 2
MOBFIREBURN 3 321 348 5 60 50 2
MOBFIREBURN 3 321 349 5 60 50 2
MOBFIREBURN 3 321 350 5 60 50 2
MOBFIREBURN 3 321 351 5 60 50 2
SendMsg 0 盟重开火墙，有效1分钟，每次掉剩余血量一半的血

### GM命令刷怪
功能:

### GOTO将传递参数返回值保存到变量，脚本参数回调
MOV S$计算结果 参数2返回值：<$str(N$计算结果2)>

### HumanHP调整血量
格式: HumanHP 参数1 参数2 参数3 参数4 参数5 参数6 参数7 参数8
参数1 操作符号(+ - =)
参数2 数值
参数3 延时扣血 (空或0表示无延时，延时单位：毫秒)
参数4 执行次数（0或或空扩展之前老模式，设置1为新模式执行1次 ，注：新模式如多条命令一起执行扣血会一起扣 漂血会叠加飘）
参数5 是否漂血 (0或空为默认漂血，1为不漂血 ，参数6大于0时本项无效)
参数6 是否自定义漂血（瓢血前缀 ：0或空为无前缀，自定义瓢血填写为NewopUI.pak中的图片编号，比如填写1810 此次瓢血采用1810-1827）参数6值大于0则按照参数6设置进行漂 参数等于0或空则按照参数5设置是否漂血）
参数7 数据单位(0:固定值，1:MaxHP%，2:MaxHP‰，3:MaxHP?)
参数7补充说明：0或空为按照参数2设置的数据值进行扣血，参数为1则按照参数2设置的值进行百分比扣血，参数为2千分比，参数为3万分比...设置万分之100也等于百分之一）
参数8 是否无视目标护身属性,参数设置0或留空为无视，1为目标护身有效
HumanHP - 500 300
HumanHP - 100 0 1 0 1810 3
HumanHP - 1 0 1 0 1810 2
HumanHP - 1 0 1 0 1810 1
HumanHP - 1000 0 1 0 1810
MP格式:
HumanMP 操作符(+ - =) 数值 微秒延时时间(空或0表示无延时) 执行次数（0或或空扩展之前老模式，设置1为新模式执行1次 ，注：新模式如多条命令一起执行扣蓝会一起扣 漂蓝会叠加飘） 比例值(0:数值；1:MaxMP%; 2:千分之MaxMP; 3万分之MaxMP)
HumanHP - 500 1000
HumanHP - 500 2000
HumanHP - 500 3000
HumanHP - 500 4000
HumanHP - 500 5000
HumanHP - 500 5000 5

### Mongen.txt 增加刷怪触发
**功能：**
Mongen.txt 刷怪触发
**格式：**
Mongen.txt 增加刷怪触发
Mongen.txt 文件内容如下：
SENDMOVEMSG 0 251 0 50 1 {【世界BOSS全服提示】:/SCOLOR=70}{『<$RegMonName>』/SCOLOR=250}已出世，位于地图<$RegMonMap>(<$RegMonMapDesc>)，坐标<$RegMonX>:<$RegMonY>，赶紧抢！！！
Mongen.txt 文件内容如下：
SENDMOVEMSG 0 251 0 50 1 {【世界BOSS全服提示】:/SCOLOR=70}{『<$RegMonName>』/SCOLOR=250}已出世，位于地图<$RegMonMap>(<$RegMonMapDesc>)，坐标<$RegMonX>:<$RegMonY>，赶紧抢！！！

### Npc命令捡物同步内挂物品，同步内挂捡取
说明：Npc命令捡物同步内挂物品
说明：
参数0为根据引擎选项决定是否开启同步内挂捡
EnableUseClientPickItems 1
SENDMSG 6 你已开启同步内挂捡物
EnableUseClientPickItems 2
SENDMSG 6 你已关闭同步内挂捡物
H.EnableUseClientPickItems 1
SENDMSG 6 你的英雄已开启同步内挂捡物
H.EnableUseClientPickItems 2
SENDMSG 6 你的英雄已关闭同步内挂捡物
PET.EnableUseClientPickItems 1
SENDMSG 6 你的宠物已开启同步内挂捡物
PET.EnableUseClientPickItems 2
SENDMSG 6 你的宠物已关闭同步内挂捡物

### 按地图列表移动


### 按给定概率随机获取分割后的字符串
格式：RandomSplit 参数1 参数2 参数3 参数4(可为空) 参数5(可为空)
参数1：需要获取随机的字符串 字符串#概率|字符串#概率 字符串分割符“|” (字符串顺序无要求)
参数2：0~2（0=参数2返回“字符串” 1=参数2返回“概率值” 2=参数2返回“字符串#概率值”）
参数3：随机得到的结果所保存的变量
参数4：0~2（0=参数4返回“字符串|字符串|字符串” 1=参数4返回“概率值|概率值|概率值” 2=参数4返回“字符串#概率值|字符串#概率值”）
参数5：剩余的结果所保存的变量
示例：
RandomSplit 木剑#2|裁决#1|怒斩#3|屠龙#5 0 S$结果 2 S$剩余
SENDMSG 6 随机取到字符串：<$str(S$结果)>
SENDMSG 6 剩余的字符串值：<$str(S$剩余)>

### 把行会加入攻城列表
格式: ADDTOCASTLEWARLIST 城堡名称 行会名称(行会名称为空时所有行会加入到攻城列表) 天数(几天后开始攻城，该参数可以为空，为空时按照引擎设置的天数)
ADDTOCASTLEWARLIST 沙巴克 1

### 把人物加入行会
格式: ADDGUILDMEMBER 行会名称 人物名称(人物名称为空时把自己加入到行会)
ADDGUILDMEMBER 行会名称

### 百分比计算命令[!]
**功能：**
格式: CalcPercent 值 百分比 结果变量
CalcPercent 200 5 N1
SendMsg 6 200的5%为<$STR(N1)>

### 绑定给予的装备进行命令操作
ChangeItemNameColor -1 253
说明：linkpickupitem和linkgiveitem都是绑定对象到升级框，调整属性后刷新-1位置即可！
注意：clearLinkItem 因为绑定必须给物品一个位置，目前以下2个命令强行绑定到OK框，请加上解除绑定命令，不然不能及时刷新背包物品属性，需要小退生效，加上后及时生效！！

### 宝宝攻击触发
说明: 宝宝攻击触发
SENDMSG 6 你的宝宝被魔法攻击了
SENDMSG 6 你的宝宝魔法攻击了目标
SENDMSG 6 你的宝宝被物理攻击了
SENDMSG 6 你的宝宝物理攻击目标
SendMsg 5 当前攻击宝宝名为<$CurSlaveName>
EQUAL <$CurSlaveName> 蜈蚣
SENDMSG 6 你的蜈蚣宝宝在攻击目标
EQUAL <$CurSlaveName> 骷髅
SENDMSG 6 你的骷髅宝宝在攻击目标
SENDMSG 6 宠物被攻击，掉血量为<$Pet.DamageValue>，抵御掉血量的50%
Pet.ChangeDamageValue 1 - 50
ChangeDamageValue 1 - 50
SENDMSG 6 你的宝宝攻击【<$CURRRTARGETNAME>】。，锁定目标<$ATTACKMONSTER\_NAMEEX>。坐标：<$ATTACKMONSTER\_X>:<$ATTACKMONSTER\_Y>掉血量为<$DamageValue>
ChangeDamageValue 0 + 10

### 宝宝死亡触发
格式: 宝宝死亡触发qf字段：@OnSlaveDie
格式: 分身死亡触发qf字段：@OnCloneDie

### 编组地图传送
GROUPMAPMOVE 地图号 X Y 可以传送最低等级(可以为空，为空时不检测队员的等级直接传送) 触发字段(可以为空) 范围（以队长为中心设置范围，只传送范围内的队友，留空或者0为不需要范围，大于0则按照范围传送）
GROUPMAPMOVE 3 333 333 @GROUPMAPMOVE
SENDMSG 6 组队传送
相关命令：

### 编组地图随机传送
GROUPMOVE 地图号 可以传送最低等级(可以为空，为空时不检测队员的等级直接传送) 触发字段(可以为空) 范围（以队长为中心设置范围，只传送范围内的队友，留空或者0为不需要范围，大于0则按照范围传送）
GROUPMOVE 3 @GROUPMOVE
SENDMSG 6 组队传送
相关命令：

### 变量传递说明
SetHumVar 对方的名字 对方的变量 值
GetHumVar 对方的名字 对方的变量 自己的变量
SetHumVar S1 S2 <$MAXAC>
SENDMSG 6 成功把你的防御力数值传递给对方的S2变量，对方已知道你的防御力多少
GetHumVar S3 <$MAXAC> S4
SENDMSG 6 你已成功取得对方防御力为<$STR(S4)>

### 播放地图魔法特效（仅自己可见）
格式: SelfMapEffect 地图名称 X Y WIL文件序号 开始图片数 播放图片张数 播放次数(-1为无限次数) 播放速度(毫秒) 播放效果(0普通 1特效) (该参数值范围0~5，0表示没有亮度，在关闭禁止免蜡时有效) ID
SelfMapEffect 3 330 330 1 10 20 1 200 1 3 1

### 播放人物效果
格式: PLAYEFFECT WIL文件序号 开始图片数 播放图片张数 播放次数（★ <=0 为永久播放 ★） 播放速度(毫秒) 播放顺序(0或空：对象上层 1：对象底层 2：所有对象上层) X坐标 Y坐标 （不需坐标可留空） 普通播放或特效播放(0或空：特效播放；非0普通播放
PLAYEFFECT 0 0 10 1 300 1
格式: StopPlayEffect WIL文件序号 开始图片数 播放图片张数 播放次数 播放速度(毫秒) 播放顺序(0或空：在角色前面；非0：在角色后面)
StopPlayEffect 0 0 10 1 300 1

### 播放网络MP3
说明: 播放网络上的MP3文件,或者本地MP3文件.
格式:
PlayMP3 <http://www.lfm2.com/123.mp3>
注意: 如果是本地文件会自动搜索客户端Music目录中同名文件.
PlayMusicEx格式：
PlayMusicEx 文件 循环次数 模式(0:自己;1:所有人;2:当前地图人;3:队友;4:自己周边的人) 参数4
PlayMusicEX 歌1.MP3 1 0 1

### 播放音乐
格式: playsound 文件位置 循环次数（设置次数0为无限次数） 播放模式(0播放给自己,1播放给全服,2播放给同一地图,,4播放给同屏人物)
PLAYSOUND Wav\1.wav 1 0
格式: playsoundExt 文件位置 循环次数（设置次数0为无限次数） 播放模式(0播放给自己,1播放给全服,2播放给同一地图,,4播放给同屏人物)

### 称号系统
**功能：**
**格式：**
SETRANKLEVELNAME  %s称号
SETRANKLEVELNAME  %s[称号]

### 创建文件
格式: CREATEFILE 文件名称
CREATEFILE ..\QuestDiary\名称列表.txt

### 从文件中随机取文本
**功能：**
**格式：**    GETRANDOMLINETEXT 文件 字符串变量 指定行(0或空：随机一行；大于0：取指定行；小于0：取倒数第几行) 是否绝对路径(0:不是；1：是)
GetRandomLineText d:\aaa.txt S1 -1 1
SendMsg 4 d:\aaa.txt中倒数第1行内容为：<$STR(S1)>
GetRandomLineText d:\aaa.txt S1 -3 1
SendMsg 4 d:\aaa.txt中倒数第3行内容为：<$STR(S1)>
GETRANDOMLINETEXT ..\QuestDiary\装备列表.txt <$STR(S0)>

### 从指定文件中删除字符串[!]
**功能：**
**格式：**    AddTextList 文件位置 字符串 是否绝对路径(0:不是，1：是)
DelTextList 文件位置 字符串
AddTextList ..\QuestDiary\TestList.txt 您的名字
AddTextList ..\QuestDiary\TestList.txt 您的名字 您的性别
DelTextList ..\QuestDiary\TestList.txt 您的名字
DelTextList ..\QuestDiary\TestList.txt 您的名字 您的性别
DELTEXTLIST E:\哈哈.txt <$USERID> 30 1
DELTEXTLIST E:\哈哈.txt <$USERID> "" 1

### 打开NPC大对话框[!]
功能说明：打开NPC大对话框
格式: OPENMERCHANTBIGDLG WIL文件序号 图片序号 是否可以移动(0,1) 显示位置(0=左上角,1=右上角,2=左下角,3=右下角,4=居中) 微调坐标X 微调坐标Y 是否显示关闭按钮(0,1) 关闭按钮坐标X 关闭按钮坐标Y 是否当前NPC对话一直使用此对话框(0和空为不延续，1则延续)
OPENMERCHANTBIGDLG 0 0

### 打开OK对话框
格式: OPENUPGRADEDLG 显示的名称
OPENUPGRADEDLG 装备升级(显示的名称)
OPENUPGRADEDLG 装备升级(显示的名称)
SetNewItemValue -1 0 + 10

### 打开摆摊（个人商店）脚本命令


### 打开自定义NPC对话框
功能说明:
说明：使用OpenBigDialogBox命令创建自定义NPC对话框
**命令格式**
OpenBigDialogBox 参数如下：
参数1：WIL文件序号
参数2：图片序号
参数3：是否可以移动
参数4：对话框在屏幕上的显示位置（0:左上角; 1:右上角; 2:左下角; 3:右下角; 4:居中)
参数5：对话框微调坐标X
参数6：对话框微调坐标Y
参数7：是否显示关闭按钮（不需要显示则需要填写0，显示为1）
参数8：关闭按钮 X
参数9：关闭按钮 Y
示例脚本：
Mov N$UI\_N 24
OpenBigDialogBox <$STR(N$UI\_N)> 0 1 0 0 0 1 590 26
OpenBigDialogBox 8 109 1 4 0 0 1 530 0

### 地图缩小，吃鸡
格式: SetMiniMapRange 参数1(地图编号) 参数2(点类型) 参数3(坐标点/中心点) 参数4(半径) 参数5(填色模式) 参数6(填色色号(0-255)) 边界类型 有效时间
SetMiniMapRange 参数1(地图编号) 参数2(点类型) 参数3(坐标点/中心点) 参数4(半径) 参数5(填色模式) 参数6(填色色号(0-255)) 边界类型 有效时间
SetMiniMapRange 3 0 130:330;330:130;530:330;330:530 100 1 249 2 180
SENDMSG 5 在小区域里
SENDMSG 5 在小区域外

### 读写配置项,读写ini配置项
说明：读写ini配置项
说明：
WriteConfigFileItem 写配置项 （最后加个参数 1为绝对路径，，0或者留空为默认的相对路径)
功能说明：可以把一些数据进行配置保存 你也可以把它当成一种变量保存方式
ReadConfigFileItem 读配置项 （最后加个参数 1为绝对路径，，0或者留空为默认的相对路径)
功能说明：获取出配置文件中的配置项内容
示例：
WriteConfigFileItem ..\QuestDiary\KEY.txt <$USERNAME> 内容 <$STR(S3)>
SENDMSG 6 你已经把你输入的内容写到配置文件中KEY.txt
ReadConfigFileItem ..\QuestDiary\KEY.txt <$USERNAME> 内容 <$STR(S$配置项内容)>
SENDMSG 6 你已经把配置文件KEY.txt中的内容获取出
GOTO @main
DelConfigFileItem 文件名 设置 用户 （删除 用户 = aaaa 这一行）
DelConfigFileSection 文件名 设置 （删除 [设置] 及设置以下的项）

### 多元数组元素变量
**功能说明: 多元数组 or 元素变量**
MOV L$测试 [11,22,33,44,55,66,77,aa]
MOV L$测试[0] 00
INC L$测试 bb
Dec L$测试 22
Mov L$测试2 [aa,bb,cc]
Mov L$测试[0] <$str(L$测试2)>
GetListVarIndex L$测试 aa N1
GetListVarCount L$测试 N1
CheckVarInList L$测试 bb
Mov N1 1
MOV L$测试[<$Str(N1)>] 23
MOV L$测试 [1,2,3,4,5,a]
MOV L$测试[0] b
MOV N$id 0
MOV L$测试[<$STR(N$ID)>] c
MOV N$id 1
INC L$测试[<$str(N$id)>] 第2个元素增加内容
注意：指定参数必须是变量名的暂不支持变量嵌套
MOV L$变<$str(N$当前行数)>量 [赋值内容,赋值内容2]
MOV L$测试 [11,22,33,44,55,66,77,aa]
Mov L$测试 []
MOV L$测试 [1,2,3] ;----赋值123
MOV L$测试 ;------清空
**注意：**
MOV L$测试 [1,2,3]
SENDMSG 6 <$scriptparam1>---显示为[1,2,3]
CheckListAllDigit 元素变量
MOV L$测试 [11,22,33,44,55,ff]
CheckListAllDigit L$测试
GetListMaxVar 元素变量名 保存变量
GetListMinVar 元素变量名 保存变量
MOV L$测试 [11,22,33,44,55,66,77,88]
CheckListAllDigit L$测试
GetListMaxVar L$测试 S100
GetListMinVar L$测试 S101
ReverseList 元素变量名 保存元素变量
MOV L$测试 [11,22,33,44,55,66,77,aa]
ReverseList L$测试 L$测试
So …[截断]

### 发送屏幕滚动信息
功能:
格式:
SENDMOVEMSG 信息类型代码(0-7)0全局发送1发送给个人 字体颜色(0-255) 背景颜色(0-255) Y坐标 滚动次数 信息内容 字体大小 滚动速度 范围
SENDMOVEMSG 1 253 255 350 1 这个是屏幕滚动信息坐标在350 10 200 0
SENDMOVEMSG 0 253 0 130 5 {[双倍护送]/SCOLOR=251}振威镖局接镖已经开启{[双倍护送]/SCOLOR=251}，请各位玩家前往镇魔大陆请各位玩家前往镇魔大陆{[双倍护送]/SCOLOR=251}XXXXX..... 0 2 30 0

### 发送屏幕中间大字体信息
功能: 在专用登录器屏幕的中间显示公告.
格式: SendCenterMsg 前景色 背景色 消息文字 模式 显示时间 倒计时标签 是否替换模式（0或空为不替换，不等于0为替换模式) X坐标
说明: 设置倒计时标签时可执行自定义脚本功能.
SendCenterMsg 180 251 这是一个居中显示的公告. 0
SendCenterMsg 180 251 这是一个居中显示的公告. 0 30
SendCenterMsg 180 251 还剩余%d发放新手奖励. 0 30 @GiveNewHumanItem
Give 金条 1
Give 裁决之杖 1
Give 圣战戒指 2
Give 圣战手镯 2
Give 圣战头盔 1
Give 圣战项链 1
Give 天魔神甲 1
SuperMoveMsg 1 251 0 20 100 3 这个是个人屏幕信息~坐标在100||欢迎使用翎风引擎|| 引擎官方网站：||http://www.lfm2.com#if
SuperMoveMsg 0 251 0 20 200 5 这个是全局屏幕信息~坐标在200||欢迎使用翎风引擎|引擎官方网站：||http://www.lfm2.com
SendNewLineMsg 0 251 0 15 100 10 2 不带透明框绘制测试||欢迎使用翎风引擎||官方网站：www.lfm2.com
SendNewLineMsg 0 251 0 15 100 10 0 带透明框绘制测试||欢迎使用翎风引擎||官方网站：www.lfm2.com
SendNewLineMsg 0 251 0 15 100 10 1 淡入淡出绘制测试||欢迎使用翎风引擎||官方网站：www.lfm2.com
SuperMoveMsg 1 251 0 20 100 3 这个是{个人|253:0:1}屏幕信息~坐标在100||欢迎使用翎风世界引擎|| 引擎官方网站：||http://www.lfm2.com

### 发送文字信息
功能：
格式：
SENDMSG 信息类型代码 %s信息内容%d 字体颜色(0-255) 背景颜色(0-255)
命令格式：
SENDMSG 0
SENDMSG 1 %s信息内容%d 249 47
SENDMSG 2 %s信息内容%d 249 47
SENDMSG 3
SENDMSG 4 %s信息内容%d
SENDMSG 5 %s信息内容%d 249 47
SENDMSG 6
SENDMSG 7 %s信息内容%d 249 47
SENDMSG 8 信息内容

### 返回OK框中的物品
格式: RECLAIMITEM

### 分割字符串[!]
**功能：**
格式: TextSplit 分割符 源字符串 保存变量(只指定第一个，后面的递增) 返回分割数量
TextSplit | aaa|bbb|ccc|ddddd|eeeeee s1 N$数量
SENDMSG 6 <$STR(s1)>,<$STR(s2)>,<$STR(s3)>,<$STR(s4)>,<$STR(s5)> ,分成了<$str(N$数量)>个变量

### 复活命令
说明: 给予角色有限时间的复活功能(此命令不受复活间隔控制，可以按照设置参数无限复活，按需使用)
格式：
参数一 复活次数
参数二 命令持续有效时间
Setreborn 10 300
SendMsg 6 npc设置复活10次，有效时间5分钟
SendMsg 6 命令剩余复活次数：<$NpcRebornCount>，已使用复活次数<$TriggerNpcRebornCount>

### 复活人物
格式: REALIVE

### 复制文件
格式: CopyFile 源文件 目标文件 是否覆盖目标(强制创建并覆盖目标文件 1:目标文件已存在不覆盖)
CopyFile ..\QuestDiary\列表.txt D:\列表.txt 0

### 改变宝宝名字颜色
功能: 改变人物宝宝名字颜色.
格式:
ChangeSlaveNameColor 宝宝名字 颜色(0-255)

### 改变人物状态
格式: MAKEPOSION 类型(0-5,0和1是绿毒和红毒 5是麻痹 其他无效) 时间(秒) 威力 是否算防御目标的对应属性(1/0) 是否**千分比**计算威力(1/0)
MAKEPOSION 5 10 10
MAKEPOSION 1 10 50 1
SENDMSG 6 防御减少50点
MAKEPOSION 0 10 50 1
SENDMSG 6 中毒了，每次伤害值50点
MAKEPOSION 1 10 50 1 1
SENDMSG 6 防御减少5%or千分之五十
MAKEPOSION 0 10 10 1 1
SENDMSG 6 中毒了，每次伤害值1%or千分之十

### 高等级杀怪经验不变
格式:HighLevelKillMonFixExp 时间 是否保存（1保存，空或0不保存）
HighLevelKillMonFixExp 720 1

### 隔位野蛮冲撞
格式：SetSpaceMotaebo 时间(-1:关;0:在线一直有效;>0:秒)
SetSpaceMotaebo 3

### 个人定时器
**功能：**
**格式：**    SETONTIMER 定时器索引(0-255) 定时间隔（单位为秒）执行次数（留空为无限制执行，需使用停止定时器方可关闭，填写3为执行3次后自动关闭定时器）
SETOFFTIMER 定时器索引(0-255) //停止定时器
SetOnTimer 0 20
SendMsg 5 你目前位于%m的(%x：%y)
SetOffTimer 0

### 给人物指定爆率文件命令
说明: 给人物指定爆率文件命令
LoadMonItems 怪物名 配置文件名 @区段（不要[]，可以为空）
LoadMonItems 白野猪 QuestDiary\爆率系统\基础爆率.txt @药水
LoadMonItems 白野猪 MonItems\稻草人.txt
ResetMonItems 怪物名

### 更改人物颜色
**功能：**
**格式：**CHANGENAMECOLOR 颜色代码(0-255)

### 更改头发类型
**功能：**
**格式：**

### 更换性别
**功能：**
**格式：**    CHANGEGENDER 性別(男 0
CHANGEGENDER 0
CHANGEGENDER 1

### 挂机命令[!]
功能: 挂机命令
格式:ISDUPMODE (0或空时检测所有对象，1只检测人物)

### 关闭NPC大对话框
格式: CLOSEMERCHANTBIGDLG
**注意：上面的命令如果不能完美关闭自定义NPC大对话框，请使用下面的命令**

### 关闭自定义NPC对话框
**注意：上面的命令如果不能完美关闭自定义NPC大对话框，请使用下面的命令**

### 过滤全服提示信息
功能：
格式：FILTERGLOBALMSG 过滤类型 是否过滤(0不过滤，1过滤)
FILTERGLOBALMSG 1 1
FILTERGLOBALMSG 2 1
FILTERGLOBALMSG 3 1
FILTERGLOBALMSG 4 1
SENDMSG 0 信息内容
SENDMSG 1 信息内容
SENDMSG 2 信息内容
SENDMSG 3 信息内容
FILTERGLOBALMSG 1 1
SENDMSG 6 开启过滤全服掉落提示信息。
FILTERGLOBALMSG 1 0
SENDMSG 6 关闭过滤全服掉落提示信息。
FILTERGLOBALMSG 2 1
SENDMSG 6 开启过滤SendCenterMsg全局信息。
FILTERGLOBALMSG 2 0
SENDMSG 6 关闭过滤SendCenterMsg全局信息。
FILTERGLOBALMSG 3 1
SENDMSG 6 开启过滤全服SENDMSG0和SENDMSG1和SENDMSG2和SENDMSG3信息。
FILTERGLOBALMSG 3 0
SENDMSG 6 关闭过滤全服SENDMSG0和SENDMSG1和SENDMSG2和SENDMSG3信息。
FILTERGLOBALMSG 4 1
SENDMSG 6 开启过滤SENDMOVEMSG信息。
FILTERGLOBALMSG 4 0
SENDMSG 6 关闭过滤SENDMOVEMSG信息。

### 行会地图传送
GUILDMAPMOVE 地图号 X
GUILDMAPMOVE  3 330

### 行会地图随机传送


### 行会建设相关
格式：
格式：
格式：
格式：GUILDFLOURISHPOINT控制符（+-）数字
格式：
CHECKGUILDBUILDPOINT  控制符（<>=）数字
格式：
CHECKGUILDAURAEPOINT 控制符（<>=）数字
格式：
格式:
CHECKGUILDFLOURISHPOINT 控制符（<>=）数字

### 回收指定位置装备
**功能：**
TakePosW 物品位置
TakePosW 1
TakePosW 30
TakePosW 40

### 获取背包中某物品的数量[!]
**功能：**
格式: GetBagItemCount 物品名称 保存变量 排除OK框中的物品(0或空:计算OK框的物品，1：不算OK框中的物品) 是否判断满持久(0:或空不判断； 1：判断）
GetBagItemCount 屠龙 N1
SENDMSG 6 你的背包中共有<$STR(N1)>把屠龙

### 获取地图中某怪物的坐标[!]
**功能：**
格式: CheckMapMonInfo 地图名称 怪物名称 X坐标变量 Y坐标变量 允许获取改名怪物(1获取，0或空为不获取)
CheckMapMonInfo 3 白野猪 n1 n2
SENDMSG 6 盟重有个白野猪在<$STR(N1)>:<$STR(N2)>

### 获取对面人物的名字
说明: 获取对面人物的名字
格式: GetOppositeHumName
GetOppositeHumName S0
SendMsg 5 你对面的人物是:

### 获取怪物原始各项参数
说明: 获取怪物原始各项参数
格式：通过怪物名字取数据库字段值 GetDBMonsterFieldValue 怪物名称 字段名 变量
GetDBMonsterFieldValue 魔龙教主 HP <$STR(N1)>

### 获取技能快捷键、设置技能快捷键
GetSkillKey 烈火剑法 N1
SetSkillKey 烈火剑法 76

### 获取技能信息命令
功能说明：获取技能信息命令
GetMagicInfo 技能名称 值类型 变量
GetMagicInfo 开天斩 0 N1
GetMagicInfo 开天斩 1 N2
GetMagicInfo 开天斩 2 N3
SENDMSG 6 技能等级：<$str(N1)>，强化等级：<$str(N2)>，技能点：<$str(N3)>

### 获取某地图怪物数量 [!]
**功能：**
格式: GetMapMonCount 地图名 是否排除宝宝(0：不排除，1：排除) 保存变量
GetMapMonCount 3 0 N1
SENDMSG 6 地图3一共有<$STR(N1)>个怪物

### 获取某地图人物数量 [!]
**功能：**
格式: GetMapHumanCount 地图名 不算假人(0：算假人，1：不算假人) 保存变量
GetMapHumanCount 3 1 N1
SENDMSG 6 地图3一共有<$STR(N1)>个真实玩家

### 获取人物全身星星数量[!]
**功能：**
格式:GetUpgradeCount 位置 变量说明：位置支持OK框，装备，首饰，神佑，all或\*表示取得身上所有装备星星的数量
GetUpgradeCount 1 n1
SENDMSG 6 武器一共有<$STR(N1)>个星星

### 获取文本字符
GetRandomText 文件路径 变量

### 获取物品原始各项数据库字段值参数
说明：获取物品原始各项数据库字段值参数
格式：通过物品名字取数据库字段值 GetDBItemFieldValue 物品名称 字段名 变量
格式：通过 IDX 字段取数据库字段值 GetDBIdxItemFieldValue idx 字段名 变量
GetDBItemFieldValue 屠龙 idx <$STR(N1)>
GetDBItemFieldValue 屠龙 stdmode <$STR(N2)>
CHECKTEXTLIST ..\QuestDiary\商城批量购物\金币物品.txt <$STR(S0)>
MOV S$商城当前购入物品名
MOV N$商城当前购入物品单 0
MOV S$商城当前购入物品名 <$STR(S0)>
MOV N$商城当前购入物品单价 <$STR(M0)>
GetDBItemFieldValue <$STR(S$商城当前购入物品名)> idx N$商铺购买物品代码
OPENMERCHANTBIGDLG 176 19 1 0 10 70 1 190 8 1
MUL N$批量商铺购买物品总金额 <$STR(N$商城当前购入物品单价)> <$STR(N$批量商铺购买物品数量)>
说明：@关闭批量\
EQUAL N300 0
MUL N$批量商铺购买物品总金额 <$STR(N$商城当前购入物品单价)> <$STR(N$批量商铺购买物品数量)>
OPENMERCHANTBIGDLG 176 19 1 0 10 70 1 190 8 1
说明：@关闭批量\
MessageBox 缺少“<$STR(N$批量商铺购买物品总金额)>”个金币无法购买！

### 技能转换 技能替换[!]
**功能：**
格式: ConvertSkill 原技能 目标技能
ConvertSkill 野蛮冲撞 烈火剑法
SENDMSG 6 替换成功
H.CONVERTSKILL 英雄野蛮冲撞 英雄烈火剑法

### 加入会员人物及时间
相关命令：
CHECKUSERDATE   会员.txt

### 假人自动练功[!]
功能: 假人自动练功
格式:AutoUseMagic 技能名字 间隔秒。(必须是学过的技能，在非挂机状态，没有攻击目标的情况下才能正常练功)
AutoUseMagic 雷电术 10

### 检测伴侣是否在线和同一地图
格式:
CheckDearOnline 人物名称 (不填表示检查自己的配偶在不在线，填则表示检查指定人的配偶在不在线）
CheckDearOnMap 地图号(self或不填，自己所在的地图，否则为指定地图） 人物名称(不填表示检查自己的配偶在某个地图，否则检查指定人的配偶是否在某个地图）
CheckDearOnline 翎风世界
CheckDearOnMap 3 翎风世界
CheckDearOnMap 0

### 检测当前玩家登陆的分辨率
CheckClientHeight = 600
CheckClientWidth = 1024
CheckClientHeight > 800

### 检测对面的有没有徒弟
**功能：**
**命令格式：**

### 检测对面是否为自己的徒弟
**功能：**
**格式：**  CHECKPOSEISPRENTICE

### 检测身上指定装备名字 获取looks保存到变量
**功能：**
格式: CheckItemwLooks 装备名称 变量名(变量名可以不填)
CheckItemwLooks 传送戒指 N0
SENDMSG 0 测试成功<$Str(n0)>

### 检测师傅（或徒弟）是否在XXX地图
**功能：**检测师傅（或徒弟）是否在XXX地图，支持SELF（是否同一地图) 徒弟序号(为空表示大徒弟)
**命令格式：**    CHECKMASTERONMAP

### 检测师傅（或徒弟）是否在线
**功能：**用来检查人物的师傅或者徒弟是否在线上
**命令格式：**
CHECKMASTERONLINE 徒弟序号(为空表示大徒弟)

### 检测文件中是否包含字符串
功能：
格式：
CheckContainsTextList 文件名 字符串
CheckContainsTextList ..\QuestDiary\理想\理想爆率\10元地图.txt <$MAP>
MESSAGEBOX 包含
CheckContainsTextList 支持绝对路径（地址直接写绝对路径即可）

### 检测英雄怒气值
**功能：**
**格式：**
CheckAngryValue 操作符(>,<,=) 值 值类型(0:点数；1:百分比)
CheckAngryValue > 80 1

### 检测装备元素属性
**功能：**
**格式：** CHECKNEWITEMVALUE 位置(-1时是OK框中的装备, 0-12时是穿在身上的装备) 属性(0-10) 检测符(<,>,=) 值(1-100)
CHECKNEWITEMVALUE 0 0 > 10

### 检测自己是否是师傅
**功能：**用来检测自己是否是师傅
**命令格式：**

### 检测自己是否是徒弟
**功能：**用来检测自己是否是徒弟
**命令格式：**

### 检查对面的人物是不是自己的师傅
**功能：**
**命令格式：**

### 检查自己是不是别人的徒弟
**功能：**
**命令格式：**

### 减少合击怒气恢复间隔
**功能：**
DecAddAngryValueTime 100 0
DecAddAngryValueTime 100 0
SENDMSG 7 怒气恢复间隔减少100毫秒，有效时间：持续有效
DecAddAngryValueTime 500 200
SENDMSG 7 怒气恢复间隔减少500毫秒，有效时间：200秒

### 减少技能冷却时间
功能说明: 减少技能冷却时间
SetSkillDecCD 技能名称 操作符(+/-/=) 时间（秒)
GetSkillDecCD 技能名称 变量名
GetSkillCD 技能名称 变量名
ClearSkillCD 技能名称
SetSkillDecCD 烈火剑法 = 2
SetSkillDecCD 烈火剑法 + 1
GetSkillDecCD 烈火剑法 N1
GetSkillCD 烈火剑法 N2
SENDMSG 6 烈火剑法缩短CD时间<$Str(N1)>秒，当前冷确时间为<$Str(N2)>秒
SetSkillDecCD [连击技能] = 3
GetSkillDecCD [连击技能] N1
GetSkillCD [连击技能] N2

### 将背包物品放入仓库
功能: 将背包物品放入仓库
格式:
BagItemToStorage 物品名称 仓库类型(0或空:普通仓；1:无限仓) 变量(保存实际存放数量)
BagItemToStorageIdx 数据库物品Idx 仓库类型(0或空:普通仓；1:无限仓) 变量(保存实际存放数量)
BagItemToStoragemakeIndex 数据库物品唯一序列号 仓库类型(0或空:普通仓；1:无限仓) 变量(保存实际存放数量)
BagItemToStorage 屠龙 1 N1
SendMsg 6 背包的屠龙有<$STR(N1)>保存到普通仓库中

### 将人物行会名加入列表
**功能：**
**格式：**
ADDGUILDLIST    guildlist.txt

### 角色变身怪物、人物变身
格式：changeAppr appr 时间(单位：秒)

### 角色打怪爆出物品自动拾取，角色打怪爆出物品范围捡起[!]
**功能：**角色打怪爆出物品自动拾取，角色打怪爆出物品范围捡起
格式：OpenAutoPickItem 类型(1:自身; 2:宝宝; 3:自己+宝宝) 有效时间 捡物范围 是否一次全捡 捡人物丢弃物品 捡人物爆出物品 物品掉地上多长时间才能捡 是否进入主人背包（参数仅H.有效）
说明：OpenAutoPickItem 类型(1:自己; 2:宝宝; 3:自己+宝宝) 有效时间(0在线一直有效,**单位：秒**) 范围(0:走上去捡；>0:范围捡 ) 是否秒捡(0或空则1个个的捡范围内可捡物品， 1则秒捡范围内所有可捡物品 ) 捡人物丢弃物品(0/1) 捡人物爆出物品(0/1) 物品掉地上多长时间才能捡(**单位:毫秒**) 是否进入主人背包（参数仅H.有效）
**注意：范围内秒捡请慎用捡起触发鉴定脚本，拾取鉴定脚本写的不够优秀（各种GOTO各种CALL等，甚至还有死循环脚本）可能会引起游戏卡顿或更严重的后果，另秒捡的话范围请设置建议3，最大建议不超过20.超过视觉范围无意义，范围越大一下捡的物品越多，同时鉴定脚本触发也越厉害**
OpenAutoPickItem 3 0 3 0 0 0 5000
NoAutoRangePickItem 禁止范围拾取 （地图内开启自动拾取命令功能后，打怪爆出物品不能自动拾取）

### 脚本控制人物等级
**功能：**
**格式：**    CHANGELEVEL
CHANGELEVEL =
CHANGELEVEL +
CHANGELEVEL -

### 脚本命令给物品镶嵌宝石
CheckItemFluteIndexHasStone 装备位置 孔位置
ItemAddStone 装备位置 宝石名 孔位置(0或空表示自动空孔位，1-8：指定位置)
ItemDelStone 装备位置 孔位置
ItemoffStone 装备位置 孔位置（1-8）

### 脚本命令释放技能
参数1 释放技能id (能支持自定义技能)
参数2 技能是否是强化技能 0=普通技能 1=强化技能
参数3 技能等级
参数4 技能目标 1=攻击目标 2=自身
参数5 是否计算冷却时间 0或空为计算。1为不计算
参数6 值=0或空会不支持伤害触发 值=1支持伤害触发
参数6为以下触发：
SENDMSG 6 你的物理攻击触发了一次3级烈火剑法
SENDMSG 6 你的雷电术触发特效攻击，对怪物释放了一次强化九重冰咆哮
SENDMSG 6 你的雷电术攻击为自己释放了一次3级治疗术

### 脚本命令释放技能(无动作施展)
参数1 释放技能id (能支持自定义技能)
参数2 技能是否是强化技能 0=普通技能 1=强化技能
参数3 技能等级
参数4 技能目标 1=攻击目标 2=自身
参数5 是否计算冷却时间 0或空为计算。1为不计算
参数6 值=0或空不会支持伤害触发 值=1支持伤害触发
参数6为以下触发：
SENDMSG 6 你的物理攻击触发了一次3级烈火剑法
SENDMSG 6 你的雷电术触发特效攻击，对怪物释放了一次强化九重冰咆哮
SENDMSG 6 你的雷电术攻击为自己释放了一次3级治疗术
SENDMSG 6 你的雷电术触发特效攻击，对怪物释放了一次强化九重冰咆哮

### 脚本刷怪
**格式：**    MONGENEX 地图名称 坐标X 坐标Y 怪物名称 范围 数量 名字颜色(0-255、 为空为默认颜色) 内功怪物(0,1) 国家ID 是否可攻击同国家的玩家(0,1) 不同国家怪物是否可PK(0,1) 怪物能否被同国家的人攻击(0,1) 体型大小（空或100为默认大小）
注意：请不要跨界留空（如不要颜色只需要内功怪物时名字颜色参数必须有，如果只要名字颜色后面不要可在颜色值后留空） 名字颜色支持变量
**示例：**
MONGENEX D717 100 100 白野猪 100 50
MonGen 怪物名 X Y 国家ID 怪物能否攻击同国家的人(0,1) 同国家的怪物能否相互攻击(0,1) 怪物能否被同国家的人来攻击(0,1)
服务端刷怪文件格式：
MonGen.txt 格式：地图 坐标X 坐标Y 怪物名字 范围 数量 间隔 集中刷新坐标机率 名字颜色(0~255) 内功怪物(0,1) 国家ID 怪物能否攻击同国家的人(0,1) 不同国家的怪物能否相互攻击(0,1) 怪物能否被同国家的人来攻击(0,1)

### 脚本调整人物PK点
**功能：**
**格式：**    CHANGEPKPOINT
CHANGEPKPOINT =
CHANGEPKPOINT +
CHANGEPKPOINT -

### 脚本调整升级经验
**功能：**
**格式：**    CHANGEEXP
CHANGEEXP = 20000
CHANGEEXP +
ChangeExp + 1000 1 1
CHANGEEXP -

### 解除英雄强制和平模式限制
**功能：**
CancelHeroForcePeaceMode 命令有效时间(单位：秒; 0为一直有效)
CancelHeroForcePeaceMode 0
SENDMSG 7 你的英雄已经解除和平模式限制
CancelHeroForcePeaceMode 600
SENDMSG 7 你的英雄已经解除和平模式限制，有效时间：600秒

### 禁止登录列表
**命令格式：**加入列表：@DenyIPLogon IP地址
**命令格式：**加入列表：@DelDenyAccountLogon
**命令格式：**加入列表：@DenyCharNameLogon

### 开启第四个连击技能的命令[!]
**功能：**开启第四个连击技能的命令
**格式：**无
**说明：**

### 扩展MessageBox
MessageBox 信息 @确定 @取消
MessageBox 是否确认要删除 @确定 @取消

### 扩展MOVR使用方法
**功能：**
**格式：**    MOVR 变量 数值1 数值2
MOVR G10 100        ;随机生成100以内的随机数.
MOVR G10 10 100     ;随机生成10-100之间随机数
MOVR G10 100 5000   ;随机生成100-5000之间随机数
MOVR G10 1000 9999  ;随机生成1000-9999之间随机数

### 练习技能
**功能：**
**格式：**    ADDSKILL
相关命令：

### 秒杀保护
**功能：**
**格式：**
ProtectHP 检测血量 保留血量 有效时间 是否为百分比
ProtectHP 90 10 360 1
SENDMSG 6 该脚本的意思是，你的血量在大于等于90%的情况下，如果有人可以一刀秒杀你，你不会被秒杀，而是把你的血量降低到10%，并且触发QF字段[@ProtectHP]，有效期360秒
ProtectHP 100 10 360 0
SENDMSG 6 该脚本的意思是，你的血量在大于等于100的情况下，如果有人可以一刀秒杀你，你不会被秒杀，而是把你的血量降低到10，并且触发QF字段[@ProtectHP]，有效期360秒

### 千里传音[!]
**功能：**
**格式：在没有佩戴传音道具前提下，使用命令进行千里传音**
CHECKGAMEGOLD > 0
MOV S1 <$PARAMS>
GAMEGOLD - 1
SENDMSG 0 <$USERNAME>:<$STR(S1)> 255 253 0
SENDMSG 7 使用千里传音需要支付1元宝
CHECKGAMEGOLD > 0
MOV S1 <$PARAM(1)>
GAMEGOLD - 1
SENDMSG 0 <$USERNAME>:<$STR(S1)> 255 253 0
SENDMSG 7 使用千里传音需要支付1元宝
CHECKGAMEGOLD > 0
MOV S1 <$PARAM(1)>
MOV S2 <$PARAM(2)>
MOV S3 <$PARAM(3)>
MOV S4 <$PARAM(4)>
MOV S5 <$PARAM(5)>
MOV S6 <$PARAM(6)>
GAMEGOLD - 2
SENDTOPCHATBOARDMSG 0 149 235 30 <$STR(S1)><$STR(S2)><$STR(S3)><$STR(S4)><$STR(S5)><$STR(S6)>
SENDMSG 7 使用传音筒需要支付2元宝

### 强行捡起他人打怪爆出未到冷却时间的物品[!]
**功能：**强行捡起地面他人打怪爆出(一定时间范围内不能捡起)的物品
SENDMSG 6 物品已捡起

### 清除SendCenterMsg DelayGoto
CLEARDELAYGOTO 1

### 清除地图物品
**功能：**
**格式：**    CLEARITEMMAP 地图 X Y 范围 物品名称 (清除地图物品，不带物品名称则清除所有)
**说明：**   物品名字等于\*时表示指定范围内的所有物品.
CLEARITEMMAP 3 330 330 10 回城卷
CLEARITEMMAP 3 330 330 10
ClearItemMap 3

### 清除地图中的怪物
**功能：**用于清除指定地图里的怪物，人物的宝宝不在此范围以内，禁止清除怪物列表中的怪物不会被清除。
**命令格式：**

### 清除结婚信息


### 清除列表内容
命令格式:
CLEARNAMELIST namelist.txt
ClearNameList 文件名 是否绝对路径（0或空：相对路径；1：绝对路径）

### 清除人物的仓库密码
**功能：**
**格式：**

### 清除人物转生
**功能：**
**格式：**;==========================================

### 清除延时移动
**功能:** 清除延时移动
**格式:**

### 清除英雄转生
**功能：**
**格式：**;==========================================

### 清掉地图某范围的怪物[!]
**功能：**
格式: KillMapMon 地图名 坐标X 坐标Y 范围 怪物名(\*表示不判断名称) 是否爆物品(0：不爆，1：爆) 是否清尸体(0或空:不清; 1:清)
KillMapMon 3 333 333 10 \* 0
SENDMSG 6 地图3，坐标333,333范围10以内怪物被成功清理，不爆物品

### 清空P变量
SENDMSG 6 你的P变量全部清空重置为0！！！！
说明：比如自定义按钮用P变量关闭对话框无法清空，可以使用此命令触发清空

### 清空变量[!]
**功能：**
格式: ClearVar 变量名 数量
ClearVar S0 5
SENDMSG 6 S0-S4全部清空

### 取得随机字符串(2020新)
功能: 从文件中随机获取一行字符串
格式:
GetCacheRandomText 文件路径 变量(S0--S99) 指定行(1-10000)
说明:
SendMsg 5
SendMsg 5
GetCacheRandomText 为缓存模式 比 GetRandomText 更为高效!

### 取对面角色人物名
**功能：**
**格式：**GETPOSENAME
**功能：
GETPOSENAME a1

### 取下镶嵌宝石命令
ItemoffStone 装备位置 孔位置（1-8）

### 取指定排行榜指定排名的玩家名字和检测人物在指定排行榜中的名次
**功能：**
GetRankNameByNo (排行榜 1-等级榜 2-战士榜 3-法师榜 4-道士榜) 名次 玩家名变量
GetRankNoByName (排行榜 1-等级榜 2-战士榜 3-法师榜 4-道士榜) 玩家名 名次变量
GetRankNameByNo 1 1 S1
SENDMSG 6 等级榜排行第一的是：<$str(S1)>
GetRankNoByName 1 <$UserName> N1
SENDMSG 6 我在等级榜中的排名是：<$str(N1)>
CheckSelfRankNo ><= 榜单(1-等级榜\2-战士榜\3-法师榜\4-道士榜) 名次
CheckSelfRankNo < 1 4
SENDMSG 6 我的排名在前3
SENDMSG 6 我的排名不在前3
GetRankLevelByNo (排行榜 1-等级榜 2-战士榜 3-法师榜 4-道士榜) 名次 玩家等级变量
GetRankNameByNo 1 5 S1
GetRankLevelByNo 1 5 N1
GetRankLevelByName (排行榜 1-等级榜 2-战士榜 3-法师榜 4-道士榜) 玩家名称 玩家等级变量
GetRankNoByName 1 dddd N1
GetRankLevelByName 1 dddd N2

### 取字符串长度[!]
**功能：**
格式: TextLength 字符串 保存变量
TextLength 这是一个测试文字aaabbbccc N1
SENDMSG 6 <$STR(N1)>

### 人物/英雄临时数据命令
格式：SetTempDBMode 开/关(0：关；非0:开）
注意：开启临时数据模式后数据不在保存到数据库，关闭临时模式或重新退出/小退进入游戏人物将读取开启临时模式前的数，临时数据模式期间该角色数据都不会保存到数据库
SetTempDBMode 1
SENDMSG 4 开启临时数据模式
SetTempDBMode 0
SENDMSG 4 关闭临时数据模式,数据恢复到开启临时数据前
SetTempDBMode 0 1
SENDMSG 4 关闭临时数据模式,数据正常保存

### 人物和英雄穿戴装备前触发
**功能：**
SENDMSG 7 Begin穿装备：位置:<$CurItemPos>，物品:<$CurItemName>(<$G\_CurItemName>)，ID:<$CurItemMakeIndex>
SENDMSG 7 英雄Begin穿装备：位置:<$H.CurItemPos>，物品:<$H.CurItemName>(<$H.G\_CurItemName>)，ID:<$H.CurItemMakeIndex>

### 人物隐身属性
HideModeEx 时间 是否半透明(0:否;1:是)
H.HideModeEx 时间 是否半透明(0:否;1:是)
HideModeEx 时间 是否半透明(0:否;1:是)
HideModeEx 5 1

### 杀死宝宝
**功能：**
**格式：KillSlave 是否清尸体（0或空:不清; 1:清）宝宝名称(名字为空或\*,清所有宝宝)**

### 杀死人物
**功能：**
**格式：**
Kill 类型(1为不显示凶手信息、2为不掉物品.不显示凶手信息、3为显示凶手信息为NPC、4为不掉物品.显示凶手信息为NPC) 清理尸体(0:不清理；1:清理；清尸对人物/英雄无效)
KILL 0
KILL 1 人物死亡不掉物品,不显示凶手信息
KILL 2
KILL 3
KILL 2
M.Kill 1 1

### 杀死人物的宝宝
说明:把自己的宝宝杀死.
格式:KillCallMob 名字
KILLCALLMOB 神兽
KILLCALLMOB 白野猪

### 删除非本职业的所有技能
**功能：**
**格式：**
相关命令：

### 删除行会成员
**功能：**
**格式：**    DelGuildMember 行会名称 人物名称
DelGuildMember 测试行会 <$USERNAME>

### 删除会员人物及时间
相关命令：

### 删除列表行会名
**功能：**
**格式：**

### 删除人物IP在列表中
**功能：**
**功能：

### 删除人物名在列表中
**功能：**
**格式：

### 删除人物帐号在列表中
**功能：**
**功能：

### 删除所有技能
**功能：**
**格式：**
相关命令：

### 删除文本指定行
格式: DelTextListLine 文件名 行号(0开始) 是否绝对路径(0:否; 1:是)
DelTextListLine d:\d.txt 0 1

### 删除一个NPC
格式: DELNPC NPC名字 地图代码
DELNPC 扩展参数3支持删除指定地图的NPC
格式：

### 删除指定技能
**功能：**
**格式：**    DELSKILL
相关命令：

### 设置被怪物攻击时伤害吸收
**功能：**
**格式：**
StruckDamageAbsorb 怪物名(\*表示所有怪) 吸收几率(1~100) 伤害吸收比例(1~100) 有效时间（秒）
StruckDamageAbsorb 白野猪 50 80 30

### 设置攻击力倍数[!]
**功能：**
**格式：**POWERRATE 攻击倍率 有效时间(0为永久) 是否保存(1为保存/0或留空不保存) 是否提示(0或者留空提示/1为不提示) 类型(0所有对象/1攻击人物(人物/英雄/宝宝)倍率/2攻击怪物倍率)
POWERRATE 1000 600
POWERRATE 1000 0 1
POWERRATE 1000 600 1

### 设置技能伤害防御[!]
**功能：**
格式: SetSkillPower 技能ID +/-/= 人物伤害增加%（-32768 .. 32767） 人物伤害增加值（-32768 .. 32767） 怪物伤害增加%（-32768 .. 32767） 怪物伤害增加值（-32768 .. 32767） 防御增加%（-32768 .. 32767） 防御增加值（-32768 .. 32767） 时间(秒; 0-65535;0一直有效) 是否保存数据库(0:不存；1：存）示范脚本：
SetSkillPower 66 = 100 0 100 0 0 0 0
SENDMSG 6 你的开天斩技能对人物伤害增加为原来的2倍(增加100%)，对怪物伤害为原来的2倍(增加100%)
GetSkillPower 技能ID 人物伤害增加%(变量) 人物伤害增加值(变量) 怪物伤害增加%(变量) 怪物伤害增加值(变量) 防御增加%(变量) 防御增加值(变量) 时间(变量) 是否保存数据库(变量)

### 设置离线挂机
**功能：**
**格式：**    SETOFFLINEPLAY ON/OFF
SETOFFLINEPLAY ON

### 设置人物当前模式
**功能：**
**格式：**CHANGEMODE 模式类型
CHANGEMODE 1 1
CHANGEMODE 2 1
CHANGEMODE 3

### 设置人物当前权限
**功能：**
**格式：(提升到超级GM)**

### 设置杀怪经验倍数
**功能：**
**格式：**
KILLMONEXPRATE 倍率
KILLMONEXPRATE 1000 600
KILLMONEXPRATE 1000 0 1
KILLMONEXPRATE 1000 600 1

### 设置修改宝宝属性
ChangeSlaveAbility 参数1 参数值 宝宝名（为空表示所有宝宝）
参数1表示值：
RecalcSlaveAbility 宝宝名（为空表示所有宝宝）
ChangeSlaveAbility 14 300
ChangeSlaveAbility 15 300
ChangeSlaveAbility 30 30

### 设置装备发光特效
格式: SETITEMEFFECT 位置(-1时是升级框中的装备, 0-51时是穿在身上的装备， boxitem0-boxitem7为自定义OK框) 特效编号(0-50000,0为清除特效) 特效位置
SETITEMEFFECT 0 1
SETITEMEFFECT 6 1
SendMsg 6 左手镯附加了特效编号1，位置0
SETITEMEFFECT 6 0
SendMsg 6 左手镯关闭了位置0特效编号
SETITEMEFFECT 6 1 1
SendMsg 6 左手镯附加了特效编号1，位置1
SETITEMEFFECT 6 0 1
SendMsg 6 左手镯关闭了位置1的特效
SETITEMEFFECT 6 5 2
SendMsg 6 左手镯附加了特效编号5，位置2
SETITEMEFFECT 6 0 2
SendMsg 6 左手镯关闭了位置2的特效

### 使用外置默认浏览器打开网站
说明: 使用外置默认浏览器打开网站
功能: 浏览器打开网站.
格式: OpenUrl 网站

### 收回OK框中的物品
格式: TAKEDLGITEM

### 收回玩家英雄脚本命令
**功能：**

### 数学表达式运算命令
FORMULATION 公式 结果保存变量
FORMULATION <$STR(N$切割倍率)>/(<$STR(N$人物切割值)>+<$STR(N10)>)\*100+<$STR(N$人物切割值)> N$切割值
Formulation 1/(3-3)\*5+6 N1
说明
ForMulAtion Random(1,20) N$获取数据显示
ForMulAtion Random(1,20) N$获取数据显示
Sendmsg 6 <$Str(N$获取数据显示)>,显示数据为1-20之间的随机数值
ForMulAtion Random(1,20)^2 N$获取数据显示
Sendmsg 6 <$Str(N$获取数据显示)>,显示数据为1-20之间的随机数值的平方

### 刷新当前装备属性到客户端
格式：updateitem 位置
ChangeItemNameColor -1 253
注意：clearLinkItem 因为绑定必须给物品一个位置，目前以下2个命令强行绑定到OK框，请加上解除绑定命令，不然不能及时刷新背包物品属性，需要小退生效，加上后及时生效！！！

### 所有行会同时攻城
功能:所有行会在当晚同时攻城
AddAttackSabukAll 城堡号(0)

### 特修装备
**功能：**
**格式：**    REPAIRALL 兼容其它引擎的特殊修理命令
ACTREPAIRALL 操作命令的修理
CHECKREPAIRALLGOLD <$STR(N99)> 统计需要修理装备数据库设置价格\*特修价格 、 变量为价格变量
CHECKREPAIRALLGOLD <$STR(N99)>

### 踢除服务器挂机人物
**功能：**
**格式：**    KICKOFFLINE //踢除服务器所有挂机人物

### 踢除服务器所有人物
**功能：**
**格式：**    KICKALLPLAY //踢除服务器所有在线人物

### 踢人物下线
**功能：**
**格式：**
SENDMSG 5
DelayCall 5000 @Kicks
SENDMSG 5 %s，非法登录游戏，5秒会将被小退游戏！[@KICKS]
KICK 1;注：命令：KICK 后面参数为0或空时为踢下线，为1时候将人物小退！

### 替换行会掌门,改变行会的掌门人
格式：SetGuildMaster 1/2(1是正会长，2是副会长）如果已经是行会会长，则调用无效
SetGuildMaster 1

### 替换字符命令[!]
**功能：**
格式：
TextReplace 字符串内容 待替换的内容 新的内容 保存变量 分大小写(0或空：不分； 1：分) 只替换一次(0或空：全部替换；1：只替换一次）
TextReplace AAABBBAAA AAA 字母 S1 0 0
SendMsg 6 <$STR(S1)>

### 添加行会成员
**功能：**
**格式：**    AddGuildMember 行会名称 人物名称
AddGuildMember 测试行会 <$USERNAME>

### 调用安全区特效命令
格式: RectMapEffect 地图 左上角X 左上角Y 宽度 高度 光圈类型 显示时间（单位：秒；0表示永久）
RectMapEffect 3 317 346 10 5 4 0

### 调整宝宝等级
功能: 直接调整人物宝宝的等级
格式:
ChangeSlaveLevel 名字(\*为所有宝宝) 操作符(+ = -) 等级(1-7) 参数4（0：调整单个宝宝；1：调整所有宝宝）
ChangeSlaveLevel 虎卫 =
ChangeSlaveLevel 虎卫 =
ChangeSlaveLevel \* = 7

### 调整暴击威力
格式: SetBlastHitRate 威力(百分比) 有效时间(秒，0表示一直有效)
SetBlastHitRate 120 5

### 调整暴击威力倍数命令
**功能：**
SetBlastHitRate 120 5

### 调整背包负重
AddMaxWeight + 100
SendMsg 6 扩展背包最大重量：<$AddMaxBW>

### 调整行会可以容纳最多成员
格式: CHANGEGUILDMEMBERMAXLIMITCOUNT 行会名称(SELF表示调整自己所在的行会) 调整符(+,-,=) 数量
CHANGEGUILDMEMBERMAXLIMITCOUNT = 100

### 调整行会人数上限[!]
功能: 调整当前行会的人数上限.
说明:
格式: AddGuildMemberCount 操作符(+
CheckItem 金条 1
Take 金条
AddGuildMemberCount +

### 调整合击怒气值
**功能：**
SetAngryValue 操作符(+/-/=) 值 是否为百分比值(0:点数；1：百分比)
SetAngryValue + 5 0
SendMsg 6 你的英雄怒气增加了5个点
SetAngryValue + 5 1
SendMsg 6 你的英雄怒气增加了5%

### 调整技能等级(扩展)
**功能：**
**格式：**   SKILLLEVEL 魔法名称 调整符(+,-,=) 等级 是否调整强化技能(0或为空时为技能等级,1为强化技能等级)
SKILLLEVEL 雷电术 =
SKILLLEVEL 雷电术 +
SKILLLEVEL 雷电术 -
CHECKSKILL 冰咆哮 = 0 1
SKILLLEVEL 冰咆哮 = 1 1
SENDMSG 6 冰咆哮已修炼到强化一重

### 调整技能点数
**功能：**
**格式：**
**英雄相关格式：**
CHANGETRANPOINT 雷电术 = 100
CHANGETRANPOINT 雷电术 + 200
CHANGETRANPOINT 雷电术 - 10
CHANGETRANPOINT 雷电术 > 10
SENDMSG 6 雷电术技能点数大于10
SENDMSG 6 雷电术技能点数小于10

### 调整金刚石数量
**功能：**
**格式：**    GAMEDIAMOND
GAMEGIRD 控制符(=,+,-)
GAMEDIAMOND =
GAMEGIRD =

### 调整流星火雨伤害次数
格式： SetSkill58AttackCount 伤害次数(1-5)
格式： H.SetSkill58AttackCount 伤害次数(1-5)
注意：人物/英雄根据设置的次数和M2选项中的是否勾选“两次伤害”，选项和次数之间取最大次数
SetSkill58AttackCount 3
SENDMSG 6 技能流星火雨伤害调整为3次了
H.SetSkill58AttackCount 5
SENDMSG 6 英雄技能流星火雨伤害调整为5次了

### 调整人物的荣誉值[!]
CheckLevelEx >
ChangeNationCredit + 100
格式: GAMEGLORY (+,-,=) 值
GAMEGLORY + 5

### 调整人物会员等级
**功能：**
**格式：**
SETMEMBERLEVEL 控制符(=,+,-)
SETMEMBERLEVEL =
SETMEMBERLEVEL +
SETMEMBERLEVEL -

### 调整人物会员类型
**功能：**
**格式：**    SETMEMBERTYPE
SETMEMBERTYPE =
SETMEMBERTYPE +
SETMEMBERTYPE -

### 调整人物金币数量
功能：调整人物金币数量
命令：GOLDCOUNT 控制符(=,+,-) 金币值 (0-2100000000)格式：
GOLDCOUNT = 10000

### 调整人物属性
格式: ChangeHumAbility 属性(1-29) 操作符(+ = -) 效果 时间秒(1-65535) 参数5(值是否为百分比;0:固定值；1:百分比)
说明: 属性1-29分别对应值
注意:整后的属性效果只在人物在线时有效.? 不带时间为在线一直有效
ChangeHumAbility 2 + 10 60
ChangeHumAbility 2 + 50 60 1
ChangeHumAbility 2 = 100 5 1
ChangeHumAbility 2 = 0
ChangeHumAbility 2 + 50 5 1

### 调整人物游戏点数
**功能：**
**格式：**
GAMEPOINT 控制符(=,+,-)
GAMEPOINT =
GAMEPOINT +
GAMEPOINT -

### 调整声望点
**功能：**
**格式：**
CREDITPOINT 控制符(=,+,-)
CREDITPOINT =
CREDITPOINT +
CREDITPOINT -

### 调整属性点
**功能：**
**格式：**
BONUSPOINT 控制符(=,+)
BONUSPOINT =
BONUSPOINT +
相关命令：

### 调整物品名字颜色
功能:调整人物身上物品装备名字颜色(英雄M2)
格式:ChangeItemNameColor 位置(0-13)
说明:颜色=0时恢复默认颜色.
ChangeItemNameColor 1

### 调整物品新增属性
格式: SetNewItemValue 位置(-1时是OK框中的装备, 0-12时是穿在身上的装备) 属性(0-25) 操作符(+,-,=) 值(1-100)
SetNewItemValue -1 0 + 10
格式: H.SetNewItemValue 位置(-1时是OK框中的装备, 0-12时是穿在身上的装备) 属性(0-10) 操作符(+,-,=) 值(1-100)

### 调整物品新增属性
格式: SetNewItemValueEx 位置( 0-12时是穿在身上的装备) 属性(0-25) 操作符(+,-,=) 值(1-100) 值(1-65535) 时间 秒
SetNewItemValueEx 0 0 + 10 10

### 调整修改下次攻击伤害比例
格式: SetNextDamage 参数1
参数1 下次伤害百分比 不能为0和负数
SetNextDamage 300

### 调整英雄职业[!]
格式: ChangeHeroJob 职业(0,1,2)
ChangeHeroJob 2

### 调整游戏速度
格式: ChangeSpeed 速度类型 速度值 有效时间(秒，该参数为空时表示不限制时间，小退失效)
CHANGESPEED 1 5
ChangeSpeed 2 10 10
SendMsg 5 攻击速度+10！时长10秒！
ChangeSpeed 2 -10 10
SendMsg 5 攻击速度-10！时长10秒！
ChangeSpeed 3 10 10
SendMsg 5 魔法速度+10！时长10秒！
SENDMSG 6 您当前攻击速度(含装备加速)是：<$AttackSpeed>

### 调整装备升级次数[!]
功能: 调整装备升级次数或星星数量.
格式: ChangeItemUpgradeCount 位置(0~37,-1时为OK框物品) (+,-,=) 次数(0~255)
CheckItem 金条 1
Take 金条 1
ChangeItemUpgradeCount 0 + 10
SendMsg 5 盔甲升级次数增加10次

### 通过脚本建立一个NPC 动态创建NPC
格式: CreateNPC NPC名字 地图 坐标X(-1时随机坐标) 坐标Y(-1时随机坐标) 外观 脚本文件 脚本文件是否要加上地图名称(例如.设置为0时脚本文件必须带“-3”如:“传送员-3.txt” 设置为1时脚本文件不需要带“-3”如:“传送员.txt”这样的好处就是，你可以在任意地图地图创建NPC，只要一个脚本“传送员.txt”而不需要“传送员-0.txt、传送员-3.txt”等等好多NPC脚本)
注意:
CreateNPC 测试 3 330 330 8
CreateNPC 测试NPC 3 -1 -1 8
CreateNPC 新的NPC 0 297 624 10026[301,634] 新的NPC 1

### 退出行会前触发
功能:
SENDMSG 7 【提示】禁止退出行会

### 文本字符交替命令
**功能：**
**说明：**
**格式：**
ExchangeLineText 文件名(有盘符是绝对路径) 行数1 变量1 行数2 变量2
CacheExchangeLineText 文件名(有盘符是绝对路径) 行数1 变量1 行数2 变量2
ExchangeLineText d:\a.txt 1 S1 -1 S2
SendMsg 6 已经将d:\a.txt中的第1行和最后1行进行交换，交行后：第1行的值为<$STR(S1)>,最后一行的值为<$STR(S2)>

### 物品标记，装备标记，物品标识，装备标识、
**功能：**
**格式：**
SetItemAddByte 0 0 10
SetItemAddInt 0 0 100
SetItemAddText 0 0 我自己加的文字
GetItemAddByte 0 0 n0
GetItemAddInt 0 0 n1
GetItemAddText 0 0 s1

### 显示倒计时信息提示
功能:
格式:
SENDDELAYMSG 信息内容 时间(秒) 字体颜色 换地图是否删除 跳转字段 X坐标
SENDDELAYMSG 你的礼物在%s后到达 300 255 0 @给礼物

### 新游戏点[!]


### 修改宝宝属性
参数1表示值：
RecalcSlaveAbility 宝宝名（为空表示所有宝宝）
ChangeSlaveAbilityEX 14 -10 1
ChangeSlaveAbilityEX 15 -10 1
ChangeSlaveAbilityEX 30 30
ChangeSlaveAbilityEX 14 -100
ChangeSlaveAbilityEX 15 -100
ChangeSlaveAbilityEX 30 30
格式如下：
ChangeSlaveAbilityEX 14 -10 1
ChangeSlaveAbilityEX 14 +10 1
ChangeSlaveAbilityEX 14 0 1
ChangeSlaveAbilityEX 14 -50
ChangeSlaveAbilityEX 14 +50
ChangeSlaveAbilityEX 14 0

### 修改宝宝外观
ChangeSlaveAppr 脸型 宝宝名（为空或\*，表示所有宝宝，指定名字为指定宝宝） 脸型有效时间（分钟，空或0 表示不检测时间）
ChangeSlaveAppr 72 神兽 60

### 修改地图内怪物属性,修改怪物属性(在原属性的基本上进行加减操作）
格式:格式: ChangeMonAbility 地图名(self：当前所在地图) 怪物名(\*：所有怪物) 参数类型 操作符(+/-/=) 参数值 值类型(0:点;1:百分比) 坐标X 坐标Y 范围 (当坐标及范围均为空时，表示为整个地图，非必要请不要整个地图修改属性，因为消耗性能)
功能说明: 刷新地图内怪物属性
格式: RecalcMonAbility 地图名(self:当前所在地图) 怪物名(\*:所有怪物) X坐标 Y坐标 范围 (当坐标及范围均为空的时候，表示为整个地图，非必要请不要整个地图修改属性，因为消耗性能)
ChangeMonAbility 地图名(self：当前所在地图) 怪物名(\*：所有怪物) 参数类型 操作符(+/=) 参数值（秒，空或0表示不检测时间）
参数1表示值：
ChangeMonAbility 3 白野猪 1 = -50 1 325 323 10
ChangeMonAbility 3 白野猪 4 = -10 0 325 323 10
ChangeMonAbility 3 白野猪 5 = -10 0 325 323 10
ChangeMonAbility 3 白野猪 8 = 50 0 325 323 10
ChangeMonAbility 3 白野猪 9 = 50 0 325 323 10
ChangeMonAbility 3 白野猪 30 + 20
RecalcMonAbility 3 白野猪 325 323 10
ChangeMonAbility 3 白野猪 1 = -50 1 325 323 10
ChangeMonAbility 3 白野猪 4 = -10 0 325 323 10
ChangeMonAbility 3 白野猪 5 = -10 0 325 323 10
ChangeMonAbility 3 白野猪 8 = 50 0 325 323 10
ChangeMonAbility 3 白野猪 9 = 50 0 325 323 10
RecalcMonAbility 3 白野猪 325 323 10

### 修改物品的附加属性值
格式: CHANGEITEMADDVALUE 装备位置(-1时是升级OK框中的装备, boxitem0 -boxitem7是自定义OK框，0-51时是穿在身上的装备) 属性位置(0-18) (符号 + - =) 值
功能：读取物品的附加属性值
格式：GetItemAddValue 装备位置(-1时是升级OK框中的装备, boxitem0 -boxitem7是自定义OK框，0-51时是穿在身上的装备) 属性位置(0-18) 变量名
CheckItemAddValue 0 0 > 1
GETITEMADDVALUE 0 0 <$STR(M10)>

### 修改装备内观和外观命令
外观格式: SetItemShape 位置 操作符(+，-，=) 数值 ;只能改武器和衣服
内观格式:SetItemLooks 位置 操作符(+，-，=) 数值

### 循环脚本运行次数设置
说明：循环脚本运行次数设置
格式：Loopgoto @脚本 脚本运行次数（为空或0时，运行1次）
Loopgoto @运算 100
Inc <$STR(N1)> <$STR(N2)>
Inc N2 1

### 延时移动
**功能:** 延时移动
**格式:**
TIMERECALL 时间(分钟)
SENDMSG 0 [%s]使用了元宝练级卷.进入快速升级地图,1小时后会将您传回土城!

### 验证码功能说明
VerifyCode @回收验证完成

### 移动到回城点
**功能：**
GoHome 5

### 英雄宝宝攻击触发


### 英雄相关命令支持与示范，英雄捡起触发
H.ChangeItemName -1 捡到的<$PICKDROPITEMNAME>
H.UpdateItem -1
SENDMSG 0 玩家<$USERNAME>的英雄在<$MapTitle>坐标<$X>：<$Y>捡到<$PICKDROPITEMNAME>
H.give 屠龙 1
H.ChangeItemNameColor -1 253
H.ChangeItemName -1 屠龙改名
H.updateitem -1

### 永久调整人物属性值
格式: ChangeHumAbilityEX 属性(1-29) 操作符(+ = -) 效果(1-65535)
说明: 属性1-29分别对应值
注意: 此命令是永久增加属性值
ChangeHumAbilityEX 2 + 10

### 永久增加人物属性点(按属性分配点分配)
**功能：**
**格式：**    USEBONUSPOINT 属性位置（1-9） 控制符（+,-,=） 点数
USEBONUSPOINT 1 + 20
SENDMSG 7 攻击力增加20点.
USEBONUSPOINT 2 + 20
SENDMSG 7 魔法力增加20点.
USEBONUSPOINT 3 + 20
SENDMSG 7 道术力增加20点.
USEBONUSPOINT 4 + 20
SENDMSG 7 防御力增加20点.
USEBONUSPOINT 5 + 20
SENDMSG 7 魔防力增加20点.
USEBONUSPOINT 6 + 20
SENDMSG 7 生命值上限增加20点
USEBONUSPOINT 7 + 20
SENDMSG 7 魔法值上限增加20点.
USEBONUSPOINT 8 + 20
SENDMSG 7 准确增加20点.
USEBONUSPOINT 9 + 20
SENDMSG 7 躲避增加20点.

### 游戏币(元宝)控制
**功能：**
**格式：**
GAMEGOLD =
GAMEGOLD +
GAMEGOLD -
**功能：**
**格式：**
AUTOADDGAMEGOLD 控制符(START,STOP)
PARAM1 1
PARAM2 10
AUTOADDGAMEGOLD STOP
**功能：**
**格式：**
AUTOADDGAMEGOLD 控制符(START,STOP)
PARAM1 1
PARAM2 10
AUTOSUBGAMEGOLD STOP

### 游戏窗口标题公告
功能说明：窗口标题公告
格式：SendClientTitleMsg 显示内容
SendClientTitleMsg 显示内容

### 在登陆器里浏览网页
**功能：**
**格式：**
WebBrowser 地址

### 在地图上播放魔法效果[!]
格式: MAPEFFECT 地图名称 X Y WIL文件序号 开始图片数 播放图片张数 播放次数(-1为无限次数) 播放速度(毫秒) 播放效果(0普通 1特效) (该参数值范围0~5，0表示没有亮度，在关闭禁止免蜡时有效) ID 播放顺序(0或空：对象底层；1：对象上层 2：所有对象上层)
MAPEFFECT 3 333 333 0 0 10 1 300 1 0
DelMapEffect 3 333 333 0 0 10 1 300 1 0
MAPEFFECT 3 333 333 1 500 10 -1 300 1 0 1
MAPEFFECT 0 111 111 1 500 10 -1 300 1 0 1
DelMAPEFFECT 0 0 0 0 0 0 0 0 0 0 1

### 在地图上放物品[!]
格式: THROWITEM 地图名称 X坐标 Y坐标 范围 物品名称 数量|时间(此时间不受M2上的爆物品可捡时间控制) 捡取条件（0、1、2、3） 叠加物品是否叠加（0或空：叠加；1非叠加）
Random 100
ThrowItem 3 330 330 10 回城卷 5|60

### 在屏幕上播放魔法效果
格式: SCREENEFFECT 屏幕坐标X 屏幕坐标Y WIL文件序号 开始图片数 播放图片张数 播放次数 播放速度(毫秒) 播放效果(0=普通，1=魔法效果) 模式(0=自己，1=所有人) 播放位置（0或空，在对话框下层播放，1：在对话框上层播放）
SCREENEFFECT 0 0 0 0 10 1 300 0
格式: StopScreenEffect 屏幕坐标X 屏幕坐标Y WIL文件序号 开始图片数 播放图片张数 播放次数(-1和0为不限次数) 播放速度(毫秒) 播放效果(0=普通，1=魔法效果) 模式(0=自己，1=所有人) 播放位置（0或空，在对话框下层播放，1：在对话框上层播放）
StopScreenEffect 0 0 0 0 10 1 300 0
ClearScreenEffect 模式（0：自己；1：屏幕上所有人）

### 在文件的固定行替换写入内容[!]
**功能：**
格式: WriteLine 文件名 行号(0开始) 内容 是否绝对路径(0或空:不是，1:是)说明：说明：文件不存在写入失败，行号从0开始，替换写入，当行不存在时，插入到最后一行
WRITELINE d:\aaaa.txt 1 写入一段文字 1
SENDMSG 6 第2行内容被修改

### 在文件的指定行插入一行内容[!]
**功能：**
格式: InsertLine 文件名 行号(0开始) 内容 是否绝对路径(0或空:不是，1:是)说明：文件不存在写入失败，行号从0开始
InsertLine d:\aaaa.txt 1 插入一行文字 1
SENDMSG 6 第2行插入了新的内容

### 在线命令弹出菜单功能
**功能：**
**格式：**

### 在线泡经验
**功能：**
**格式：例：（等级30级以上，地图3安全区内每1秒种得到10个经验点）****==================================================**
参数一：间隔时间
参数二：获得经验值
参数三：是否安全区（0为任何地方）
参数四：地图号（\*为任何地图）
参数五：是否允许英雄分配经验（0为禁止）
参数六：是否允许将经验存放聚灵珠（1为允许，留空或0为不允许）
参数七：泡点有效时间（秒；为0或空表示泡点一直有效）
参数八：100为限制泡点等级（参数8等级限制(0为不限制 填写100 则表示小于100级才会获得经验 到100级了就不加经验了 命令自动结束)

### 在线修改宝宝名字[!]
**功能：**
**格式：ChangeBmz 新名字 原有名字 （如果原有名字为空，则把所有宝宝的名字都改成新名字）**
ChangeBmz 超级神兽
SendMsg 5 你所有宝宝名字修改为超级神兽！
CHECKSLAVENAME 神兽
ChangeBmz 超级神兽 神兽
SendMsg 5 你的神兽宝宝名字成功修改为超级神兽！
SENDMSG 5 提示:你的宝宝名字不叫神兽

### 暂停刷怪,停止刷怪
说明: 暂停游戏刷怪
StopM2MakeMon 参数1(0:不暂停；1:暂停)
StopM2MakeMon 0
StopM2MakeMon 1

### 增加附加伤害效果
格式: RangeHarm 参数1 参数2 参数3 参数4 参数5 参数6....参数12
说明：
RangeHarm 参数1 参数2 参数3 参数4 参数5 参数6.....参数12
参数1 X坐标
参数2 Y坐标
参数3 范围
参数4 伤害值
参数5 附加效果 0=无，1=击退，2=冻结，3=麻痹，4=吸血，5=吸蓝,6真实伤害,7石化, 8冰冻,9蛛网效果,10红毒, 11绿毒,12定身,13瘫痪,14防禁锢,15最大hp百分比真实伤害,16当前hp百分比真实伤害
参数6 附加属性值 分别对应参数5= 1;击退距离 、2;冻结时间 、3;麻痹时间、4;吸血值、5;吸蓝值、6;真实伤害值（真实伤害无视防御不无视护身）、7;石化时间、8;冰冻时间、9;蛛网时间、10;红毒时间、
参数7 是否检查防冻结/麻痹/石化/冰冻/蛛网/红毒/绿毒属性（0: 直接设置状态; 1：检查后设置状态)
参数8 目标(0或空:所有目标; 1:仅人物; 2:仅怪物)
参数9 WIL序号
参数10 开始图片
参数11 播放张数
参数12 播放速度
参数13 是否透明绘制(0或空，1)
参数14 是否物理属性攻击(0或空，1 物理属性则目标以防御来抵御伤害，0或者空目标则以魔御来抵御伤害)
RangeHarm 333 333 8 100 1 5 0 0
参数1 X坐标
参数2 Y坐标
参数3 范围
参数4 伤害值
参数5 附加效果 0=无；1=击退，2=冻结，3=麻痹，4=吸血，5=吸蓝, 6真实伤害, 7.石化 8.冰冻 9.蛛网效果 10.红毒 11.绿毒, 12.定身 13.瘫痪 14.防禁锢,15最大hp百分比真实伤害,16当前hp百分比真实伤害
参数6 附加属性值 分别对应参数5= 1;击退距离 、2;冻结时间 、3;麻痹时间、4;吸血值、5;吸蓝值、6;真实伤害值（真实伤害无视防御不无视护身）、7;石化时间、8;冰冻时间、9;蛛网时间、10;红毒时间、
参数7 是否检查防冻结/麻痹/石化/冰冻/蛛网/红毒/绿毒属性（0: 直接设置状态; 1：检查后设置状态)
参数8 目标(0或空: …[截断]

### 增加会员时间[!]
CHECKNAMEDATETIMELIST ..\QuestDiary\会员名单.txt 1 <$STR(S1)> <$STR(N1)> <$STR(N2)> <$STR(N3)>
ADDNAMEDATETIMELIST ..\QuestDiary\会员名单.txt 30 0 0
SENDMSG 5 <$USERNAME>会员充值成功，增加30天0小时0分会员时间！
SENDMSG 6 你的会员到期时间是<$STR(S1)>【剩余天数=<$STR(N1)>】【剩余小时=<$STR(N2)>】【剩余分钟=<$STR(N3)>】 255 253
SENDMSG 6 你不是会员或已过期，请及时充值！ 255 253

### 增加人物IP在列表中
**功能：**
**功能：

### 增加人物名在列表中
**功能：**
**格式：

### 增加人物帐号在列表中
**功能：**
**功能：

### 增加隐藏元素属性
格式: AddHumNewValue 属性(0-20) 操作符(+,-,=) 值(1-100) 时间(1-21亿秒，时间留空则为在线一直有效)
AddHumNewValue 属性(0-20) 操作符(+,-,=) 值(1-100)
说明：此命令只调整本命令对应的元素属性值，而不会改变装备自带的属性值

### 战斗力计算
功能说明：位于引擎---选项--战斗力计算设置 用于计算战斗力总值
Inc N0 10
SENDMSG 6 你的战斗力为<$CombatPower>
Inc N0 10
SENDMSG 6 你英雄的战斗力为<$H.CombatPower>

### 掌门人踢出行会成员前触发
功能:
SENDMSG 7 【提示】禁止退出行会

### 召唤指定怪物为宝宝
**功能：**
**格式：**RECALLMOB 怪物名称 宝宝等级(最高为 7) 叛变时间(分钟)
CHECKSLAVECOUNT < 5
RECALLMOB 神兽 7 30

### 致命一击触发，暴击触发
**说明：**    致命一击打出触发，暴击打出触发
SENDMSG 6 物理攻击触发暴击
SENDMSG 6 魔法攻击触发暴击
SENDMSG 6 物理攻击触发致命一击
SENDMSG 6 魔法攻击触发致命一击
SENDMSG 6 英雄物理攻击触发暴击
SENDMSG 6 英雄魔法攻击触发暴击
SENDMSG 6 英雄物理攻击触发致命一击
SENDMSG 6 英雄魔法攻击触发致命一击

### 重新分配人物附加属性点
功能：
格式：
相关命令：

### 转换职业
**功能：**
**格式：**    CHANGEJOB

### 装备名称自定义系统
功能：
格式：
SETSCRIPTFLAG 1 1
SETSCRIPTFLAG 1 1

### 装备属性升级
**命令格式**
UPGRADEITEMEX 物品位置(0-12) 属性位置(0-17) 成功机率(0-100) 点数机率(0-255) 是否破碎(0,1) 是否显示文字信息(0,1)
H.UPGRADEITEMEX 物品位置(0-12) 属性位置(0-17) 成功机率(0-100) 点数机率(0-255) 是否破碎(0,1) 是否显示文字信息(0,1)

### 装备投保功能
SETINSURANCECOUNTXX 位置 操作符(+，-，=) 数值
GETINSURANCECOUNTXX 位置 变量
H.SETINSURANCECOUNTXX 位置 操作符(+，-，=) 数值
H.GETINSURANCECOUNTXX 位置 变量
相关常量：

### 自定义OK框[!]
ReturnBoxItem (0~31)
CheckBoxItemCount OK框编号(0~31) 物品数量(该参数只有是叠加物品时才会有效)
NOT Equal <$BOXITEM[0].NAME>
SetUpgradeItem 0
CHANGEITEMNAMECOLOR boxitem0 253
CHANGEITEMUPGRADECOUNT boxitem0 + 1
ChangeItemName boxitem0 <$BOXITEM[0].NAME>+1
SetNewItemValue boxitem0 0 + 1
UpdateItem boxitem0
ReturnBoxItem 0
SENDMSG 6 装备升级成功
SENDMSG 6 请放入需要升级的装备
GiveBoxItem 0 怒斩
SendMsg 5 恭喜：OK框0成功放入怒斩！
功能：通过唯一ID将物品放入OK框
GiveOnItem 装备位置 物品名称 数量默认写1(数量大于1时只对OK框叠加物品有效) 参数4 参数5 参数6 参数7 参数8 参数9
参数4-参数9 参考 GIVE的扩展
CHECKBAGITEMCOUNTEX 物品名称 数量

### 自定义UI中自定义按钮使用,预留按钮
SENDMSG 7 按钮点击编号为<$CustomButtonID>
SENDMSG 7 你触发了50编号的按钮
ShowCustomButton 编号 显示/隐藏(0:隐藏， 1:显示）
SENDMSG 7 你触发了他人装备栏自定义按钮1
SENDMSG 7 他人名称<$USERSTATENAME>

### 自定义变量按变量值大小排序[!]
功能：
格式：
SortVarToList 自定义变量名 自定义变量文件路径 排序后列表的保存路径 降序还是升序(0,1) 保存格式(0,1)为0时只保存人物名,为1时:人物名 变量值. 自定义变量文件是否绝对路径(0,1) 保存文件是否绝对路径(0,1)
SortVarToList LJSQZS .\QuestDiary\数据文件\Test.txt ..\QuestDiary\数据文件\排序的文件.txt 0 1

### 自定义变量功能
**功能：**
CALCVAR HUMAN QQQQ +
CALCVAR HUMAN
QQQQ - 5
CHECKVAR HUMAN
QQQQ = 5
CHECKVAR HUMAN QQQQ >
CHECKVAR HUMAN QQQQ <
DEC QQQQ 1
INC QQQQ 1
LOADVAR HUMAN QQQQ
GOTO @varcontrol
SAVEVAR HUMAN QQQQ
GOTO @varcontrol
VAR Integer HUMAN QQQQ

### 自动穿取装备
**功能：**
**格式：**    穿装备 TakeOnItem  装备名称 位置(0-12)
TakeOnItem 天魔神甲 0
TakeOffItem 0

### 自动穿装备和取装备
AutoTakeOnItem 装备名称 位置(0-12)
AutoTakeOffItem 装备名称 位置(0-12)如不能正常脱请删除装备名字，只需位置即可

### 自动行走
AUTOGOTOXY 3 330 330

### 自动替换装备
格式：
参数1 ：为0或空时静默替换。参数为1时则提示替换
参数2 ： 有效时间 1-65535分钟 0或空不限制时间
参数3： 替换对话框倒计时时间（如果填0，建议直接用静默的方式）
参数4： 0或空自动替换，1为不替换，到时间直接关闭提示窗口
OpenAutoUsePickItem 1 60 5
H.OpenAutoUsePickItem 0

### 字符串分隔命令
ExtractStringEx | aaa|bbb|ccc|ddd|000 S11
SendMsg 6 <$STR(S11)>,<$STR(S12)>,<$STR(S13)>,<$STR(S14)>,<$STR(S15)>
ExtractStringEx | aaa|bbb|ccc|ddd|000 S$拆分
SendMsg 4 <$STR(S$拆分1)>,<$STR(S$拆分2)>,<$STR(S$拆分3)>,<$STR(S$拆分4)>,<$STR(S$拆分5)>
GetDBItemFieldValue <$STR(S$奖励内容<$str(p1)>)> idx N$签到奖励<$str(p1)>
GetDBItemFieldValue <$STR(S$奖励内容<$str(p1)>)> idx s1
MOV S$奖励内容 麻痹戒指,圣战戒指,裁决之杖,屠龙
ExtractStringEx , <$STR(S$奖励内容)> S$奖励内容
MOV P1 1
WHILE P1 < 3
GetDBItemFieldValue <$STR(S$奖励内容<$str(p1)>)> idx s1
INC P1 1

### 字符串分隔命令
GetRandomText ..\QuestDiary\装备列表.txt S0 0
EXTRACTSTRING : <$STR(S0)> s1 s2 s3 s4 s5 s6 s7 s8
GIVE <$STR(S1)> 1
GIVE <$STR(S2)> 1
GIVE <$STR(S3)> 1
GIVE <$STR(S4)> 1
GIVE <$STR(S5)> 1
GIVE <$STR(S6)> 1
GIVE <$STR(S7)> 1
GIVE <$STR(S8)> 1
TakeOn <$STR(S1)> 0
TakeOn <$STR(S2)> 1
TakeOn <$STR(S3)> 3
TakeOn <$STR(S4)> 4
TakeOn <$STR(S5)> 5
TakeOn <$STR(S6)> 6
TakeOn <$STR(S7)> 7
TakeOn <$STR(S8)> 8
ExtractStringEx | aaa|bbb|ccc|ddd|000 S11
SendMsg 6 <$STR(S11)>,<$STR(S12)>,<$STR(S13)>,<$STR(S14)>,<$STR(S15)>
ExtractStringEx | aaa|bbb|ccc|ddd|000 S$拆分
SendMsg 4 <$STR(S$拆分1)>,<$STR(S$拆分2)>,<$STR(S$拆分3)>,<$STR(S$拆分4)>,<$STR(S$拆分5)>

### 字符检测命令GetStringPosEX
**功能：**
**格式：
GetStringPosEX A B C D E F
参数A：文件路径
参数B：检测字符(支持变量、支持大小写字母、支持数字)
参数C：N1返回检测的字符所在的行数(N变量不是固定，可以更换其它数字型变量)
参数D：S1返回检测的字符所在的行数(S变量不是固定，可以更换其它字符型变量)
参数E：是否绝对路径(0:相对路径 1:绝对路径)两种模式
参数F：匹配模式(0或空:包含匹配; 1:完全匹配)
GetStringPosEX ..\QuestDiary\测试.txt 管理员1号 N1 S1 0
SendMsg 5 字符在文本中的行数:<$STR(N0)>，本行所有内容是:<$STR(S1)>。
SendMsg 5 字符不在测试.txt文本中。
GetStringPosEX ..\QuestDiary\111.txt aabb N1 S1 0