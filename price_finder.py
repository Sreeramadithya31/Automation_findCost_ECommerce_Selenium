import json
import re
from pathlib import Path
from decimal import Decimal, InvalidOperation

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def parse_price(raw_text: str):
    # Keep digits, decimal separators, and minus; treat comma as thousands separator.
    cleaned = re.sub(r"[^0-9.,]", "", raw_text).replace(",", "")
    if not cleaned:
        return None
    try:
        return Decimal(cleaned)
    except InvalidOperation:
        return None


def main():
    config_path = Path(__file__).resolve().parents[1] / "config.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    options = webdriver.ChromeOptions()
    if config.get("headless"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1365,900")

    driver = webdriver.Chrome(options=options)  # Selenium Manager handles driver setup
    try:
        driver.get(config["url"])
        WebDriverWait(driver, int(config.get("wait_seconds", 10))).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, config["price_selector"])
        )
        elements = driver.find_elements(By.CSS_SELECTOR, config["price_selector"])
        prices = []
        for element in elements:
            value = parse_price(element.text)
            if value is not None:
                prices.append((value, element.text.strip()))

        if not prices:
            print("No prices were found. Check the URL and price_selector in config.json.")
            return
        low = min(prices, key=lambda item: item[0])
        high = max(prices, key=lambda item: item[0])
        print(f"Prices parsed: {len(prices)}")
        print(f"Lowest price:  {low[1]} (numeric value: {low[0]})")
        print(f"Highest price: {high[1]} (numeric value: {high[0]})")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
