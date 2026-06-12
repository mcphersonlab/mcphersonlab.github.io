#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path

proposals = json.load(open('/tmp/conference_proposals.json'))
# Import conferences from module
import importlib.util
from pathlib import Path
conf_path = Path(__file__).resolve().parents[1] / 'research' / '_conferences_data.py'
spec = importlib.util.spec_from_file_location('_conferences_data', str(conf_path))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
confs = mod.conferences

by_name = {c['name']: c for c in confs}

candidates = {}
for name, p in proposals.items():
    try:
        sd = datetime.fromisoformat(p['start_date'])
        ed = datetime.fromisoformat(p['end_date'])
    except Exception:
        continue
    if ed < sd:
        continue
    if sd.year < 2026 and ed.year < 2026:
        continue
    if name not in by_name:
        continue
    cur = by_name[name]
    if cur.get('start_date') != p['start_date'] or cur.get('end_date') != p['end_date']:
        candidates[name] = {'current': (cur.get('start_date'), cur.get('end_date')),'proposed':(p['start_date'],p['end_date'])}

print(json.dumps(candidates, indent=2))
