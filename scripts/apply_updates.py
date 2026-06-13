#!/usr/bin/env python3
"""Apply selected conference date updates to research/_conferences_data.py

Expects /tmp/candidates.json to contain a mapping of conference name -> {current, proposed}.
The script updates `start_date` and `end_date` fields in-place and prints a JSON summary.
"""
import json
import re
from pathlib import Path
import sys

CANDIDATES = Path('/tmp/candidates.json')
TARGET = Path(__file__).resolve().parents[1] / 'research' / '_conferences_data.py'

if not CANDIDATES.exists():
    print(json.dumps({'error': 'candidates file not found'}))
    sys.exit(0)

data = json.load(open(CANDIDATES))
if not data:
    print(json.dumps({'updated': []}))
    sys.exit(0)

text = TARGET.read_text(encoding='utf8')
orig_text = text
updates = []

for name, info in data.items():
    proposed = info['proposed']
    sd_new, ed_new = proposed
    # find the name occurrence
    name_token = f'"name": "{name.replace("\"", "\\\"")}"'
    pos = text.find(name_token)
    if pos == -1:
        # try a more relaxed search (escaped characters)
        pos = text.find(f'"name": "{name.split("(")[0].strip()}')
    if pos == -1:
        continue

    # find opening brace of this dict
    start_brace = text.rfind('{', 0, pos)
    # find the end of the dict (first occurrence of '},' after pos)
    end_brace = text.find('},', pos)
    if end_brace == -1:
        end_brace = text.find('\n}\n', pos)
    if end_brace == -1:
        continue

    block = text[start_brace:end_brace+1]

    # replace or insert start_date
    sd_match = re.search(r'("start_date"\s*:\s*")([0-9\-]*)("\s*,?)', block)
    if sd_match:
        block = block[:sd_match.start(2)] + sd_new + block[sd_match.end(2):]
    else:
        # insert after the "name" line
        name_line_end = block.find('\n', block.find('"name"'))
        insert = '\n        "start_date": "' + sd_new + '",' 
        block = block[:name_line_end+1] + insert + block[name_line_end+1:]

    # replace or insert end_date
    ed_match = re.search(r'("end_date"\s*:\s*")([0-9\-]*)("\s*,?)', block)
    if ed_match:
        block = block[:ed_match.start(2)] + ed_new + block[ed_match.end(2):]
    else:
        # try to insert after start_date line if present
        sd_line = block.find('"start_date"')
        if sd_line != -1:
            sd_line_end = block.find('\n', sd_line)
            insert2 = '\n        "end_date": "' + ed_new + '",' 
            block = block[:sd_line_end+1] + insert2 + block[sd_line_end+1:]
        else:
            # fallback: insert after name line
            name_line_end = block.find('\n', block.find('"name"'))
            insert2 = '\n        "end_date": "' + ed_new + '",' 
            block = block[:name_line_end+1] + insert2 + block[name_line_end+1:]

    # apply the block replacement
    text = text[:start_brace] + block + text[end_brace+1:]
    updates.append({'name': name, 'proposed': proposed})

if text != orig_text:
    TARGET.write_text(text, encoding='utf8')

print(json.dumps({'updated': updates}, indent=2))
