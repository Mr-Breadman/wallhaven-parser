# Wallhaven Dark Wallpaper Parser

A Python script that downloads wallpapers from [Wallhaven.cc](https://wallhaven.cc) with parallel downloading via multiprocessing.

> ⚠️ **Note:** This script is configured to download wallpapers from the **"Dark" category only**. If you want other categories, change the `q=` parameter in the search URL (see "Customization" below).

## Features

- Collects wallpaper links from multiple search pages
- Extracts direct image URLs from detail pages
- Downloads images in parallel using `multiprocessing`
- Skips already downloaded files and broken links
- Respects request timeouts (5s) and adds delays between page requests

## Customisation

- start_page = 1   # first page to parse
- end_page = 5     # last page to parse

To change the wallpaper category, edit the search URL in the link variable:
link = f'https://wallhaven.cc/search?q=id%3A369&categories=110&purity=100&sorting=favorites&order=desc&page={page}'
    
    q=id%3A369 — preset search filter (Dark category);
    
    categories=110 — categories (general / anime / people);
    
    purity=100 — content purity (SFW / Sketchy / NSFW);
    
    sorting=favorites — sorting type.

For more filter options, visit Wallhaven search and copy the URL parameters.

## Requirements

- Python 3.10+
- Libraries: `requests`, `beautifulsoup4`, `lxml`, `fake-useragent`

## Installation

```bash
git clone https://github.com/YOUR-USERNAME/wallhaven-parser.git
cd wallhaven-parser
pip install -r requirements.txt
