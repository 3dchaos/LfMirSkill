# GetPlayInfo命令使用大全

说明: GetPlayInfo命令使用大全(部分可能无效，按需使用)




[@main]
<玩家名/@玩家名>
<玩家机器硬盘序列号/@玩家机器硬盘序列号>
<玩家机器网卡序列号/@玩家机器网卡序列号>
<当前登录器版本号/@当前登录器版本号> \
<玩家账号/@玩家账号>
<玩家登录IP/@玩家登录IP>
<玩家IP所在地/@玩家IP所在地>
<玩家当前地图编号/@玩家当前地图编号>
<玩家当前地图描述/@玩家当前地图描述> \
<玩家当前X坐标/@玩家当前X坐标>
<玩家当前Y坐标/@玩家当前Y坐标>
<玩家当前方向/@玩家当前方向>
<玩家英雄当前方向/@玩家英雄当前方向>
yin
<玩家当前职业/@玩家当前职业>
<玩家性别/@玩家性别>
<玩家发型/@玩家发型> \
<玩家金币数量/@玩家金币数量>
<玩家灵符数量/@玩家灵符数量>
<玩家等级/@玩家等级>
<玩家当前经验值/@玩家当前经验值>
<玩家升级所需经验/@玩家升级所需经验> \
<玩家防御下限/@玩家防御下限>
<玩家防御上限/@玩家防御上限>
<玩家魔御下限/@玩家魔御下限>
<玩家魔御上限/@玩家魔御上限> \
<玩家攻击下限/@玩家攻击下限>
<玩家攻击上限/@玩家攻击上限>
<玩家魔法力下限/@玩家魔法力下限>
<玩家魔法力上限/@玩家魔法力上限>
<玩家道术下限/@玩家道术下限> \
<玩家道术上限/@玩家道术上限>
<玩家当前HP值/@玩家当前HP值>
<当前最大HP值/@当前最大HP值>
<当前MP值/@当前MP值> \
<当前最大MP值/@当前最大MP值>
<当前负重量/@当前负重量>
<当前最大负重量/@当前最大负重量>
<当前穿重量/@当前穿重量>
<当前最大可穿重量/@当前最大可穿重量> \
<当前腕力/@当前腕力>
<当前最大腕力/@当前最大腕力>
<人物回城点地图编号/@人物回城点地图编号>
<人物回城点X坐标/@人物回城点X坐标> \
<人物回城点Y坐标/@人物回城点Y坐标>
<人物PK值/@人物PK值>
<人物声望值/@人物声望值>
<人物转生等级/@人物转生等级> \
<人物元宝数量/@人物元宝数量>
<人物游戏点/@人物游戏点>
<人物背包空格数/@人物背包空格数>
<人物在线时长(分)/@人物在线时长(分)> \
<会员类型/@会员类型>
<会员等级/@会员等级>
<宝宝数量/@宝宝数量>
<夫妻对方姓名/@夫妻对方姓名> \
<师父名字/@师父名字>
<玩家仓库密码/@玩家仓库密码>
<行会名/@行会名>
<行会封号的编号/@行会封号的编号>
<还未分配的属性点/@还未分配的属性点> \
<已分配的属性点/@已分配的属性点>
<玩家组队队员数/@玩家组队队员数>
<组队队长姓名/@组队队长姓名>
<攻击模式编号/@攻击模式编号> \
<镖车的名字/@镖车的名字>
<玩家挂机的留言/@玩家挂机的留言>
<玩家贡献度/@玩家贡献度>
<幸运值/@幸运值> \


[@玩家名]
#ACT
GetPlayInfo Name S1
SENDMSG 6 玩家名<$STR(S1)>

[@玩家机器硬盘序列号]
#ACT
GetPlayInfo IDE S1
SENDMSG 6 玩家机器硬盘序列号<$STR(S1)>

[@玩家机器网卡序列号]
#ACT
GetPlayInfo NIC S1
SENDMSG 6 玩家机器网卡序列号<$STR(S1)>

[@当前登录器版本号]
#ACT
GetPlayInfo VER S1
SENDMSG 6 当前登录器版本号<$STR(S1)>

[@玩家账号]
#ACT
GetPlayInfo ID S1
SENDMSG 6 玩家账号<$STR(S1)>

[@玩家登录IP]
#ACT
GetPlayInfo IP S1
SENDMSG 6 玩家登录IP<$STR(S1)>

[@玩家IP所在地]
#ACT
GetPlayInfo IPLOCAL S1
SENDMSG 6 玩家IP所在地<$STR(S1)>

[@玩家当前地图编号]
#ACT
GetPlayInfo Map S1
SENDMSG 6 玩家当前地图编号<$STR(S1)>

[@玩家当前地图描述]
#ACT
GetPlayInfo MapName S1
SENDMSG 6 玩家当前地图描述<$STR(S1)>

[@玩家当前X坐标]
#ACT
GetPlayInfo X N1
SENDMSG 6 玩家当前X坐标<$STR(N1)>

[@玩家当前Y坐标]
#ACT
GetPlayInfo Y N1
SENDMSG 6 玩家当前Y坐标<$STR(N1)>

[@玩家英雄当前方向]
#ACT
GetPlayInfo H.Dir N1
SENDMSG 6 玩家英雄当前方向<$STR(N1)>


[@玩家当前方向]
#ACT
GetPlayInfo Dir N1
SENDMSG 6 玩家当前方向<$STR(N1)>


[@玩家当前职业]
#ACT
GetPlayInfo Job N1
SENDMSG 6 玩家当前职业<$STR(N1)>

[@玩家性别]
#ACT
GetPlayInfo sex N1
SENDMSG 6 玩家性别<$STR(N1)>

[@玩家发型]
#ACT
GetPlayInfo Hair N1
SENDMSG 6 玩家发型<$STR(N1)>

[@玩家金币数量]
#ACT
GetPlayInfo Gold N1
SENDMSG 6 玩家金币数量<$STR(N1)>

[@玩家灵符数量]
#ACT
GetPlayInfo GameGird N1
SENDMSG 6 玩家灵符数量<$STR(N1)>

[@玩家等级]
#ACT
GetPlayInfo Level N1
SENDMSG 6 玩家等级<$STR(N1)>

[@玩家当前经验值]
#ACT
GetPlayInfo Exp N1
SENDMSG 6 玩家当前经验值<$STR(N1)>

[@玩家升级所需经验]
#ACT
GetPlayInfo MAXEXP N1
SENDMSG 6 玩家升级所需经验<$STR(N1)>

[@玩家防御下限]
#ACT
GetPlayInfo AC N1
SENDMSG 6 玩家防御下限<$STR(N1)>

[@玩家防御上限]
#ACT
GetPlayInfo MAXAC N1
SENDMSG 6 玩家防御上限<$STR(N1)>

[@玩家魔御下限]
#ACT
GetPlayInfo MAC N1
SENDMSG 6 玩家魔御下限<$STR(N1)>

[@玩家魔御上限]
#ACT
GetPlayInfo MAXMAC N1
SENDMSG 6 玩家魔御上限<$STR(N1)>

[@玩家攻击下限]
#ACT
GetPlayInfo DC N1
SENDMSG 6 玩家攻击下限<$STR(N1)>

[@玩家攻击上限]
#ACT
GetPlayInfo MAXDC N1
SENDMSG 6 玩家攻击上限<$STR(N1)>

[@玩家魔法力下限]
#ACT
GetPlayInfo MC N1
SENDMSG 6 玩家魔法力下限<$STR(N1)>

[@玩家魔法力上限]
#ACT
GetPlayInfo MACMC N1
SENDMSG 6 玩家魔法力上限<$STR(N1)>

[@玩家道术下限]
#ACT
GetPlayInfo SC N1
SENDMSG 6 玩家道术下限<$STR(N1)>

[@玩家道术上限]
#ACT
GetPlayInfo MAXSC N1
SENDMSG 6 玩家道术上限<$STR(N1)>

[@玩家当前HP值]
#ACT
GetPlayInfo HP N1
SENDMSG 6 玩家当前HP值<$STR(N1)>

[@当前最大HP值]
#ACT
GetPlayInfo MAXHP N1
SENDMSG 6 当前最大HP值<$STR(N1)>

[@当前MP值]
#ACT
GetPlayInfo MP N1
SENDMSG 6 当前MP值<$STR(N1)>

[@当前最大MP值]
#ACT
GetPlayInfo MAXMP N1
SENDMSG 6 当前最大MP值<$STR(N1)>

[@当前负重量]
#ACT
GetPlayInfo WEIGHT N1
SENDMSG 6 当前负重量<$STR(N1)>

[@当前最大负重量]
#ACT
GetPlayInfo MAXWEIGHT N1
SENDMSG 6 当前最大负重量<$STR(N1)>

[@当前穿重量]
#ACT
GetPlayInfo WEARWEIGHT N1
SENDMSG 6 当前穿重量<$STR(N1)>

[@当前最大可穿重量]
#ACT
GetPlayInfo MAXWEARWEIGHT N1
SENDMSG 6 当前最大可穿重量<$STR(N1)>

[@当前腕力]
#ACT
GetPlayInfo HANDWEIGHT N1
SENDMSG 6 当前腕力<$STR(N1)>

[@当前最大腕力]
#ACT
GetPlayInfo MAXHANDWEIGHT N1
SENDMSG 6 当前最大腕力<$STR(N1)>

[@人物回城点地图编号]
#ACT
GetPlayInfo HOMEMAP S1
SENDMSG 6 人物回城点地图编号<$STR(S1)>

[@人物回城点X坐标]
#ACT
GetPlayInfo HOMEX N1
SENDMSG 6 人物回城点X坐标<$STR(N1)>

[@人物回城点Y坐标]
#ACT
GetPlayInfo HOMEY N1
SENDMSG 6 人物回城点Y坐标<$STR(N1)>

[@人物PK值]
#ACT
GetPlayInfo PK N1
SENDMSG 6 人物PK值<$STR(N1)>

[@人物声望值]
#ACT
GetPlayInfo CREDITPOINT N1
SENDMSG 6 人物声望值<$STR(N1)>

[@人物转生等级]
#ACT
GetPlayInfo RELEVEL N1
SENDMSG 6 人物转生等级<$STR(N1)>

[@人物元宝数量]
#ACT
GetPlayInfo GAMEGOLD N1
SENDMSG 6 人物元宝数量<$STR(N1)>

[@人物游戏点]
#ACT
GetPlayInfo GAMEPOINT N1
SENDMSG 6 人物游戏点<$STR(N1)>

[@人物背包空格数]
#ACT
GetPlayInfo BAGSIZE N1
SENDMSG 6 人物背包空格数<$STR(N1)>

[@人物在线时长(分)]
#ACT
GetPlayInfo LOGINLONGMIN N1
SENDMSG 6 人物在线时长(分)<$STR(N1)>

[@会员类型]
#ACT
GetPlayInfo MEMBERTYPE N1
SENDMSG 6 会员类型<$STR(N1)>

[@会员等级]
#ACT
GetPlayInfo MEMBERLEVEL N1
SENDMSG 6 会员等级<$STR(N1)>

[@宝宝数量]
#ACT
GetPlayInfo SLAVECOUNT N1
SENDMSG 6 宝宝数量<$STR(N1)>

[@夫妻对方姓名]
#ACT
GetPlayInfo DEARNAME S1
SENDMSG 6 夫妻对方姓名<$STR(S1)>

[@师父名字]
#ACT
GetPlayInfo MASTERNAME S1
SENDMSG 6 师父名字<$STR(S1)>

[@玩家仓库密码]
#ACT
GetPlayInfo STORAGEPWD S1
SENDMSG 6 玩家仓库密码<$STR(S1)>

[@行会名]
#ACT
GetPlayInfo GUILDNAME S1
SENDMSG 6 行会名<$STR(S1)>

[@行会封号的编号]
#ACT
GetPlayInfo GUILDRANKNO N1
SENDMSG 6 行会封号的编号<$STR(N1)>

[@还未分配的属性点]
#ACT
GetPlayInfo BONUSPOINT N1
SENDMSG 6 还未分配的属性点<$STR(N1)>

[@已分配的属性点]
#ACT
GetPlayInfo BONUSPOINTEX N1
SENDMSG 6 已分配的属性点<$STR(N1)>

[@玩家组队队员数]
#ACT
GetPlayInfo GROUPCOUNT N1
SENDMSG 6 玩家组队队员数<$STR(N1)>


[@组队队长姓名]
#ACT
GetPlayInfo GROUPOWNER S1
SENDMSG 6 组队队长姓名<$STR(S1)>

[@攻击模式编号]
#ACT
GetPlayInfo ATTACKMODE N1
SENDMSG 6 攻击模式编号<$STR(N1)>

[@镖车的名字]
#ACT
GetPlayInfo CARNAME S1
SENDMSG 6 镖车的名字<$STR(S1)>

[@玩家挂机的留言]
#ACT
GetPlayInfo OFFTALK S1
SENDMSG 6 玩家挂机的留言<$STR(S1)>

[@玩家贡献度]
#ACT
GetPlayInfo CONTRIBUTE N1
SENDMSG 6 玩家贡献度<$STR(N1)>

[@幸运值]
#ACT
GetPlayInfo LUCK N1
SENDMSG 6 幸运值<$STR(N1)>
