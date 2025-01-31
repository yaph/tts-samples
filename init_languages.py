#!/usr/bin/env python
from pathlib import Path
import json


voices = json.loads(Path('data/voices.json').read_text())
languages = {}

for v in voices:
    lang = v['FriendlyName'].split(' - ')[-1].split(' (')[0].strip()
    code = v['Locale'].split('-')[0].strip()
    languages[code] = {
        'language': lang,
        'text': ''
    }

Path('data/languages.json').write_text(json.dumps(languages))