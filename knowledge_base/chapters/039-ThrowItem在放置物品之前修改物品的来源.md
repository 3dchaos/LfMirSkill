# ThrowItem在放置物品之前修改物品的来源

功能说明：使用ThrowItem命令放置物品之前修改物品的来源

命令：SetThrowItemFrom 物品来源(0-9) 地图号 怪物人 杀人者 日期(yyyy-mm-dd) 时间(hh:nn:ss)

物品来源代码：
0未知; 1:GM制造; 2:脚本; 3:商店购买; 4:打怪掉落; 5:系统给予; 6:挖矿得到; 7:宝箱取得; 8:挖肉得到; 9捕捉得到

说明：本命令只对设置后的一条ThrowItem生效。执行一次ThrowItem后，设置还原。



-----------------------------------------------------------------------------

示范：

[@物品]
#if
#act
SetThrowItemFrom 4 3 白野猪 杀人者 2021-01-11 10:00:00
ThrowItem <$map> <$x> <$y> 1 屠龙 1|0


[@KillMon]
#if
#act
SetThrowItemFrom 4 3 白野猪 杀人者 <$Date> <$Time>
THROWITEM <$MAP> <$KILLMONX> <$KILLMONY> 1 力量戒指 1|120 2 1
sendmsg 7 测试下放置物品修改来源
SENDMSG 6 当前日期：<$Date>；当前时间<$Time>
