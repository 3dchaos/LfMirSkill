# Npc文字Text使用

**功能：**
    Npc对话框文字Text运用

**功能：设置文字在对话框中坐标、颜色、字体大小、字体、粗体显示.**

说明：




格式：Text:文字:提示:X:Y{FCOLOR=250;FSIZE=14;FNAME=黑体;FBOLD=1}/@测试

示范： <Text:文字内容|提示:0:0{FCOLOR=250;FSIZE=14;FNAME=黑体}/@测试> \ \


**绝对坐标示范：** <&Text:绝对坐标|提示:0:0{FCOLOR=250;FSIZE=14;FNAME=黑体}/@测试> \ \





**字体25号，加粗，楷体，变色显示**
<Text:绝对坐标|提示:30:20{AUTOCOLOR=254,251,168,191,250,70,245,249,253;FSIZE=25;FNAME=楷体;FBOLD=1}/@测试> \ \\ \\ \



**颜色253，字体25号，宋体**
<Text:测试下这段文字的显示|提示信息:10:20{FCOLOR=253;FSIZE=25;FNAME=宋体}/@测试>





参数说明:
AUTOCOLOR 彩色字体设置
FSIZE 字体大小
FNAME 字体类型
FBOLD 字体加粗
FCOLOR 字体颜色
