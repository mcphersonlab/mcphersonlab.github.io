#!/usr/bin/env python3
"""Fetch each conference URL and try to extract date and abstract deadline hints.
Produces a JSON-like report printed to stdout.
"""
import re
import json
import sys
from urllib.parse import urlparse

# Import conferences from repo
import importlib.util
from pathlib import Path

# Load conferences from the repository file directly
conf_path = Path(__file__).resolve().parents[1] / "research" / "_conferences_data.py"
spec = importlib.util.spec_from_file_location("_conferences_data", str(conf_path))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
conferences = getattr(mod, "conferences")

import requests
from bs4 import BeautifulSoup

YEARS = ["2024","2025","2026","2027","2028"]
MONTH_RE = r"(?:January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
DATE_PATTERNS = [
    re.compile(rf"({MONTH_RE}\s+\d{{1,2}}(?:[–\-]\d{{1,2}})?\,?\s*(?:{"|".join(YEARS)}))", re.I),
    re.compile(rf"(\d{{4}}[\-–]\d{{4}})", re.I),
    re.compile(rf"(20\d{{2}})"),
]
ABSTRACT_PAT = re.compile(r"abstract|abstracts|call for abstracts|submission deadline|abstract deadline|call for papers", re.I)

session_results = []

for conf in conferences:
    url = conf.get("url")
    name = conf.get("name")
    entry = {"name": name, "url": url, "found_dates": [], "found_abstracts": []}
    if not url:
        session_results.append(entry)
        continue
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent": "mcphersonlab-bot/1.0"})
        text = r.text
    except Exception as e:
        entry["error"] = str(e)
        session_results.append(entry)
        continue
    soup = BeautifulSoup(text, "lxml")
    visible = soup.get_text(separator="\n")
    # Search for date patterns
    for pat in DATE_PATTERNS:
        for m in pat.finditer(visible):
            span = visible[max(0, m.start()-80):m.end()+80].strip()
            entry["found_dates"].append(span)
            if len(entry["found_dates"])>8:
                break
        if len(entry["found_dates"])>0:
            break
    # Search for abstract-related snippets
    for m in ABSTRACT_PAT.finditer(visible):
        span = visible[max(0, m.start()-120):m.end()+120].strip()
        entry["found_abstracts"].append(span)
        if len(entry["found_abstracts"])>6:
            break
    session_results.append(entry)

print(json.dumps(session_results, indent=2))
