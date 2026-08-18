# 扩展check支持批量检测个人标识

**扩展check支持批量检测**






check支持批量检测

多个非连续的标识可以用逗号隔开，连续可用 - 串联
格式：check [1,2,4-6,8] 1

#if
check [1,2,4-6,8] 1
#act
SENDMSG 6 1,2,4,5,6,8全为1




**SET支持批量设置个人标识**

格式：
SET [1,2,4-6,8] 1
SET [1,2,4-6,<$STR(N$变量)>] 1



**个人标识取反 set [n] -1**

; 新增方式 set [n] -1

[@main1]
个人标识9的值为：<$flag(9)> \
<修改flag\_9/@修改flag9>\
<flag取反\_9/@取反flag9>

[@取反flag9]
#act
set [9] -1
goto @main1

[@修改flag9]
#IF
check [9] 0
#act
set [9] 1
goto @main1
#elseact
set [9] 0
goto @main1



**特别注意：个人标识从1开始，0是无效的！！！**
