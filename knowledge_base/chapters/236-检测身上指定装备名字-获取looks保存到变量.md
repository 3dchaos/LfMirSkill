# 检测身上指定装备名字 获取looks保存到变量

**功能：**
    检测身上指定装备名字 获取looks保存到变量

格式: CheckItemwLooks 装备名称 变量名(变量名可以不填)
有指定装备返回真，否则返回假

[@main]
#IF
CheckItemwLooks 传送戒指 N0
#ACT
SENDMSG 0 测试成功<$Str(n0)>
