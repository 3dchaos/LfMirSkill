from __future__ import annotations

import argparse
import json
import os
import re
import sys
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
SCRIPT_LEARNING_MANUAL_TOPICS = [
    (
        "call",
        ["#CALL", "#CALLEX"],
        "knowledge_base/chapters/028-CallEx支持多个同样的@地址.md",
    ),
    (
        "script-params",
        ["$SCRIPTPARAM", "SCRIPTPARAM", "CHECKSCRIPTPARAM"],
        "knowledge_base/chapters/787-扩展NPC脚本点击触发带参数-NPC标签带参数.md",
    ),
    (
        "goto-return",
        ["GOTO", "RETURN"],
        "knowledge_base/chapters/163-GOTO将传递参数返回值保存到变量-脚本参数回调.md",
    ),
    (
        "npc-input",
        ["INPUTTEXT", "INPUTNUM", "$NPCINPUT", "NPCINPUT"],
        "knowledge_base/chapters/624-NPC对话框内默认输入框.md",
    ),
    (
        "timers",
        ["SETONTIMER", "SETOFFTIMER", "ONTIMER"],
        "knowledge_base/chapters/205-个人定时器.md",
    ),
    (
        "flags",
        ["SET [", "RESET [", "CHECK [", "$FLAG"],
        "knowledge_base/chapters/608-扩展check支持批量检测.md",
    ),
    (
        "variables",
        ["MOV ", "INC ", "DEC ", "$STR("],
        "knowledge_base/chapters/628-程序变量说明.md",
    ),
    (
        "arrays",
        ["L$", "GETLISTVAR", "CHECKVARINLIST", "SORTLIST"],
        "knowledge_base/chapters/192-多元数组元素变量.md",
    ),
    (
        "big-dialog",
        ["OPENMERCHANTBIGDLG", "LAYOUT:", "IMG:", "IMGEX:", "TEXT:", "MTEXT:"],
        "knowledge_base/chapters/782-脚本中使用图标功能.md",
    ),
]
EXTRA_THINKING_PRINCIPLES = [
    "`QMission-0.txt` 这类任务页展示脚本不要用 `GOTO @标签` 做当前进度页分发；菜单用 `<文本/@标签>` 直连，进度页把 `#IF / #SAY / #ACT BREAK` 直接写在目标标签里。",
]
EXTRA_PATTERN_NOTES = {
    "自动化与定时": [
        "LF script `#IF` starts an independent condition block; use `#ELSEACT BREAK` to stop failed prerequisites from falling through into the next `#IF` block.",
        "Variable classes are distinct. `L$` is the documented array/list family: assign with brackets (`MOV L$列表 [0,1,D1002]`), count/search with `GetListVarCount` / `CheckVarInList`, and read with `<$STR(L$列表[<$STR(N$下标)>])>`. `S$` and `N$` are extended string/number variables; `A` is a documented global string family often accepted by file/text commands. Confirm the family before inventing a prefix.",
        "Random selection has two patterns: use `RANDOM n` only as a `#IF` probability condition, and use `MOVR` when a random numeric value must be stored. For an in-script candidate list, use `MOVR N$下标 0 最大下标` plus `L$数组[<$STR(N$下标)>]`; for a file-backed list, use `GetRandomText 文件路径 S/A变量`.",
    ],
}


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


def print_json(data: object) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2)
    if hasattr(sys.stdout, "buffer"):
        sys.stdout.buffer.write((text + "\n").encode("utf-8"))
    else:
        print(text)


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


def _extract_script_labels(text: str) -> list[str]:
    labels = []
    for match in re.finditer(r"\[@([^\]\r\n]+)\]", text):
        label = match.group(1).strip()
        if label and label not in labels:
            labels.append(label)
    return labels


def _scan_script_patterns(text: str, signals: list[str]) -> list[str]:
    upper = text.upper()
    seen = []
    for signal in signals:
        if signal.upper() in upper and signal not in seen:
            seen.append(signal)
    return seen


def _find_script_lines(text: str, keywords: list[str], limit: int = 12) -> list[dict[str, object]]:
    lines = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        upper = raw.upper()
        if any(keyword.upper() in upper for keyword in keywords):
            lines.append({"line": lineno, "text": raw.strip()})
    return lines[:limit]


def _collect_variables(text: str) -> dict[str, list[str]]:
    families: dict[str, list[str]] = {
        "N$": [],
        "S$": [],
        "T$": [],
        "U$": [],
        "L$": [],
        "A$": [],
        "G$": [],
        "N": [],
        "S": [],
        "T": [],
        "U": [],
        "D": [],
        "P": [],
        "A": [],
        "G": [],
        "I": [],
        "J": [],
        "Z": [],
    }
    patterns = {
        "N$": r"\bN\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "S$": r"\bS\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "T$": r"\bT\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "U$": r"\bU\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "L$": r"\bL\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "A$": r"\bA\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "G$": r"\bG\$[A-Za-z0-9_\u4e00-\u9fff]+",
        "N": r"(?<![A-Z$])N\d{1,3}\b",
        "S": r"(?<![A-Z$])S\d{1,3}\b",
        "T": r"(?<![A-Z$])T\d{1,3}\b",
        "U": r"(?<![A-Z$])U\d{1,3}\b",
        "D": r"(?<![A-Z$])D\d{1,3}\b",
        "P": r"(?<![A-Z$])P\d{1,3}\b",
        "A": r"(?<![A-Z$])A\d{1,3}\b",
        "G": r"(?<![A-Z$])G\d{1,3}\b",
        "I": r"(?<![A-Z$])I\d{1,3}\b",
        "J": r"(?<![A-Z$])J\d{1,3}\b",
        "Z": r"(?<![A-Z$])Z\d{1,3}\b",
    }
    for family, pattern in patterns.items():
        matches = []
        for match in re.findall(pattern, text, flags=re.IGNORECASE):
            if match not in matches:
                matches.append(match)
        families[family] = matches
    return families


def _collect_timers(text: str) -> list[dict[str, str]]:
    timers = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        match = re.search(r"\bSETONTIMER(EX)?\s+(\d+)\s+([^\s]+)", raw, flags=re.IGNORECASE)
        if not match:
            match = re.search(r"\bSETOFFTIMER(EX)?\s+(\d+)", raw, flags=re.IGNORECASE)
            if match:
                timers.append({"line": str(lineno), "op": "SETOFFTIMER", "id": match.group(2)})
            continue
        timers.append({"line": str(lineno), "op": "SETONTIMEREX" if match.group(1) else "SETONTIMER", "id": match.group(2), "interval": match.group(3)})
    return timers


def _collect_calls(text: str) -> list[dict[str, str]]:
    calls = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        match = re.search(r"#CALL(?:EX)?\s+\[([^\]]+)\]\s+(@[^\s]+)", raw, flags=re.IGNORECASE)
        if match:
            calls.append({"line": str(lineno), "path": match.group(1), "label": match.group(2)})
    return calls


def _collect_itemboxes(text: str) -> list[dict[str, str]]:
    boxes = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        match = re.search(r"<ITEMBOX:([^:>]+):", raw, flags=re.IGNORECASE)
        if match:
            boxes.append({"line": str(lineno), "id": match.group(1)})
    return boxes


def _collect_input_controls(text: str) -> list[dict[str, str]]:
    inputs = []
    for lineno, raw in enumerate(text.splitlines(), start=1):
        for kind in ("INPUTTEXT", "INPUTNUM"):
            match = re.search(rf"<{kind}:([^:>]+):", raw, flags=re.IGNORECASE)
            if match:
                inputs.append({"line": str(lineno), "kind": kind, "id": match.group(1)})
    return inputs


def _collect_flags(text: str) -> list[str]:
    flags = []
    for match in re.finditer(r"\$FLAG\((\d+)\)|\b(?:SET|CHECK)\s+\[(\d+)\]", text, flags=re.IGNORECASE):
        value = match.group(1) or match.group(2)
        if value and value not in flags:
            flags.append(value)
    return flags


def _manual_topics_for_script(text: str) -> list[str]:
    topics = []
    upper = text.upper()
    for _name, signals, manual_path in SCRIPT_LEARNING_MANUAL_TOPICS:
        if any(signal.upper() in upper for signal in signals):
            topics.append(manual_path)
    return topics


def _learning_notes_for_script(labels: list[str], calls: list[dict[str, str]], text: str) -> list[str]:
    notes = []
    if labels:
        notes.append("先按标签画流程图，再分别看入口、守门、动作和返回路径。")
    if calls:
        notes.append("有 #CALL/#CALLEX 的地方先确认被调用文件，再回看调用点是否只是派发。")
    if "GOTO" in text.upper():
        notes.append("遇到 GOTO 先确认它是在跳分支还是跳回主菜单。")
    if any(signal in text.upper() for signal in ("INPUTTEXT", "INPUTNUM", "$NPCINPUT")):
        notes.append("输入框要顺着输入ID查回写变量和失败提示。")
    if any(signal in text.upper() for signal in ("SETONTIMER", "SETOFFTIMER", "ONTIMER")):
        notes.append("定时器要一起看开启点、关闭点和触发标签。")
    if any(signal in text.upper() for signal in ("ITEMBOX", "BOXITEM", "RETURNBOXITEM", "SETUPGRADEITEM")):
        notes.append("物品框脚本要同时检查取物、改名、刷新和归还。")
    if any(signal in text.upper() for signal in ("L$", "GETLISTVAR", "CHECKVARINLIST")):
        notes.append("数组处理要先确认是否已有 L$ 方案，再决定是否需要文本列表。")
    return notes


def analyze_script_learning(root: Path, rel_path: str) -> dict[str, object]:
    path = (root / rel_path).resolve()
    if root.resolve() not in [path, *path.parents]:
        raise ValueError("Path escapes knowledge root.")
    text = read_text(path)
    labels = _extract_script_labels(text)
    calls = _collect_calls(text)
    inputs = _collect_input_controls(text)
    boxes = _collect_itemboxes(text)
    timers = _collect_timers(text)
    flags = _collect_flags(text)
    variables = _collect_variables(text)
    manual_topics = _manual_topics_for_script(text)
    notes = _learning_notes_for_script(labels, calls, text)
    return {
        "relative_path": normalize_rel(path.relative_to(root)),
        "labels": labels,
        "calls": calls,
        "flags": flags,
        "npc_inputs": [item["id"] for item in inputs],
        "item_boxes": boxes,
        "timers": timers,
        "variables": variables,
        "manual_topics": manual_topics,
        "learning_notes": notes,
        "line_hits": _find_script_lines(text, ["#CALL", "#CALLEX", "GOTO", "INPUTTEXT", "INPUTNUM", "SETONTIMER", "SETOFFTIMER", "ITEMBOX", "RETURNBOXITEM", "UPDATEITEM", "MOV ", "SET [", "CHECK [", "$FLAG", "L$"]),
        "script_signals": _scan_script_patterns(
            text,
            [
                "OPENMERCHANTBIGDLG",
                "ITEMBOX",
                "INPUTTEXT",
                "INPUTNUM",
                "#CALL",
                "GOTO",
                "SETONTIMER",
                "SETOFFTIMER",
                "MOV ",
                "SET [",
                "CHECK [",
                "$FLAG",
                "L$",
            ],
        ),
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
    for item in EXTRA_THINKING_PRINCIPLES:
        lines.append(f"- {item}")
    lines.extend(["", "## Patterns", ""])
    for pattern in summary.get("patterns", []):
        signals = ", ".join(pattern.get("signals", []))
        lines.append(f"- {pattern.get('name')} ({pattern.get('count', 0)}): {signals}")
        for note in EXTRA_PATTERN_NOTES.get(str(pattern.get("name")), []):
            lines.append(f"  - {note}")
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
            "- Treat the manual as syntax authority and `样本Mir200` as practical usage authority. For arrays, the strongest evidence is `knowledge_base/chapters/192-多元数组元素变量.md` plus sample scripts such as `样本Mir200/Envir/Market_def/酒馆/翔天-3.txt` and `样本Mir200/Envir/Market_def/其它区域/踏云尊者-yssd.txt`.",
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
    print_json({"ok": True, "root": str(root), **counts})


def cmd_search(root: Path, query: str, source: str, limit: int) -> None:
    records: list[dict[str, str]] = []
    if source in ("all", "docs"):
        records.extend(load_index(root, DOCS_INDEX))
    if source in ("all", "sample"):
        records.extend(load_index(root, SAMPLE_INDEX))
    if source in ("all", "mapinfo"):
        records.extend(load_index(root, MAPINFO_LINKS_INDEX))
    print_json(search_records(records, query, limit))


def cmd_inspect(root: Path, rel_path: str, max_chars: int) -> None:
    path = (root / rel_path).resolve()
    if root.resolve() not in [path, *path.parents]:
        raise ValueError("Path escapes knowledge root.")
    text = read_text(path)
    print(text[:max_chars])


def cmd_learn_script(root: Path, rel_path: str) -> None:
    report = analyze_script_learning(root, rel_path)
    print_json(report)


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

    learn = sub.add_parser("learn-script", help="Build a static learning report for a sample Mir200 script.")
    learn.add_argument("relative_path")

    args = parser.parse_args()
    root = find_root(explicit_root=args.root).root
    if args.command == "update":
        cmd_update(root)
    elif args.command == "validate":
        print_json(validate_root(root))
    elif args.command == "search":
        cmd_search(root, args.query, args.source, args.limit)
    elif args.command == "inspect":
        cmd_inspect(root, args.relative_path, args.max_chars)
    elif args.command == "learn-script":
        cmd_learn_script(root, args.relative_path)


if __name__ == "__main__":
    main()
