#!/usr/bin/env python
from pathlib import Path
import asyncio
import json

import edge_tts


async def main():
    voices = await edge_tts.voices.list_voices()
    Path('data/voices.json').write_text(json.dumps(voices))


asyncio.run(main())