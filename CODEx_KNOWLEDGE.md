# Codex Knowledge Base

This workspace contains a reusable Codex knowledge setup for LF/LFM2 Mir200 server scripting.

## What is included

- `codex-skills/lf-mir200-knowledge/knowledge_base/`: Markdown manual converted from the CHM help file; required skill content.
- `样本Mir200/`: Real Mir200 server sample used for script examples.
- `.codex-kb/indexes/`: Generated search indexes for Codex.
- `codex-skills/lf-mir200-knowledge/`: Shareable Codex skill source.

## Install for Codex

Install the skill together with its required manual knowledge base:

```powershell
python scripts\install_codex_skill.py `
  --source . `
  --dest "$env:USERPROFILE\.codex\skills\lf-mir200-knowledge"
```

The public package does not include `样本Mir200`; provide it separately through `--root` or `LF_MIR200_KB_ROOT` when sample-backed analysis is needed.

If the local sample root is elsewhere, set:

```powershell
$env:LF_MIR200_KB_ROOT = "D:\path\to\LF知识库搭建"
```

## Refresh indexes

Run this after updating the manual or replacing the sample Mir200 folder:

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root codex-skills\lf-mir200-knowledge update
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root codex-skills\lf-mir200-knowledge validate
```

## Search examples

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root codex-skills\lf-mir200-knowledge search "OPENMERCHANTBIGDLG ITEMBOX 装备转移" --source all --limit 5
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root codex-skills\lf-mir200-knowledge search "MAPMOVE 老兵" --source sample --limit 5
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root codex-skills\lf-mir200-knowledge inspect "knowledge_base/chapters/661-丢弃背包物品前触发.md"
```

## Operating rule

Use static validation only. Do not compile or launch Mir200 server binaries unless the project owner explicitly changes that rule.
