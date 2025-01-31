#!/usr/bin/env python
from pathlib import Path
import json


voices = json.loads(Path('data/voices.json').read_text())
languages = {v['FriendlyName'].split(' - ')[-1].split(' (')[0] for v in voices}
