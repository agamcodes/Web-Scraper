# Python Web Scraper

A beginner-friendly Python web scraper using `requests` and `BeautifulSoup4`.

## Files

- `0_retrieving_html.py` — Fetches raw HTML from a target URL
- `1_bs4.py` — Parses the HTML using BeautifulSoup
- `fresh_proxies.py` — Retrieves fresh proxies for anonymous scraping
- `file.html` — Sample HTML for local testing

## Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4`

Install dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the scripts in order:

```bash
python 0_retrieving_html.py
python 1_bs4.py
```

To use proxies:

```bash
python fresh_proxies.py
```