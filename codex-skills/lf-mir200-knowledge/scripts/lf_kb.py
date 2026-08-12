from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


INDEX_DIR = ".codex-kb/indexes"
DOCS_INDEX = "docs.json"
SAMPLE_INDEX = "sample.json"
THOUGHTS_INDEX = "thoughts.json"
TRAINING_INDEX = "training-course.json"
MAPINFO_LINKS_INDEX = "mapinfo-links.json"
TEXT_EXTENSIONS = {".md", ".txt", ".ini"}
SAMPLE_SKIP_EXTENSIONS = {".exe", ".db", ".dat", ".lic"}
THINKING_SKIP_CATEGORIES = {"ConLog"}
THINKING_CATEGORY_PREFIXES = (
    "Market_def",
    "Npc_def",
    "QuestDiary",
    "MapQuest_def",
    "Robot_def",
    "MerChant",
    "Npcs",
    "MapEvent",
    "MapInfo",
    "MonGen",
    "Robot.txt",
)
PATTERN_RULES = [
    ("入口与分发", ["[@main]", "@main", "@Startup", "@Help", "@Home", "@start"]),
    ("条件守门", ["#IF", "CHECK", "LARGE ", "SMALL ", "EQUAL ", "RANDOM ", "COMPARETEXT", "CHECKMAPNAME"]),
    ("动作执行", ["#ACT", "GIVE ", "TAKE ", "GAMEGOLD", "GAMEGIRD", "MAPMOVE", "MonGen", "GOTO", "BREAK"]),
    ("UI与交互", ["#SAY", "MESSAGEBOX", "OPENMERCHANTBIGDLG", "ITEMBOX", "Text:", "Img:", "Layout:", "MText:"]),
    ("状态回写", ["SET [", "MOV ", "SetOnTimer", "DelTextListLine", "AddTextListEx", "ReturnBoxItem", "UpdateItem", "SetCustomItemText"]),
    ("自动化与定时", ["AutoRun", "OnTimer", "SetOnTimer", "Robot", "Gmexecute", "#CALL"]),
    ("地图链接", ["->", "MapInfo", "MAPMOVE"]),
]
TRAINING_LESSONS = [
    {
        "id": "lesson-01-entry-dispatch",
        "title": "入口与分发",
        "goal": "先定位玩家从哪个 NPC 标签进入，再追踪 GOTO 和按钮链接如何把流程分出去。",
        "signals": ["[@main]", "@main", "GOTO"],
        "categories": ["Market_def", "Npc_def", "QuestDiary"],
        "thinking_focus": ["入口不是业务本身，入口负责把玩家动作分派到真正的处理标签。", "读脚本时先画标签流，再判断每个分支的条件和副作用。"],
    },
    {
        "id": "lesson-02-dialog-ui",
        "title": "对话与界面组织",
        "goal": "学习 #SAY、按钮链接、大对话框、ITEMBOX、Text/Img 等 UI 如何承载业务输入。",
        "signals": ["#SAY", "OPENMERCHANTBIGDLG", "ITEMBOX", "Text:", "Img:", "MESSAGEBOX"],
        "categories": ["Market_def", "QuestDiary"],
        "thinking_focus": ["UI 标签既展示说明，也把玩家选择绑定到后续标签。", "ITEMBOX 这类控件要顺着 boxitem 变量继续查真正的状态读写。"],
    },
    {
        "id": "lesson-03-guards-costs",
        "title": "条件守门与成本检查",
        "goal": "提炼 CHECK、COMPARE、RANDOM、货币/背包/地图检查如何阻止非法执行。",
        "signals": ["#IF", "CHECKITEM", "CHECKGOLD", "CHECKGAMEGOLD", "COMPARETEXT", "RANDOM", "CHECKBAGSIZE", "small ", "large ", "equal "],
        "categories": ["Market_def", "QuestDiary", "MapQuest_def"],
        "thinking_focus": ["先检查资格，再扣成本，再执行奖励或传送。", "有 #ELSEACT 或 BREAK 的地方通常是失败路径，不要只读成功路径。"],
    },
    {
        "id": "lesson-04-actions-rewards",
        "title": "动作、奖励与惩罚",
        "goal": "学习 GIVE、TAKE、GAMEGOLD、MAPMOVE、MonGen、SENDMSG 等动作如何改变玩家、地图和背包。",
        "signals": ["#ACT", "GIVE ", "TAKE ", "GAMEGOLD", "MAPMOVE", "MonGen", "SENDMSG", "MESSAGEBOX"],
        "categories": ["Market_def", "QuestDiary", "Robot_def", "MapEvent.txt"],
        "thinking_focus": ["动作块是副作用集中区，要把每个 TAKE/GIVE/MAPMOVE 当成状态变化记录。", "扣费与奖励最好成对审查，确认失败路径不会误扣或漏还。"],
    },
    {
        "id": "lesson-05-state-writeback",
        "title": "变量、物品状态与回写",
        "goal": "学习 MOV、SET、物品属性读写、文本列表、UpdateItem/ReturnBoxItem 如何保存业务结果。",
        "signals": ["MOV ", "SET ", "GetCustomItemText", "GETITEMADDVALUE", "CHANGEITEMADDVALUE", "SetNewItemValue", "UpdateItem", "ReturnBoxItem", "AddTextListEx", "DelTextListLine"],
        "categories": ["QuestDiary", "Market_def", "MapQuest_def"],
        "thinking_focus": ["变量只是中间账本，真正结果常落在物品、列表文件、称号、计时器或角色状态上。", "遇到 boxitem 和自定义属性时，必须同时检查读取、清零、写入、刷新和归还。"],
    },
    {
        "id": "lesson-06-timers-automation",
        "title": "定时器、机器人与全局流程",
        "goal": "学习 SetOnTimer、OnTimer、Robot_def、AutoRunRobot 和 QManage 如何驱动后台流程。",
        "signals": ["SetOnTimer", "OnTimer", "AutoRunRobot", "Robot", "Gmexecute", "@Startup", "@Login"],
        "categories": ["Robot_def", "MapQuest_def", "Robot.txt"],
        "thinking_focus": ["自动化脚本不靠玩家点击触发，入口常在 Startup/Login/OnTimer。", "读定时器要把启动位置、间隔、终止条件和重复副作用连起来看。"],
    },
    {
        "id": "lesson-07-world-config",
        "title": "地图、怪物与商人配置",
        "goal": "学习 MapInfo、MapEvent、MonGen、MerChant、Npcs 等配置文件如何把脚本挂到世界上，特别是 MapInfo 的地图链接行。",
        "signals": ["MapInfo", "MapEvent", "MonGen", "MerChant", "Npcs", "NoRecall", "SAFE", "Mongen", "->"],
        "categories": ["MapInfo.txt", "MapEvent.txt", "MonGen.txt", "MerChant.txt", "Npcs.txt"],
        "thinking_focus": [
            "功能脚本往往不是孤立文件，要从地图/NPC/刷怪配置找到它的挂载点。",
            "MapInfo 链接行表示玩家走到源地图源坐标时，被传送到目标地图目标坐标。",
            "排查问题时同时看脚本内容和配置入口，确认玩家是否真的能触发。",
        ],
    },
    {
        "id": "lesson-08-combined-systems",
        "title": "组合系统拆解",
        "goal": "练习把复杂系统拆成入口、UI、守门、动作、状态回写、后台触发六个面向再逐项检查。",
        "signals": ["OPENMERCHANTBIGDLG", "ITEMBOX", "SetOnTimer", "GOTO", "RANDOM", "UpdateItem", "ReturnBoxItem", "MAPMOVE"],
        "categories": ["QuestDiary", "Market_def", "MapQuest_def"],
        "thinking_focus": ["复杂脚本不要从头读到尾硬啃，先按职责切块。", "每次改动前写出输入、条件、成本、成功副作用、失败副作用和恢复路径。"],
    },
]


@dataclass
class ResolvedRoot:
    root: Path
    source: str


def read_text(path: Path) -> str:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "gb18030", "gbk"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return data.decode("gb18030", errors="replace")


def normalize_rel(path: Path) -> str:
    return path.as_posix()


def find_root(start: Path | None = None, explicit_root: str | None = None) -> ResolvedRoot:
    candidates: list[tuple[Path, str]] = []
    if explicit_root:
        candidates.append((Path(explicit_root), "--root"))
    env_root = os.environ.get("LF_MIR200_KB_ROOT")
    if env_root:
        candidates.append((Path(env_root), "LF_MIR200_KB_ROOT"))

    current = (start or Path.cwd()).resolve()
    for parent in [current, *current.parents]:
        candidates.append((parent, "ancestor"))

    for candidate, source in candidates:
        root = candidate.resolve()
        if (root / "knowledge_base" / "index.md").exists() and (root / "样本Mir200").exists():
            return ResolvedRoot(root=root, source=source)
    raise FileNotFoundError("Cannot locate LF/Mir200 knowledge root. Pass --root or set LF_MIR200_KB_ROOT.")


def first_heading(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return match.group(1).strip()
    return fallback


def compact_text(text: str, limit: int = 12000) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def build_docs_index(root: Path) -> list[dict[str, str]]:
    chapters = root / "knowledge_base" / "chapters"
    records: list[dict[str, str]] = []
    for path in sorted(chapters.rglob("*.md")):
        text = read_text(path)
        rel = normalize_rel(path.relative_to(root))
        records.append(
            {
                "kind": "doc",
                "title": first_heading(text, path.stem),
                "relative_path": rel,
                "text": compact_text(text),
            }
        )
    return records


def classify_sample(path: Path, sample_root: Path) -> str:
    parts = path.relative_to(sample_root).parts
    if "Envir" in parts:
        index = parts.index("Envir")
        if len(parts) > index + 1:
            return parts[index + 1]
        return "Envir"
    if parts:
        return parts[0]
    return "sample"


def build_sample_index(root: Path) -> list[dict[str, str]]:
    sample_root = root / "样本Mir200"
    records: list[dict[str, str]] = []
    for path in sorted(sample_root.rglob("*")):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix in SAMPLE_SKIP_EXTENSIONS or suffix not in TEXT_EXTENSIONS:
            continue
        text = read_text(path)
        rel = normalize_rel(path.relative_to(root))
        records.append(
            {
                "kind": "sample",
                "category": classify_sample(path, sample_root),
                "title": path.stem,
                "relative_path": rel,
                "text": compact_text(text),
            }
        )
    return records


def parse_mapinfo_link_line(line: str, line_number: int) -> dict[str, object] | None:
    raw = line.rstrip("\r\n")
    stripped = raw.strip()
    if not stripped or stripped.startswith(";") or stripped.startswith("[") or "->" not in stripped:
        return None

    left, right = stripped.split("->", 1)
    left_parts = left.replace(",", " ").split()
    right_parts = right.replace(",", " ").split()
    if len(left_parts) != 3 or len(right_parts) != 3:
        return None

    try:
        source_x = int(left_parts[1])
        source_y = int(left_parts[2])
        target_x = int(right_parts[1])
        target_y = int(right_parts[2])
    except ValueError:
        return None

    return {
        "kind": "map_link",
        "line_number": line_number,
        "source_map": left_parts[0],
        "source_x": source_x,
        "source_y": source_y,
        "target_map": right_parts[0],
        "target_x": target_x,
        "target_y": target_y,
        "raw": raw,
    }


def build_mapinfo_link_index(root: Path) -> list[dict[str, object]]:
    mapinfo = root / "样本Mir200" / "Envir" / "MapInfo.txt"
    if not mapinfo.exists():
        return []

    records: list[dict[str, object]] = []
    for line_number, line in enumerate(read_text(mapinfo).splitlines(), start=1):
        parsed = parse_mapinfo_link_line(line, line_number)
        if not parsed:
            continue
        source = f"{parsed['source_map']}({parsed['source_x']},{parsed['source_y']})"
        target = f"{parsed['target_map']}({parsed['target_x']},{parsed['target_y']})"
        parsed["title"] = f"{source} -> {target}"
        parsed["relative_path"] = f"{normalize_rel(mapinfo.relative_to(root))}:{line_number}"
        parsed["text"] = (
            f"MapInfo 地图链接规则: 当玩家走到源地图 {parsed['source_map']} 的 "
            f"X{parsed['source_x']} Y{parsed['source_y']}，进入目标地图 {parsed['target_map']} 的 "
            f"X{parsed['target_x']} Y{parsed['target_y']}。原始行: {parsed['raw']}"
        )
        records.append(parsed)
    return records


def detect_patterns(text: str) -> list[dict[str, object]]:
    upper = text.upper()
    results = []
    for name, signals in PATTERN_RULES:
        matched = [signal for signal in signals if signal.upper() in upper]
        if matched:
            results.append({"name": name, "signals": matched[:4]})
    return results


def thinking_records(records: list[dict[str, str]]) -> list[dict[str, str]]:
    return [
        record
        for record in records
        if record.get("kind") == "sample"
        and record.get("category", "") not in THINKING_SKIP_CATEGORIES
        and record.get("category", "").startswith(THINKING_CATEGORY_PREFIXES)
    ]


def record_signal_score(record: dict[str, str], signals: list[str], preferred_categories: list[str] | None = None) -> int:
    text = record.get("text", "")
    upper_text = text.upper()
    rel = record.get("relative_path", "")
    rel_upper = rel.upper()
    category = record.get("category", "")
    score = 0
    for signal in signals:
        upper_signal = signal.upper()
        if upper_signal in upper_text:
            score += 10 + min(upper_text.count(upper_signal), 12)
            if upper_signal in {"OPENMERCHANTBIGDLG", "ITEMBOX", "TEXT:", "IMG:", "LAYOUT:", "MTEXT:"}:
                score += 8
        if upper_signal in rel_upper:
            score += 4
    if preferred_categories:
        for index, preferred in enumerate(preferred_categories):
            if category == preferred or preferred.upper() in rel_upper:
                score += 10 + max(0, len(preferred_categories) - index)
    return score


def best_examples(
    records: list[dict[str, str]],
    signals: list[str],
    preferred_categories: list[str] | None = None,
    limit: int = 3,
) -> list[dict[str, object]]:
    ranked = []
    for record in thinking_records(records):
        score = record_signal_score(record, signals, preferred_categories)
        if not score:
            continue
        matched = [signal for signal in signals if signal.upper() in record.get("text", "").upper()]
        ranked.append(
            {
                "score": score,
                "title": record.get("title", ""),
                "category": record.get("category", ""),
                "relative_path": record.get("relative_path", ""),
                "signals": matched[:6],
            }
        )
    ranked.sort(key=lambda item: (-int(item["score"]), str(item["relative_path"])))
    return ranked[:limit]


def build_thought_summary(records: list[dict[str, str]]) -> dict[str, object]:
    sample_records = thinking_records(records)
    pattern_counter: Counter[str] = Counter()
    signal_counter: Counter[str] = Counter()
    category_counter: Counter[str] = Counter()
    examples_by_pattern: dict[str, list[dict[str, object]]] = {}

    for record in sample_records:
        patterns = detect_patterns(record.get("text", ""))
        if not patterns:
            continue
        category = record.get("category", "sample")
        category_counter[category] += 1
        for pattern in patterns:
            pattern_counter[pattern["name"]] += 1
            for signal in pattern["signals"]:
                signal_counter[signal] += 1

    pattern_rows = []
    for name, signals in PATTERN_RULES:
        if pattern_counter.get(name, 0):
            pattern_rows.append(
                {
                    "name": name,
                    "count": pattern_counter[name],
                    "signals": [signal for signal in signals if signal_counter.get(signal)],
                    "examples": examples_by_pattern.get(name) or best_examples(sample_records, signals, limit=3),
                }
            )

    principles = [
        "先找入口，再看条件，再看动作，最后确认状态回写。",
        "NPC 脚本常把问答、跳转、奖励和退出放在同一条线里处理。",
        "任务脚本常把 UI 交互、背包检测、物品流转和反馈消息绑定在一起。",
        "地图事件与自动化脚本常靠定时器、全局变量和场景条件驱动。",
        "MapInfo 中的 `源地图 源X,源Y -> 目标地图 目标X,目标Y` 是地图链接；玩家踩到源坐标后进入目标坐标。",
    ]
    return {
        "principles": principles,
        "patterns": pattern_rows,
        "dominant_categories": category_counter.most_common(8),
    }


def build_training_course(records: list[dict[str, str]]) -> dict[str, object]:
    lessons = []
    covered_paths: set[str] = set()
    for lesson in TRAINING_LESSONS:
        examples = best_examples(records, lesson["signals"], lesson["categories"], limit=4)
        if examples:
            covered_paths.update(str(example["relative_path"]) for example in examples)
        lessons.append(
            {
                "id": lesson["id"],
                "title": lesson["title"],
                "goal": lesson["goal"],
                "signals": lesson["signals"],
                "thinking_focus": lesson["thinking_focus"],
                "examples": examples,
                "practice": [
                    "先用 search 查同类关键词，再 inspect 最相关的样本。",
                    "写出入口、条件、动作、状态回写、失败路径五项笔记。",
                    "把可复用经验补进 mir200-thinking.md 或重新运行 update 生成。",
                ],
            }
        )
    return {
        "course_name": "Mir200 样本脚本渐进训练课",
        "source": "样本Mir200",
        "method": "按真实脚本信号抽样，从简单入口到组合系统逐层学习。",
        "lessons": lessons,
        "coverage": {
            "lessons": len(lessons),
            "example_files": len(covered_paths),
            "sample_records": len(thinking_records(records)),
        },
    }


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def render_thoughts_markdown(summary: dict[str, object], root: Path) -> str:
    lines = [
        "# Mir200 Script Thinking",
        "",
        "Generated from the live `样本Mir200` scripts.",
        "",
        "## Principles",
        "",
    ]
    for item in summary.get("principles", []):
        lines.append(f"- {item}")
    lines.extend(["", "## Patterns", ""])
    for pattern in summary.get("patterns", []):
        signals = ", ".join(pattern.get("signals", []))
        lines.append(f"- {pattern.get('name')} ({pattern.get('count', 0)}): {signals}")
        for example in pattern.get("examples", [])[:3]:
            example_signals = ", ".join(example.get("signals", []))
            lines.append(f"  - Example: `{example.get('relative_path')}` ({example_signals})")
    lines.extend(["", "## Dominant Categories", ""])
    for category, count in summary.get("dominant_categories", []):
        lines.append(f"- {category}: {count}")
    lines.extend(
        [
            "",
            "## Reading Discipline",
            "",
            "- Treat the manual as syntax authority and `样本Mir200` as practical usage authority.",
            "- For any script, write down: entry, guards, actions, state writeback, failure path.",
            "- If a pattern appears in multiple examples, prefer the repeated local style over a one-off shortcut.",
        ]
    )
    lines.extend(
        [
            "",
            "## Update Loop",
            "",
            "1. Refresh `docs.json` and `sample.json`.",
            "2. Rebuild this summary from the current sample scripts.",
            "3. Rebuild `mir200-training.md` so the learning course follows current examples.",
            "4. Read this file before answering new Mir200 questions.",
            "",
            f"Source root: `{root}`",
        ]
    )
    return "\n".join(lines).strip() + "\n"


def render_training_markdown(course: dict[str, object], root: Path) -> str:
    coverage = course.get("coverage", {})
    lines = [
        "# Mir200 Training Course",
        "",
        "Generated from the live `样本Mir200` scripts.",
        "",
        f"- Method: {course.get('method')}",
        f"- Lessons: {coverage.get('lessons', 0)}",
        f"- Example files: {coverage.get('example_files', 0)}",
        f"- Sample records considered: {coverage.get('sample_records', 0)}",
        "",
        "## How To Train",
        "",
        "1. Start with lesson 1 and inspect each listed sample file.",
        "2. For each file, trace entry, guards, actions, state writeback, and failure path.",
        "3. Compare the sample against the manual before copying command syntax.",
        "4. Add new reusable observations to `mir200-thinking.md`, then run `update` to refresh generated summaries.",
        "",
        "## Lessons",
        "",
    ]
    for lesson in course.get("lessons", []):
        lines.extend(
            [
                f"### {lesson.get('title')}",
                "",
                f"- ID: `{lesson.get('id')}`",
                f"- Goal: {lesson.get('goal')}",
                f"- Signals: {', '.join(lesson.get('signals', []))}",
                "- Thinking focus:",
            ]
        )
        for focus in lesson.get("thinking_focus", []):
            lines.append(f"  - {focus}")
        lines.append("- Examples:")
        examples = lesson.get("examples", [])
        if examples:
            for example in examples:
                signals = ", ".join(example.get("signals", []))
                lines.append(f"  - `{example.get('relative_path')}` ({signals})")
        else:
            lines.append("  - No strong matching sample yet; search manually before answering this topic.")
        lines.append("- Practice:")
        for item in lesson.get("practice", []):
            lines.append(f"  - {item}")
        lines.append("")
    lines.extend(["", f"Source root: `{root}`"])
    return "\n".join(lines).strip() + "\n"


def write_indexes(root: Path, skill_dir: Path | None = None) -> dict[str, int]:
    out_dir = root / INDEX_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    docs = build_docs_index(root)
    sample = build_sample_index(root)
    mapinfo_links = build_mapinfo_link_index(root)
    thought = build_thought_summary(sample)
    course = build_training_course(sample)
    (out_dir / DOCS_INDEX).write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / SAMPLE_INDEX).write_text(json.dumps(sample, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / MAPINFO_LINKS_INDEX).write_text(json.dumps(mapinfo_links, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / THOUGHTS_INDEX).write_text(json.dumps(thought, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / TRAINING_INDEX).write_text(json.dumps(course, ensure_ascii=False, indent=2), encoding="utf-8")

    skill_dir = skill_dir or skill_root()
    thought_md = skill_dir / "references" / "mir200-thinking.md"
    thought_md.parent.mkdir(parents=True, exist_ok=True)
    thought_md.write_text(render_thoughts_markdown(thought, root), encoding="utf-8")
    training_md = skill_dir / "references" / "mir200-training.md"
    training_md.parent.mkdir(parents=True, exist_ok=True)
    training_md.write_text(render_training_markdown(course, root), encoding="utf-8")
    return {
        "docs": len(docs),
        "sample": len(sample),
        "mapinfo_links": len(mapinfo_links),
        "thoughts": len(thought.get("patterns", [])),
        "lessons": len(course.get("lessons", [])),
    }


def load_index(root: Path, name: str) -> list[dict[str, str]]:
    path = root / INDEX_DIR / name
    if not path.exists():
        write_indexes(root)
    return json.loads(path.read_text(encoding="utf-8"))


def tokenize(query: str) -> list[str]:
    return [token.lower() for token in re.findall(r"[\w\u4e00-\u9fff@#$<>.!\-\[\]]+", query) if token.strip()]


def score_record(record: dict[str, str], terms: list[str]) -> int:
    title = record.get("title", "").lower()
    rel = record.get("relative_path", "").lower()
    text = record.get("text", "").lower()
    score = 0
    for term in terms:
        if term in title:
            score += 12
        if term in rel:
            score += 6
        count = text.count(term)
        if count:
            score += min(count, 8)
    return score


def search_records(records: list[dict[str, str]], query: str, limit: int = 8) -> list[dict[str, str]]:
    terms = tokenize(query)
    if not terms:
        return []
    ranked = []
    for record in records:
        score = score_record(record, terms)
        if score:
            item = dict(record)
            item["score"] = score
            item["snippet"] = snippet(record.get("text", ""), terms)
            ranked.append(item)
    ranked.sort(key=lambda item: (-item["score"], item["relative_path"]))
    return ranked[:limit]


def snippet(text: str, terms: list[str], radius: int = 90) -> str:
    lower = text.lower()
    hit = min((lower.find(term) for term in terms if lower.find(term) >= 0), default=0)
    start = max(0, hit - radius)
    end = min(len(text), hit + radius)
    return text[start:end].strip()


def validate_root(root: Path) -> dict[str, object]:
    docs_index = root / INDEX_DIR / DOCS_INDEX
    sample_index = root / INDEX_DIR / SAMPLE_INDEX
    mapinfo_links_index = root / INDEX_DIR / MAPINFO_LINKS_INDEX
    thought_index = root / INDEX_DIR / THOUGHTS_INDEX
    training_index = root / INDEX_DIR / TRAINING_INDEX
    report = {
        "root": str(root),
        "knowledge_base_index": (root / "knowledge_base" / "index.md").exists(),
        "chapters_dir": (root / "knowledge_base" / "chapters").exists(),
        "sample_mir200_dir": (root / "样本Mir200").exists(),
        "docs_index": docs_index.exists(),
        "sample_index": sample_index.exists(),
        "mapinfo_links_index": mapinfo_links_index.exists(),
        "thoughts": thought_index.exists(),
        "training_course": training_index.exists(),
        "docs_index_records": 0,
        "sample_index_records": 0,
        "mapinfo_link_records": 0,
        "thought_patterns": 0,
        "training_lessons": 0,
    }
    if docs_index.exists():
        report["docs_index_records"] = len(json.loads(docs_index.read_text(encoding="utf-8")))
    if sample_index.exists():
        sample_records = json.loads(sample_index.read_text(encoding="utf-8"))
        report["sample_index_records"] = len(sample_records)
        report["thought_patterns"] = len(build_thought_summary(sample_records)["patterns"])
        report["training_lessons"] = len(build_training_course(sample_records)["lessons"])
    if mapinfo_links_index.exists():
        report["mapinfo_link_records"] = len(json.loads(mapinfo_links_index.read_text(encoding="utf-8")))
    report["ok"] = all(
        [
            report["knowledge_base_index"],
            report["chapters_dir"],
            report["sample_mir200_dir"],
            report["docs_index"],
            report["sample_index"],
            report["mapinfo_links_index"],
            report["thoughts"],
            report["training_course"],
        ]
    )
    return report


def cmd_update(root: Path) -> None:
    counts = write_indexes(root, skill_root())
    print(json.dumps({"ok": True, "root": str(root), **counts}, ensure_ascii=False, indent=2))


def cmd_search(root: Path, query: str, source: str, limit: int) -> None:
    records: list[dict[str, str]] = []
    if source in ("all", "docs"):
        records.extend(load_index(root, DOCS_INDEX))
    if source in ("all", "sample"):
        records.extend(load_index(root, SAMPLE_INDEX))
    if source in ("all", "mapinfo"):
        records.extend(load_index(root, MAPINFO_LINKS_INDEX))
    print(json.dumps(search_records(records, query, limit), ensure_ascii=False, indent=2))


def cmd_inspect(root: Path, rel_path: str, max_chars: int) -> None:
    path = (root / rel_path).resolve()
    if root.resolve() not in [path, *path.parents]:
        raise ValueError("Path escapes knowledge root.")
    text = read_text(path)
    print(text[:max_chars])


def main() -> None:
    parser = argparse.ArgumentParser(description="LF/Mir200 local knowledge base maintenance and search.")
    parser.add_argument("--root", help="Knowledge root containing knowledge_base/ and 样本Mir200/.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("update", help="Rebuild docs and sample-script indexes.")
    sub.add_parser("validate", help="Validate required files and indexes.")

    search = sub.add_parser("search", help="Search local docs and sample scripts.")
    search.add_argument("query")
    search.add_argument("--source", choices=["all", "docs", "sample", "mapinfo"], default="all")
    search.add_argument("--limit", type=int, default=8)

    inspect = sub.add_parser("inspect", help="Print a local knowledge file by relative path.")
    inspect.add_argument("relative_path")
    inspect.add_argument("--max-chars", type=int, default=12000)

    args = parser.parse_args()
    root = find_root(explicit_root=args.root).root
    if args.command == "update":
        cmd_update(root)
    elif args.command == "validate":
        print(json.dumps(validate_root(root), ensure_ascii=False, indent=2))
    elif args.command == "search":
        cmd_search(root, args.query, args.source, args.limit)
    elif args.command == "inspect":
        cmd_inspect(root, args.relative_path, args.max_chars)


if __name__ == "__main__":
    main()
