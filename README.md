# LF Mir200 Codex Skill

这是一个面向 **LF/LFM2/翎风引擎 Mir200 服务端脚本** 的 Codex 知识库技能项目。

项目把已经转换好的说明书 Markdown、实际 `Mir200` 脚本样本、索引工具和训练总结组织成一个标准 Codex Skill，方便未来的 Codex 在回答、分析或修改 Mir200 脚本时先查资料、再看真实脚本、最后给出可复用判断。

## 项目内容

核心 skill 位于：

```text
codex-skills/lf-mir200-knowledge
```

主要文件：

```text
codex-skills/lf-mir200-knowledge/
  SKILL.md                         # Codex skill 主说明
  scripts/lf_kb.py                 # 本地索引、搜索、检查工具
  references/local-layout.md       # 本地知识库目录约定
  references/mir200-thinking.md    # 从真实脚本提炼出的思维模型
  references/mir200-training.md    # 用样本脚本继续训练的课程地图
  agents/openai.yaml               # 可复用 agent 配置参考
```

仓库还包含：

```text
tests/test_lf_kb.py                # 静态工具测试
```

## 能力范围

这个 skill 用于：

- 查询 LF/LFM2/Mir200 说明书中的命令、参数和规则。
- 检索真实 `样本Mir200` 脚本中的可用写法。
- 分析 NPC、QuestDiary、MapInfo、MonGen、MerChant、Robot_def、Market_def 等脚本结构。
- 从样本脚本中总结入口、条件、动作、状态写回、失败路径等通用经验。
- 生成并维护 `mir200-thinking.md` 和 `mir200-training.md`，让 skill 可以随着样本持续升级。

这个 skill 不用于：

- 编译、启动或运行 Mir200 服务端。
- 修改或上传服务端二进制、数据库、授权文件、运行日志。
- 凭空编造命令语法。回答前应先检索说明书或样本。

## 本地知识根要求

使用时需要在某个本地目录中准备两类内容：

```text
knowledge_base/index.md            # 已转换好的说明书总目录
样本Mir200/                        # 实际 Mir200 服务端脚本样本
```

本仓库默认不提交这些大体积或敏感内容：

- 原始 CHM 文件
- CHM 解包目录
- 完整转换后的说明书正文
- `样本Mir200/` 服务端样本
- `.exe`、`.db`、`.dat`、`.lic`、日志、缓存等运行文件

这样做是为了让 GitHub 仓库保持轻量，也避免误传服务器私有文件。

## 安装到 Codex

将 skill 目录复制到 Codex 的本地 skills 目录：

```powershell
Copy-Item -Recurse -Force "codex-skills\lf-mir200-knowledge" "$env:USERPROFILE\.codex\skills\lf-mir200-knowledge"
```

安装后，在新任务中当你询问 LF/LFM2/Mir200 脚本、命令、NPC、地图、怪物刷新、机器人脚本、商人脚本等问题时，Codex 会根据 skill 描述加载这套知识库工作流。

## 常用命令

在知识根目录运行，或用 `--root` 指定知识根：

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . validate
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . update
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . search "CHECKITEM GIVE 装备回收" --source all --limit 8
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . inspect "codex-skills/lf-mir200-knowledge/references/mir200-thinking.md"
```

命令用途：

| 命令 | 用途 |
| --- | --- |
| `validate` | 静态检查知识根、说明书索引、样本索引和训练文件是否可用 |
| `update` | 根据当前说明书和样本脚本重建索引、思维总结、训练课程 |
| `search` | 在说明书、样本脚本或全部来源中检索关键词 |
| `inspect` | 安全读取指定文件，便于 Codex 引用和分析 |

## 自我升级方式

当说明书或 `样本Mir200` 内容变化后，执行：

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . update
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . validate
```

更新后重点查看：

- `references/mir200-thinking.md`：当前从真实脚本中提炼出的“脚本思维”。
- `references/mir200-training.md`：适合未来 Codex 逐课学习的样本阅读路线。

推荐训练方法：

1. 先看 `mir200-training.md` 的课程顺序。
2. 每次只学习一个主题，例如 NPC 对话、装备回收、自动机器人、地图事件。
3. 对照说明书确认命令语法。
4. 再从样本中总结入口、条件、动作、状态写回和失败分支。
5. 可复用经验沉淀到 `mir200-thinking.md`，稳定规则再沉淀到 `SKILL.md`。

## 静态分析约束

本项目遵循一个硬约束：

```text
不要编译、启动或运行 Mir200 服务端；只做静态分析与静态验证。
```

也就是说，Codex 可以读取说明书、检索脚本、分析文本、更新索引、运行本项目的静态检查工具，但不应该尝试启动服务端、连接运行环境或执行 Mir200 相关二进制。

## 开发验证

本项目当前使用 Python 标准库实现索引工具和测试。提交前建议运行：

```powershell
python -m unittest tests.test_lf_kb -v
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . validate
```

这些验证只检查本仓库的工具逻辑和知识库结构，不会编译或运行 Mir200 服务端。

## GitHub 发布说明

这个仓库适合公开保存 skill 本体、工具脚本、训练方法和项目说明。

真实服务器样本、完整说明书、CHM 解包产物和运行文件应继续保留在本地，并通过 `.gitignore` 排除。
