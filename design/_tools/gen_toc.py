import re
from pathlib import Path

ROOT = Path(r"C:\Users\admin\.workbuddy\skills\lf-mir200-knowledge\knowledge_base")
OUT = Path(r"D:\wangsiProject\LF知识库搭建\design\_toc_by_category.md")

lines = (ROOT / "index.md").read_text(encoding="utf-8").split("\n")
cur = None
buckets = {}
for L in lines:
    m = re.match(r"^(  )- (?!\[)(.+)$", L)
    if m:
        cur = m.group(2).strip()
        buckets.setdefault(cur, [])
        continue
    m2 = re.match(r"^\s+- \[(.+?)\]\(chapters/(.+?)\)", L)
    if m2 and cur:
        buckets[cur].append((m2.group(1), m2.group(2)))

parts = ["# 说明书章节按分类索引\n", "> 由 scripts 自动生成，供规划阶段并行阅读使用。\n"]
for k, v in buckets.items():
    parts.append("\n\n## %s （共 %d 章）\n" % (k, len(v)))
    for title, fn in v:
        parts.append("- %s  ->  `chapters/%s`" % (title, fn))
OUT.write_text("\n".join(parts), encoding="utf-8")
print("WROTE", OUT, sum(len(v) for v in buckets.values()), "chapters")
