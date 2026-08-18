# 地图参数限制人物在地图的时间（TimeMap）

功能: 使用地图参数限制角色在地图内时间

格式:TimeMap(3|5|1|@计时地图返回)

参数一到时间返回的地图代码
参数二 倒计时时间分钟计算
参数三 是否显示当前地图剩余倒计时
参数四 退出地图触发QF字段


（MapInfo.txt)

[G001 质询屋] SAFE DAY QUIZ NOMANNOMON TimeMap(3|5|1)

OR

[G001 质询屋] SAFE DAY QUIZ NOMANNOMON TimeMap(3|5|1|@计时地图返回)

QFunction-0.txt
[@计时地图返回]
#IF
#ACT
Sendmsg 5 返回地图。
;从地图出来时候触发，无论在线到时间出来还是小退后自动出地图，只要出地图就触发
