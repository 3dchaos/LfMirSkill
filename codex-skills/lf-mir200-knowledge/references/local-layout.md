# Local Layout

The expected knowledge root contains:

- `knowledge_base/index.md`: Manual table of contents converted from CHM.
- `knowledge_base/chapters/*.md`: One Markdown file per manual page.
- `knowledge_base/assets/`: Images and attachments from the manual.
- `knowledge_base/manifest.json`: Conversion counts and duplicate CHM targets.
- `样本Mir200/`: Real Mir200 server sample.
- `.codex-kb/indexes/docs.json`: Derived manual search index.
- `.codex-kb/indexes/sample.json`: Derived sample-script search index.
- `.codex-kb/indexes/mapinfo-links.json`: Derived `MapInfo.txt` map-link index.
- `.codex-kb/indexes/thoughts.json`: Derived script-thinking summary.
- `references/mir200-thinking.md`: Human-readable version of the current script-thinking summary.

Important sample folders:

- `样本Mir200/Envir/Market_def`: merchant/NPC dialog scripts.
- `样本Mir200/Envir/Npc_def`: NPC definition scripts.
- `样本Mir200/Envir/QuestDiary`: feature and quest script modules.
- `样本Mir200/Envir/MapQuest_def`: map-trigger scripts.
- `样本Mir200/Envir/Robot_def`: robot/timer automation scripts.
- `样本Mir200/Envir/MapInfo.txt`: map flags and directional map links, for example `0 308,264 -> 0102 3,7`.
- `样本Mir200/Envir/MerChant.txt`: NPC placement table.
- `样本Mir200/Envir/MonGen.txt`: monster spawn table.

Do not treat binary runtime files as editable knowledge sources.
