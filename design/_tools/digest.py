"""把说明书章节压成高密度摘要：标题 + 功能/说明/格式/命令签名行。

用法: python digest.py <分类名> <每章最大字符数> <输出文件>
分类名须与 design/_toc_by_category.md 中的 ## 标题一致。
"""
import re
import sys
from pathlib import Path

KB = Path(r"C:\Users\admin\.workbuddy\skills\lf-mir200-knowledge\knowledge_base")
TOC = Path(r"D:\wangsiProject\LF知识库搭建\design\_toc_by_category.md")

KEEP_PREFIX = (
    "功能", "说明", "参数", "注意", "返回值", "格式", "命令格式", "使用说明",
    "相关", "示例", "实例", "语法", "作用", "用途", "补充", "限制",
)


def parse_toc():
    cur = None
    buckets = {}
    for line in TOC.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^## (.+?) （共 (\d+) 章）", line)
        if m:
            cur = m.group(1)
            buckets.setdefault(cur, [])
            continue
        m2 = re.match(r"^- (.*?)  ->  `(chapters/.+?)`", line)
        if m2 and cur:
            buckets[cur].append((m2.group(1), m2.group(2)))
    return buckets


def digest(text: str, maxc: int) -> str:
    lines = text.split("\n")
    title = ""
    body = []
    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        if not title and s.startswith("#"):
            title = s.lstrip("# ").strip()
            continue
        if not title:
            continue
        if s.startswith("#") or s.startswith("---") or s.startswith("|"):
            # 表格保留少量，配置表信息量大
            if s.startswith("|") and len(s) < 160:
                body.append(s)
            continue
        keep = False
        core = s.lstrip("*").strip()
        if any(core.startswith(p) for p in KEEP_PREFIX):
            keep = True
        elif re.search(r"格式[：:]", s):
            keep = True
        elif re.match(r"^[A-Z][A-Za-z0-9_.]{2,}\s+\S", s) and len(s) < 220:
            keep = True  # 命令签名
        if keep:
            body.append(s)
    out = "\n".join(body)
    if len(out) > maxc:
        out = out[:maxc] + " …[截断]"
    return "### " + title + "\n" + out if title else out


def main():
    cat, maxc, outfile = sys.argv[1], int(sys.argv[2]), Path(sys.argv[3])
    buckets = parse_toc()
    if cat not in buckets:
        print("可用分类:", " | ".join(buckets))
        sys.exit(1)
    parts = ["# 摘要：%s（%d 章）\n" % (cat, len(buckets[cat]))]
    for title, fn in buckets[cat]:
        p = KB / fn
        if not p.exists():
            parts.append("### %s\n[缺失文件 %s]" % (title, fn))
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            parts.append("### %s\n[读取失败 %s]" % (title, e))
            continue
        d = digest(txt, maxc)
        if not d.startswith("### "):
            d = "### " + title + "\n" + d
        parts.append(d)
    outfile.write_text("\n\n".join(parts), encoding="utf-8")
    print("WROTE", outfile, outfile.stat().st_size // 1024, "KB")


if __name__ == "__main__":
    main()
