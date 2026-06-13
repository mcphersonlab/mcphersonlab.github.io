#!/usr/bin/env python3
"""Parse /tmp/conference_report.json and propose ISO start/end dates for conferences.
"""
import json
import re
from datetime import datetime

REPORT = "/tmp/conference_report.json"

MONTHS = {
    'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12,
    'jan':1,'feb':2,'mar':3,'apr':4,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12
}

# patterns for ranges like 'February 20-24, 2027' or 'Feb 20, 2027 - Feb 24, 2027'
RANGE1 = re.compile(r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})\s*[\-–]\s*(\d{1,2})\,?\s*(20\d{2})", re.I)
RANGE2 = re.compile(r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(\d{1,2})\,?\s*(?:-|to|–)\s*(?:[A-Za-z]+\s+)?(\d{1,2})\,?\s*(20\d{2})", re.I)
RANGE3 = re.compile(r"(\d{1,2})\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*[\-–]\s*(\d{1,2})\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)?\s*,?\s*(20\d{2})", re.I)
SINGLEDATE = re.compile(r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?).{0,6}?(\d{1,2})\,?\s*(20\d{2})", re.I)

with open(REPORT) as f:
    data = json.load(f)

proposals = {}

for entry in data:
    name = entry.get('name')
    text = '\n'.join(entry.get('found_dates', []) + entry.get('found_abstracts', []))
    if not text:
        continue
    m = RANGE1.search(text) or RANGE2.search(text) or RANGE3.search(text)
    if m:
        # handle RANGE1
        try:
            if len(m.groups()) == 4:
                mon = m.group(1)
                d1 = int(m.group(2))
                d2 = int(m.group(3))
                year = int(m.group(4))
                mon_n = MONTHS[mon.lower()[:3]]
                start = datetime(year, mon_n, d1).date().isoformat()
                end = datetime(year, mon_n, d2).date().isoformat()
                proposals[name] = {'start_date': start, 'end_date': end, 'source':'range-pattern'}
                continue
        except Exception:
            pass
    # fallback to single date: take the first occurrence
    m2 = SINGLEDATE.search(text)
    if m2:
        try:
            mon = m2.group(1)
            d = int(m2.group(2))
            year = int(m2.group(3))
            mon_n = MONTHS[mon.lower()[:3]]
            dt = datetime(year, mon_n, d).date().isoformat()
            proposals[name] = {'start_date': dt, 'end_date': dt, 'source':'single-date'}
        except Exception:
            continue

print(json.dumps(proposals, indent=2))
