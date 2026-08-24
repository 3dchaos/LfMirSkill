# Codex Knowledge Base

This workspace contains a reusable Codex knowledge setup for LF/LFM2 Mir200 server scripting.

## What is included

- `knowledge_base/`: Markdown manual converted from the CHM help file.
- `样本Mir200/`: Real Mir200 server sample used for script examples.
- `.codex-kb/indexes/`: Generated search indexes for Codex.
- `codex-skills/lf-mir200-knowledge/`: Shareable Codex skill source.
- `codex-skills/codegraph/`: CodeGraph repository-navigation skill source.

## Install for Codex

Copy `codex-skills/lf-mir200-knowledge` into a Codex skills directory:

```powershell
Copy-Item -Recurse -Force "codex-skills\lf-mir200-knowledge" "$env:USERPROFILE\.codex\skills\lf-mir200-knowledge"
```

Install the optional CodeGraph skill:

```powershell
Copy-Item -Recurse -Force "codex-skills\codegraph" "$env:USERPROFILE\.codex\skills\codegraph"
```

The CodeGraph CLI/MCP server is a separate prerequisite. The skill uses an existing `.codegraph/` index for symbol and call-path queries.

If the workspace is moved, either start Codex inside this workspace or set:

```powershell
$env:LF_MIR200_KB_ROOT = "D:\path\to\LF知识库搭建"
```

## Refresh indexes

Run this after updating the manual or replacing the sample Mir200 folder:

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . update
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . validate
```

## Search examples

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . search "OPENMERCHANTBIGDLG ITEMBOX 装备转移" --source all --limit 5
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . search "MAPMOVE 老兵" --source sample --limit 5
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . inspect "knowledge_base/chapters/661-丢弃背包物品前触发.md"
```

## Operating rule

Use static validation only. Do not compile or launch Mir200 server binaries unless the project owner explicitly changes that rule.
