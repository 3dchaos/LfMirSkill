# NPC对话框提示文字命令，NPC界面上向上滚动提示信息

功能说明：NPC界面上向上滚动提示信息

格式：SENDMOVEHINTMSG 文字信息 文字颜色 背景颜色 X坐标 Y坐标 停留时间(秒；0或空默认3秒)

文字换行：\



[@5555]
#IF
checkgold 2500000
#ACT
#ELSEACT
SENDMOVEHINTMSG 金币不足\金币不足 249 0 10 60



[@55555]
#IF
checkgold 2500000
#ACT
#ELSEACT
;停留5秒消失
SENDMOVEHINTMSG 金币不足\金币不足 249 0 10 60 5
