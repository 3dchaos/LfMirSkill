# LF Mir200 Knowledge Workspace

This workspace builds a standard Codex skill from LF/LFM2 Mir200 help docs and real sample scripts.

## Main skill

The published skill lives at:

- `codex-skills/lf-mir200-knowledge`

## What it does

- indexes the converted knowledge base
- indexes the real `样本Mir200` scripts
- generates a reusable thinking summary
- generates a progressive training course from examples
- validates the knowledge root statically

## Local workflow

```powershell
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . update
python codex-skills\lf-mir200-knowledge\scripts\lf_kb.py --root . validate
```

## Install into Codex

Copy the skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force "codex-skills\lf-mir200-knowledge" "$env:USERPROFILE\.codex\skills\lf-mir200-knowledge"
```

## Constraint

Do not compile or run the Mir200 server. This project is for static analysis only.
