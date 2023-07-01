import os
import time

import aiohttp
import asyncio
import json
from typing import List

import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"
multiple_dots = r'\.{2,}'


def split_sentences(text: str) -> list[str]:
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    text = re.sub(multiple_dots, lambda match: "<prd>" * len(match.group(0)) + "<stop>", text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = [s.strip() for s in sentences]
    if sentences and not sentences[-1]: sentences = sentences[:-1]
    return sentences


async def send_text_to_api(path:str, text: str, voice_id: str, api_keys: List[str], idx: int):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            api_key = api_keys[idx % len(api_keys)]  # rotate through API keys
            headers = {
                'accept': 'audio/mpeg',
                'xi-api-key': api_key,
                'Content-Type': 'application/json'
            }
            async with session.post(url, headers=headers, data=json.dumps(data)) as response:
                if response.status == 200:
                    audio_content = await response.read()
                    if not os.path.exists(f'audio_files/{path}'):
                        os.makedirs(f'audio_files/{path}')
                    with open(f'audio_files/{path}/{idx+1}.mp3', 'wb') as f:
                        f.write(audio_content)
                    break
                else:
                    print(f'Request failed with status {response.status}, retrying...')
                await asyncio.sleep(1)


async def generate(path: str,text: str):
    voice_id = "EXAVITQu4vr4xnSDxMaL"
    api_keys = ["b287d7668a6e607efde82f3ae4e658fa", "a93039384fc501f3163f71a114470127",
                "30a39f55223f566e41c93b5d6c227d64"]
    sentences = split_sentences(text)
    print(sentences)
    tasks = []
    for idx, sentence in enumerate(sentences):
        tasks.append(asyncio.create_task(send_text_to_api(path, sentence, voice_id, api_keys, idx)))
    await asyncio.gather(*tasks)
    return len(sentences)
