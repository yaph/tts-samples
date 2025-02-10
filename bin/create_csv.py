#!/usr/bin/env python
from pathlib import Path
import csv
import json

from pycountry import countries

voices = json.loads(Path('data/voices.json').read_text())
voice_names = {}
rows = [['Name', 'Gender', 'Language', 'Country', 'Categories', 'Personalities', 'Sample']]

for sample in Path('mp3').glob('**/*.mp3'):
    lang, voice = sample.parent.name, sample.stem
    voice_names[voice] = {'language': lang, 'path': sample.as_posix()}

for voice in voices:
    name = voice['ShortName']
    if name in voice_names:
        country = countries.get(alpha_2=voice['Locale'].split('-')[1]).name
        rows.append([voice['FriendlyName'].split(' - ')[0].replace('Microsoft ', '').replace(' Online (Natural)', ''),
                     voice['Gender'],
                     voice_names[name]['language'],
                     country,
                     ', '.join(voice['VoiceTag']['ContentCategories']),
                     ', '.join(voice['VoiceTag']['VoicePersonalities']),
                     voice_names[name]['path']
                     ])

csv.writer(Path('data/tts-samples.csv').open('w')).writerows(rows)