# HTTP请求与JSON处理功能说明

﻿

HTTP请求与JSON处理功能说明

# HTTP请求与JSON处理功能说明

```
功能说明：向指定网络地址提交数据

参数说明
HttpGet 请求地址 NPC触发标签 返回内容保存到变量

HttpPost 请求地址 请求体内容 请求体类型 NPC触发标签 返回内容保存到变量
请求体类型 支持
- form：按表单发送，自动编码 key/value
- json：按 application/json; charset=utf-8 发送，正文自动转 UTF-8
- text：按 text/plain; charset=utf-8 发送，正文自动转 UTF-8

执行结果

- 请求在线程里异步执行
- 成功或失败后，都会把返回文本写入 内容保存到变量
- 然后跳转到 NPC触发标签

;------------------------------------------------------------------------------------------------------------------

[@HttpGet请求]
#ACT
HttpGet https://webhook.site/b42ecf85-b0eb-4aa2-88d0-b31e382e4cc7 @HttpGetBack S100
BREAK

[@HttpGetBack]
#SAY
Get返回:\
<$STR(S100)>

;------------------------------------------------------------------------------------------------------------------

[@HttpPost提交表单]
HttpPost https://postman-echo.com/post p1=请求内容&p2=22344 form @PostFormBack S100

[@PostFormBack]
#SAY
Post表单返回:\
<$STR(S100)>

;------------------------------------------------------------------------------------------------------------------

[@HttpPost提交JSON]
#ACT
HttpPost https://postman-echo.com/post {"username":"lfm2","msg":"你好"} json @PostJsonBack S100

[@PostJsonBack]
#ACT
JsonGetNodeValue S100 data.username S1
JsonGetNodeValue S100 data.msg S2
#SAY
UserName:<$STR(S1)>\
Msg:<$STR(S2)>\
Post Json返回:\
<$STR(s100)>

;------------------------------------------------------------------------------------------------------------------

[@HttpPost提交Text]
#ACT
HttpPost https://postman-echo.com/post 这是一段普通文本 text @PostTextBack S100
BREAK

[@PostTextBack]
#SAY
Post Text返回:\
<$STR(S100)>

========================分界线====================================================================

下面所有示例中，Json内容(S1)中为:{"user":{"name":"tom","level":55,"items":[1001,1002,1003],"info":{"vip":1},"remark":null}}

•• 条件命令

1、检查某个节点是否存在：CheckJsonNodeExists Json内容 节点路径
- 说明：节点值是 null 时，也算存在
- 示例：
#IF
CheckJsonNodeExists S1 user.name
#ACT
SENDMSG 6 user.name 存在

2、检测指定节点是否存在且为数组：CheckJsonNodeIsArray Json内容 节点路径
- 示例：
#IF
CheckJsonNodeIsArray S1 user.items
#ACT
SENDMSG 6 user.items 是数组

3、检测指定节点是否存在且为对象：CheckJsonNodeIsObject Json内容 节点路径
- 示例：
#IF
CheckJsonNodeIsObject S1 user.info
#ACT
SENDMSG 6 user.info 是对象

4、检测指定节点是否存在且值为null：CheckJsonNodeIsNull Json内容 节点路径
- 示例：
#IF
CheckJsonNodeIsNull S1 user.remark
#ACT
SENDMSG 6 user.remark 是 null

--------------------------------------------------------------------------------------------

••动作命令

1、获取节点值并写入变量：JsonGetNodeValue Json内容 节点路径 输入变量 默认值
- 说明：
    - 节点存在则取值
    - 节点不存在则写默认值
    - JSON格式错误或路径非法会报脚本错误
- 示例：
#ACT
JsonGetNodeValue S1 user.name <$STR(S2)> 未知
SENDMSG 6 名字:<$STR(S2)>

#ACT
JsonGetNodeValue S1 user.job <$STR(S2)> 战士
SENDMSG 6 职业:<$STR(S2)>

2、获取数组长度并写入变量：JsonGetNodeArrLen Json内容 节点路径 输出变量 默认值
- 说明：
    - 节点存在且为数组，返回数组长度
    - 节点不存在，写默认值
    - 节点存在但不是数组，会报脚本错误

- 示例：
#ACT
JsonGetNodeArrLen S1 user.items <$STR(S3)> 0
SENDMSG 6 数组长度:<$STR(S3)>

#ACT
JsonGetNodeArrLen S1 user.list <$STR(S4)> 0
SENDMSG 6 list长度:<$STR(S4)>

--------------------------------------------------------------------------------------------
路径示例

- user.name
- user.level
- user.items
- user.items[0]
- user.info.vip
- user.remark

--------------------------------------------------------------------------------------------
完整组合示例

#IF
#ACT
Mov S1 {"user":{"name":"tom","level":55,"items":[1001,1002,1003],"info":{"vip":1},"remark":null}}

#IF
CheckJsonNodeExists S1 user.name
CheckJsonNodeIsArray S1 user.items
#ACT
JsonGetNodeValue S1 user.name S2 未知
JsonGetNodeArrLen S1 user.items N1 0
SENDMSG 6 名字:<$STR(S2)>
SENDMSG 6 items数量:<$STR(N1)>

;N2为下标；下标置0
Mov N2 0
While N2 < N1

;拼接字符串
TextConcat S2 user.items[ <$STR(N2)> ]

;从Json内容S1中，取User.Items[0]的值到S3中，默认值为空
JsonGetNodeValue S1 S2 S3

SENDMSG 6 <$STR(S2)>:<$STR(S3)>
Inc N2 1
EndWhile

;输出：
;名字:tom;
;items数量:3
;user.items[0]:1001
;user.items[1]:1002
;user.items[1]:1003

#ELSEACT
SENDMSG 6 条件不满足
```

## 功能概述

本文档提供了两种核心功能：HTTP网络请求（GET/POST）和JSON数据处理。通过脚本命令，可以实现与外部服务器的数据交互，并对返回的JSON格式数据进行解析和操作。

## HTTP请求功能

### 1. HttpGet 请求

向指定URL发送GET请求，并将服务器响应内容保存到变量中。

HttpGet 请求地址 NPC触发标签 返回内容保存到变量

#### 参数说明

| 参数位置 | 参数名 | 说明 | 示例 |
| --- | --- | --- | --- |
| 1 | 请求地址 | 完整的HTTP/HTTPS URL | https://webhook.site/b42ecf85... |
| 2 | NPC触发标签 | 请求完成后跳转执行的脚本标签 | @HttpGetBack |
| 3 | 返回内容保存到变量 | 存储服务器返回文本的变量名 | S100 |

#### 使用示例

[@HttpGet请求示例]
#ACT
HttpGet https://webhook.site/b42ecf85-b0eb-4aa2-88d0-b31e382e4cc7 @HttpGetBack S100
BREAK

[@HttpGetBack]
#SAY
Get返回:\
<$STR(S100)>

### 2. HttpPost 请求

向指定URL发送POST请求，支持多种内容类型。

HttpPost 请求地址 请求体内容 请求体类型 NPC触发标签 返回内容保存到变量

#### 参数说明

| 参数位置 | 参数名 | 说明 | 示例 |
| --- | --- | --- | --- |
| 1 | 请求地址 | 完整的HTTP/HTTPS URL | https://postman-echo.com/post |
| 2 | 请求体内容 | 要发送的数据内容 | p1=请求内容&p2=22344 或 {"username":"lfm2","msg":"你好"} |
| 3 | 请求体类型 | 数据发送格式，支持：form, json, text | form |
| 4 | NPC触发标签 | 请求完成后跳转执行的脚本标签 | @PostFormBack |
| 5 | 返回内容保存到变量 | 存储服务器返回文本的变量名 | S100 |

#### 请求体类型详解

- **form**: 按表单格式发送，key=value 对会自动进行URL编码
- **json**: 按 application/json; charset=utf-8 发送，正文自动转换为UTF-8编码
- **text**: 按 text/plain; charset=utf-8 发送，正文自动转换为UTF-8编码

#### Post请求示例

##### 提交表单数据 (form)

[@HttpPost提交表单]
#ACT
HttpPost https://postman-echo.com/post p1=请求内容&p2=22344 form @PostFormBack S100
BREAK

[@PostFormBack]
#SAY
Post表单返回:\
<$STR(S100)>

##### 提交JSON数据 (json)

[@HttpPost提交JSON]
#ACT
HttpPost https://postman-echo.com/post {"username":"lfm2","msg":"你好"} json @PostJsonBack S100
BREAK

[@PostJsonBack]
#ACT
JsonGetNodeValue S100 data.username S1
JsonGetNodeValue S100 data.msg S2
#SAY
UserName:<$STR(S1)>\
Msg:<$STR(S2)>\
Post Json返回:\
<$STR(S100)>

##### 提交文本数据 (text)

[@HttpPost提交Text]
#ACT
HttpPost https://postman-echo.com/post 这是一段普通文本 text @PostTextBack S100
BREAK

[@PostTextBack]
#SAY
Post Text返回:\
<$STR(S100)>

#### 执行结果说明

- 所有HTTP请求都在**异步线程**中执行，不会阻塞主脚本
- 无论请求成功或失败，返回的文本内容都会被写入指定的**返回内容保存到变量**
- 请求完成后，脚本会自动跳转到指定的**NPC触发标签**继续执行

## JSON处理功能

以下所有示例中，假设变量 S1 中的JSON内容为：
{"user":{"name":"tom","level":55,"items":[1001,1002,1003],"info":{"vip":1},"remark":null}}

### 条件命令 (检查命令)

#### 1. CheckJsonNodeExists - 检查节点是否存在

CheckJsonNodeExists Json内容 节点路径

**说明**: 检查JSON中指定路径的节点是否存在。即使节点值为 null，也被视为存在。

##### 示例

#IF
CheckJsonNodeExists S1 user.name
#ACT
SENDMSG 6 user.name 存在

#### 2. CheckJsonNodeIsArray - 检查节点是否为数组

CheckJsonNodeIsArray Json内容 节点路径

**说明**: 检查指定节点是否存在且其值是否为数组类型。

##### 示例

#IF
CheckJsonNodeIsArray S1 user.items
#ACT
SENDMSG 6 user.items 是数组

#### 3. CheckJsonNodeIsObject - 检查节点是否为对象

CheckJsonNodeIsObject Json内容 节点路径

**说明**: 检查指定节点是否存在且其值是否为对象（字典）类型。

##### 示例

#IF
CheckJsonNodeIsObject S1 user.info
#ACT
SENDMSG 6 user.info 是对象

#### 4. CheckJsonNodeIsNull - 检查节点值是否为null

CheckJsonNodeIsNull Json内容 节点路径

**说明**: 检查指定节点是否存在且其值是否为 null。

##### 示例

#IF
CheckJsonNodeIsNull S1 user.remark
#ACT
SENDMSG 6 user.remark 是 null

### 动作命令 (操作命令)

#### 1. JsonGetNodeValue - 获取节点值

JsonGetNodeValue Json内容 节点路径 输出变量 默认值

**说明**:

- 节点存在则读取其值并写入输出变量
- 节点不存在则将默认值写入输出变量
- JSON格式错误或路径非法会报脚本错误

##### 示例

; 节点存在的情况
#ACT
JsonGetNodeValue S1 user.name S2 未知
SENDMSG 6 名字:<$STR(S2)>
; 输出: 名字:tom
; 节点不存在的情况
#ACT
JsonGetNodeValue S1 user.job S2 战士
SENDMSG 6 职业:<$STR(S2)>
; 输出: 职业:战士

#### 2. JsonGetNodeArrLen - 获取数组长度

JsonGetNodeArrLen Json内容 节点路径 输出变量 默认值

**说明**:

- 节点存在且为数组，返回数组长度到输出变量
- 节点不存在，将默认值写入输出变量
- 节点存在但不是数组，会报脚本错误

##### 示例

; 获取数组长度
#ACT
JsonGetNodeArrLen S1 user.items S3 0
SENDMSG 6 数组长度:<$STR(S3)>
; 输出: 数组长度:3
; 节点不存在（非数组）
#ACT
JsonGetNodeArrLen S1 user.list S4 0
SENDMSG 6 list长度:<$STR(S4)>
; 输出: list长度:0



### JSON路径示例

JSON路径使用点号(.)表示层级关系，数组使用方括号([])加索引：

- user.name - 获取user对象的name属性
- user.level - 获取user对象的level属性
- user.items - 获取user对象的items数组
- user.items[0] - 获取user对象的items数组的第一个元素
- user.info.vip - 获取user对象中info对象的vip属性
- user.remark - 获取user对象的remark属性

### 完整组合示例

#IF
#ACT
; 定义JSON数据
Mov S1 {"user":{"name":"tom","level":55,"items":[1001,1002,1003],"info":{"vip":1},"remark":null}}
#IF
; 条件检查
CheckJsonNodeExists S1 user.name
CheckJsonNodeIsArray S1 user.items
#ACT
; 获取节点值
JsonGetNodeValue S1 user.name S2 未知
; 获取数组长度
JsonGetNodeArrLen S1 user.items N1 0
SENDMSG 6 名字:<$STR(S2)>
SENDMSG 6 items数量:<$STR(N1)>
; 循环遍历数组
Mov N2 0
While N2 < N1
; 拼接路径字符串，如 "user.items[0]"
TextConcat S2 user.items[ <$STR(N2)> ]
; 获取数组元素值
JsonGetNodeValue S1 S2 S3
SENDMSG 6 <$STR(S2)>:<$STR(S3)>
Inc N2 1
EndWhile
; 输出结果：
; 名字:tom
; items数量:3
; user.items[0]:1001
; user.items[1]:1002
; user.items[2]:1003
#ELSEACT
SENDMSG 6 条件不满足

## 功能逻辑总结

### HTTP请求执行流程

1. 脚本执行 HttpGet 或 HttpPost 命令
2. 系统在异步线程中发起HTTP网络请求
3. 等待服务器响应（成功或失败）
4. 将响应内容保存到指定的变量中
5. 自动跳转到指定的NPC触发标签继续执行脚本
6. 在触发标签中处理返回的数据（如显示或解析JSON）

### JSON数据处理流程

1. 通过HTTP请求或其他方式获取JSON数据并存入变量
2. 使用条件命令（CheckJsonNodeExists等）验证数据结构
3. 使用动作命令（JsonGetNodeValue等）提取具体数据
4. 对提取的数据进行业务逻辑处理
5. 处理过程中注意错误处理，特别是路径不存在的情况

#### 重要注意事项

- HTTP请求是异步执行的，请求发出后脚本会立即继续执行，响应处理在指定的NPC触发标签中进行
- JSON路径区分大小写，必须与数据中的键名完全一致
- 使用 JsonGetNodeValue 和 JsonGetNodeArrLen 时，如果节点路径不存在，会使用默认值，不会报错
- 但如果JSON格式错误或路径非法（如对非数组使用数组索引），会导致脚本错误
- 在处理未知的JSON数据时，建议先使用条件命令检查节点存在性和类型

## 应用场景

- **与Web API交互**: 调用外部服务的REST API获取数据或提交数据
- **数据同步**: 与中心服务器同步游戏数据、配置信息
- **第三方登录验证**: 通过OAuth等协议与第三方平台对接
- **动态配置加载**: 从远程服务器加载JSON格式的游戏配置
- **数据统计上报**: 向统计服务器上报游戏事件和数据
- **复杂数据解析**: 处理嵌套的JSON数据结构，提取所需信息
- **条件分支逻辑**: 根据JSON中的特定字段值决定脚本执行路径
