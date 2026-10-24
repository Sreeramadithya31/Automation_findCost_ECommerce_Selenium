# E-commerce Price Range Finder 🛍️

A Selenium-based browser automation project that searches a product page, extracts visible prices, normalizes currency strings, and reports the lowest and highest prices found. This reflects the aim described in the supplied Automated Testing Tools–Selenium micro-project report.

## Features
- Opens a configured product/search page with Selenium
- Collects price elements using configurable CSS selectors
- Normalizes price strings such as `₹1,299` into numeric values
- Reports minimum, maximum, and count of parsed prices
- Uses explicit configuration because websites have different page structures

## Requirements
- Python 3.10+
- Google Chrome
- Selenium 4

## Setup and Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Edit `config.json` with the target URL and a selector that matches the website's price elements, then run:

```bash
python src/price_finder.py
```

## Important
This is a reference implementation, not a universal scraper. E-commerce websites frequently change their markup and may restrict automated access. Follow each website's terms, robots policy, and applicable law. No login bypass or anti-bot circumvention is included.
