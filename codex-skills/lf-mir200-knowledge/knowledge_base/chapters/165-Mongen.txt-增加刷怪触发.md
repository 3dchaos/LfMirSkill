# Mongen.txt 增加刷怪触发

**功能：**

Mongen.txt 刷怪触发

**格式：**
Mongen.txt 增加刷怪触发



Mongen.txt 文件内容如下：
3 180 275 毒蜘蛛 2 4 1 100 249 0 0 0 0 0 @刷毒蜘蛛

------------------
;QF触发：

[@刷毒蜘蛛]
#if
#act
SENDMOVEMSG 0 251 0 50 1 {【世界BOSS全服提示】:/SCOLOR=70}{『<$RegMonName>』/SCOLOR=250}已出世，位于地图<$RegMonMap>(<$RegMonMapDesc>)，坐标<$RegMonX>:<$RegMonY>，赶紧抢！！！





################################################满足G变量刷怪##################################################

G变量 操作符(>,<,=,>=,<=) 数值

Mongen.txt 文件内容如下：
3 180 275 毒蜘蛛 2 4 1 100 249 0 0 0 0 0 @刷毒蜘蛛 G9 > 9

;G9变量大于9刷怪
------------------
;QF触发：

[@刷毒蜘蛛]
#if
#act
SENDMOVEMSG 0 251 0 50 1 {【世界BOSS全服提示】:/SCOLOR=70}{『<$RegMonName>』/SCOLOR=250}已出世，位于地图<$RegMonMap>(<$RegMonMapDesc>)，坐标<$RegMonX>:<$RegMonY>，赶紧抢！！！





**变量说明**

<$RegMonName>：当前怪物
<$RegMonMap>： 地图号
<$RegMonMapDesc>：地图名
<$RegMonX>：刷怪X
<$RegMonY>：刷怪Y



**适用于单个刷怪，或极少数刷怪，也就是BOSS刷新触发，如果刷怪数量太大，超过死循环设置数量将被提示死循环**




。
;==========================================
