#!/usr/bin/env python3
"""Regenerate the Current Active Projects markdown table with best opportunities.

Best conference selection per project:
1) Earliest upcoming abstract close date (if available and not past)
2) Otherwise earliest upcoming conference start date
3) Otherwise earliest known conference start date

Best call-for-papers selection per project:
1) Earliest upcoming dated deadline
2) Ongoing
3) TBD
4) Most recent past dated deadline

Rows are sorted by conference priority date, then call deadline priority, then
impact factor (descending), then project name.
"""

from __future__ import annotations

import importlib.util
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_QMD = ROOT / "research" / "projects" / "index.qmd"
CONFERENCES_PATH = ROOT / "research" / "_conferences_data.py"
CALLS_PATH = ROOT / "research" / "_callforpapers_data.py"

TABLE_START = "| Project (Link) | Target Conference | Call for Paper | IF |"
TABLE_END_MARKER = ":::"

_SORT_MAX = datetime(9999, 12, 31)


def _load_module(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, str(path))
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


conferences_mod = _load_module(CONFERENCES_PATH, "_conferences_data")
calls_mod = _load_module(CALLS_PATH, "_callforpapers_data")

conferences = conferences_mod.conferences
conference_abstract_deadlines = conferences_mod.conference_abstract_deadlines
normalize_conference_url = conferences_mod.normalize_conference_url

call_for_papers = calls_mod.call_for_papers
SPECIAL_CALL_DUE_DATES = calls_mod.SPECIAL_CALL_DUE_DATES
SPECIAL_CALL_DUE_DATE_RULES = calls_mod.SPECIAL_CALL_DUE_DATE_RULES


@dataclass
class ConferenceOption:
    name: str
    url: str
    start_date: str
    abstract_display: str
    abstract_close_dt: Optional[datetime]
    start_dt: datetime


@dataclass
class CallOption:
    journal: str
    website: str
    due_date: str
    display_date: str
    impact: str
    due_dt: Optional[datetime]


@dataclass
class Row:
    project_name: str
    project_url: str
    conference: Optional[ConferenceOption]
    call: Optional[CallOption]
    row_sort_date: datetime
    row_call_sort: datetime
    row_impact_sort: float


def _parse_iso_date(value: str) -> Optional[datetime]:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return None


def _format_call_due_date(due_date: str, journal: str) -> str:
    if due_date in SPECIAL_CALL_DUE_DATE_RULES:
        return SPECIAL_CALL_DUE_DATE_RULES[due_date]["display_date"]
    try:
        return datetime.strptime(due_date, "%Y-%m-%d").strftime("%B %d, %Y")
    except ValueError as exc:
        raise ValueError(
            f"Invalid call-for-papers due_date {due_date!r} for journal {journal!r}"
        ) from exc


def _impact_numeric(impact: str) -> Optional[float]:
    if not impact:
        return None
    m = re.search(r"(\d+\.?\d*)", impact)
    return float(m.group(1)) if m else None


def _impact_display(impact: str) -> str:
    if not impact or impact == "N/A":
        return "—"
    return impact


def _conference_options_by_project() -> Dict[str, List[ConferenceOption]]:
    out: Dict[str, List[ConferenceOption]] = {}
    for conf in conferences:
        conf_url = conf.get("url", "")
        deadline_data = conference_abstract_deadlines.get(normalize_conference_url(conf_url), {})
        option = ConferenceOption(
            name=conf.get("name", ""),
            url=conf_url,
            start_date=conf.get("start_date", ""),
            abstract_display=deadline_data.get("abstract_display", "TBD"),
            abstract_close_dt=_parse_iso_date(conf.get("abstract_close", "")),
            start_dt=_parse_iso_date(conf.get("start_date", "")) or _SORT_MAX,
        )
        for project_url in conf.get("projects", []) or []:
            if not isinstance(project_url, str) or not project_url.strip():
                continue
            out.setdefault(project_url.strip().rstrip("/"), []).append(option)
    return out


def _call_options_by_project() -> Dict[str, List[CallOption]]:
    out: Dict[str, List[CallOption]] = {}
    for call in call_for_papers:
        option = CallOption(
            journal=call.get("journal", ""),
            website=call.get("website", ""),
            due_date=call.get("due_date", "TBD"),
            display_date=_format_call_due_date(call.get("due_date", "TBD"), call.get("journal", "")),
            impact=call.get("impact", ""),
            due_dt=_parse_iso_date(call.get("due_date", "")),
        )
        for project_url in call.get("projects", []) or []:
            if not isinstance(project_url, str) or not project_url.strip():
                continue
            out.setdefault(project_url.strip().rstrip("/"), []).append(option)
    return out


def _conference_rank(opt: ConferenceOption, now: datetime) -> Tuple[int, datetime, datetime]:
    # 0 = upcoming abstract deadline, 1 = upcoming conference date, 2 = fallback
    if opt.abstract_close_dt and opt.abstract_close_dt >= now:
        return (0, opt.abstract_close_dt, opt.start_dt)
    if opt.start_dt >= now:
        return (1, opt.start_dt, opt.start_dt)
    return (2, opt.start_dt, opt.start_dt)


def _call_rank(opt: CallOption, now: datetime) -> Tuple[int, datetime, float]:
    # 0 = upcoming dated deadline, 1 = ongoing, 2 = TBD, 3 = past dated
    imp = _impact_numeric(opt.impact)
    impact_sort = -(imp if imp is not None else -1.0)
    if opt.due_dt and opt.due_dt >= now:
        return (0, opt.due_dt, impact_sort)
    if opt.due_date == "Ongoing":
        return (1, _SORT_MAX.replace(day=30), impact_sort)
    if opt.due_date == "TBD":
        return (2, _SORT_MAX.replace(day=29), impact_sort)
    if opt.due_dt:
        return (3, opt.due_dt, impact_sort)
    return (3, _SORT_MAX, impact_sort)


def _extract_project_name_from_existing_table(text: str) -> Dict[str, str]:
    names: Dict[str, str] = {}
    row_re = re.compile(r"\| \[([^\]]+)\]\((https://github\.com/[^)]+)\) \|", re.IGNORECASE)
    for m in row_re.finditer(text):
        names[m.group(2).rstrip("/")] = m.group(1).strip()
    return names


def _slug_name(project_url: str) -> str:
    return project_url.rstrip("/").split("/")[-1]


def _build_rows(project_names: Dict[str, str]) -> List[Row]:
    now = datetime.now()
    conf_map = _conference_options_by_project()
    call_map = _call_options_by_project()

    project_urls = sorted(set(conf_map.keys()) | set(call_map.keys()))
    rows: List[Row] = []

    for project_url in project_urls:
        conf_options = conf_map.get(project_url, [])
        call_options = call_map.get(project_url, [])

        best_conf = min(conf_options, key=lambda c: _conference_rank(c, now)) if conf_options else None
        best_call = min(call_options, key=lambda c: _call_rank(c, now)) if call_options else None

        conf_sort = _conference_rank(best_conf, now)[1] if best_conf else _SORT_MAX
        call_sort = _call_rank(best_call, now)[1] if best_call else _SORT_MAX
        impact_val = _impact_numeric(best_call.impact) if best_call else None

        rows.append(
            Row(
                project_name=project_names.get(project_url, _slug_name(project_url)),
                project_url=project_url,
                conference=best_conf,
                call=best_call,
                row_sort_date=conf_sort,
                row_call_sort=call_sort,
                row_impact_sort=impact_val if impact_val is not None else -1.0,
            )
        )

    rows.sort(key=lambda r: (r.row_sort_date, r.row_call_sort, -r.row_impact_sort, r.project_name.lower()))
    return rows


def _render_rows(rows: Iterable[Row]) -> List[str]:
    lines: List[str] = []
    for row in rows:
        conf_cell = "TBD<br><em>Abstract: TBD</em>"
        if row.conference:
            conf_cell = (
                f"[{row.conference.name}]({row.conference.url})"
                f"<br><em>Abstract: {row.conference.abstract_display}</em>"
            )

        call_cell = "—"
        if row.call:
            call_cell = (
                f"**[{row.call.journal}]({row.call.website})**"
                f"<br><em>Deadline: {row.call.display_date}</em>"
            )

        impact_cell = _impact_display(row.call.impact if row.call else "")

        lines.append(
            f"| [{row.project_name}]({row.project_url}) | {conf_cell} | {call_cell} | {impact_cell} |"
        )
    return lines


def _replace_table(text: str, new_rows: List[str]) -> str:
    lines = text.splitlines()

    start_idx = None
    for idx, line in enumerate(lines):
        if line.strip() == TABLE_START:
            start_idx = idx
            break
    if start_idx is None:
        raise ValueError("Could not locate the Current Active Projects table header in projects/index.qmd")

    end_idx = None
    for idx in range(start_idx + 1, len(lines)):
        if lines[idx].strip() == TABLE_END_MARKER:
            end_idx = idx
            break
    if end_idx is None:
        raise ValueError("Could not locate the end of the Current Active Projects table wrapper in projects/index.qmd")

    header = lines[start_idx:start_idx + 2]
    replacement = header + new_rows

    return "\n".join(lines[:start_idx] + replacement + lines[end_idx:]) + "\n"


def main() -> int:
    original = PROJECTS_QMD.read_text(encoding="utf-8")
    project_names = _extract_project_name_from_existing_table(original)
    rows = _build_rows(project_names)
    rendered_rows = _render_rows(rows)
    updated = _replace_table(original, rendered_rows)

    if updated != original:
        PROJECTS_QMD.write_text(updated, encoding="utf-8")

    print(f"Updated Current Active Projects rows: {len(rendered_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
