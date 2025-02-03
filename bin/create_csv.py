#!/usr/bin/env python
from pathlib import Path
import csv
import json

voices = json.loads(Path('data/voices.json').read_text())
voice_names = {}
rows = [['Name', 'Gender', 'Language', 'Categories', 'Personalities', 'Speech Sample']]

for sample in Path('mp3').glob('**/*.mp3'):
    lang, voice = sample.parent.name, sample.stem
    voice_names[voice] = {'language': lang, 'path': sample.as_posix()}

for voice in voices:
    name = voice['ShortName']
    if name in voice_names:
        rows.append([voice['FriendlyName'].split(' - ')[0].replace('Microsoft ', '').replace(' Online (Natural)', ''),
                     voice['Gender'],
                     voice_names[name]['language'],
                     ', '.join(voice['VoiceTag']['ContentCategories']),
                     ', '.join(voice['VoiceTag']['VoicePersonalities']),
                     voice_names[name]['path']
                     ])

csv.writer(Path('data/tts-samples.csv').open('w')).writerows(rows)