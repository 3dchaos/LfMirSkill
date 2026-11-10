import re
from pathlib import Path

KB = Path(r"C:\Users\admin\.workbuddy\skills\lf-mir200-knowledge\knowledge_base")
TOC = Path(r"D:\wangsiProject\LF知识库搭建\design\_toc_by_category.md")

cur = None
buckets = {}
for line in TOC.read_text(encoding="utf-8").split("\n"):
    m = re.match(r"^## (.+?) （共 (\d+) 章）", line)
    if m:
        cur = m.group(1)
        buckets[cur] = []
        continue
    m2 = re.match(r"^- .*`(chapters/.+?)`", line)
    if m2 and cur:
        buckets[cur].append(m2.group(1))

print(f"{'分类':<22}{'章数':>5}{'总KB':>9}{'最大单章KB':>12}")
print("-" * 48)
tot_c = tot_b = 0
for k, v in buckets.items():
    sizes = [(KB / f).stat().st_size for f in v if (KB / f).exists()]
    tot_c += len(v)
    tot_b += sum(sizes)
    print(f"{k:<22}{len(v):>5}{sum(sizes)//1024:>9}{max(sizes)//1024:>12}")
print("-" * 48)
print(f"{'总计':<22}{tot_c:>5}{tot_b//1024:>9}")
