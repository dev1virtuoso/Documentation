import asyncio
import aiohttp
import aiofiles
import json
import pandas as pd
import warnings
from tqdm import tqdm

ORIGINAL_ENTRIES_PATH = '/Library/Application Support/com.apple.idleassetsd/Customer/entries.json'

with open(ORIGINAL_ENTRIES_PATH, 'r') as f:
    ENTRIES = json.load(f)

DISPLAY_NAMES = pd.read_csv('data/display_names.csv').reset_index().set_index('assetId')

ASSET_URLS = pd.DataFrame([
    {'assetId': asset['id'], 'previewImage': asset['previewImage'], 'fullVideo': asset['url-4K-SDR-240FPS'}
    for asset in ENTRIES['assets']
]).set_index('assetId')

NAMES_AND_URLS = DISPLAY_NAMES.join(ASSET_URLS)

if len(ASSET_URLS) > len(DISPLAY_NAMES):
    warnings.warn(f'There are {len(ASSET_URLS)} assets but only {len(DISPLAY_NAMES)} display names. Some assets will be missing from the output.')


async def download_with_progress(session: aiohttp.ClientSession, url: str, filename: str):
    async with session.get(url, verify_ssl=False) as response:
        total = int(response.headers.get('content-length', 0))
        progress_bar = tqdm(total=total, desc=filename, unit='B', unit_scale=True)
        
        async with aiofiles.open(filename, mode='wb') as f:
            while True:
                chunk = await response.content.read(1024)  # Adjust chunk size as needed
                if not chunk:
                    break
                await f.write(chunk)
                progress_bar.update(len(chunk))
        
        progress_bar.close()


async def download_all_with_progress(urls: pd.Series, folder: str):
    async