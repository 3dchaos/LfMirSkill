---
name: codegraph
description: Use CodeGraph to inspect indexed repositories with symbol lookup, call paths, and project-aware exploration. Use when a repo has a `.codegraph/` index, when the user asks to use CodeGraph, or when they need to locate symbols, follow callers/callees, trace paths, or understand code relationships.
---

# CodeGraph

Use CodeGraph as the first structural query tool when the current repository contains a `.codegraph/` index. It is for repository understanding and navigation; use normal file inspection and project tests for implementation details and verification.

## Quick Workflow

1. Check for `.codegraph/` at the repository root.
2. Prefer the available MCP tools: `codegraph_explore`, `codegraph_node`, `codegraph_query`, and `codegraph_files`.
3. If MCP tools are unavailable, use the CLI equivalents: `codegraph explore`, `codegraph node`, `codegraph query`, and `codegraph files`.
4. If the project is not indexed, run `codegraph init` only when indexing is appropriate, then confirm with `codegraph status`.
5. Use the graph result to narrow file reads before editing or testing code.

## Good Queries

- Where is `X` defined?
- Who calls `Y`, and what does `Y` call?
- Trace the path from `A` to `B`.
- Which files are related to this feature?
- Summarize the code around symbol `Z`.

## Boundaries

- Keep queries repository-specific and cite the graph nodes or files used.
- Treat graph output as navigation evidence, not proof of runtime behavior; verify configuration, generated code, reflection, and dynamic dispatch in the source and tests.
- Do not force CodeGraph when the repository has no index or the CLI/MCP server is unavailable; fall back to targeted `rg`, project tooling, and normal static analysis.
- Do not modify `.codegraph/` database or daemon files manually.

## Installation Prerequisite

The skill assumes the CodeGraph CLI/MCP server is installed separately. On Windows, install the upstream tool first, then restart Codex so its MCP tools can load. A repository with an existing `.codegraph/` index can be inspected without rebuilding it.
