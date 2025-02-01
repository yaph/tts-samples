#!/usr/bin/env python
from pathlib import Path
import json

import edge_tts


voices = json.loads(Path('data/voices.json').read_text())
languages = json.loads(Path('data/languages-with-text.json').read_text())

# Add list of voices to each language item
for v in voices:
    code = v['Locale'].split('-')[0]
    languages[code]['voices'] = languages[code].get('voices', []) + [v['ShortName']]

# Create mp3 files for each language and voice
for lang in languages.values():
    p_lang = Path('mp3', lang['language'])
    p_lang.mkdir(exist_ok=True)
    for voice in lang.get('voices', []):
        p_voice = p_lang / f'{voice}.mp3'
        if p_voice.exists():
            continue

        try:
            communicate = edge_tts.Communicate(lang['text'], voice)
            communicate.save_sync(p_voice)
        except ValueError as e:
            print(e)
