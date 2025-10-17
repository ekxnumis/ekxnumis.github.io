# =========================================
# update_gold_prices.py
# Scrapes gold prices from BullionByPost and updates JSON files
# =========================================

import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Folder where JSON files are stored
DATA_DIR = "assets/data"

# Ensure directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# URL for the current gold price per gram (GBP)
URL = "https://www.bullionbypost.co.uk/gold-price/gold-price-chart-gram-gbp/#show-chart"


def fetch_gold_price():
    """Fetch latest gold price per gram (GBP) from BullionByPost."""
    print("Fetching live gold price from BullionByPost...")
    response = requests.get(URL, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Look for the price inside the <span id="metal-price"> tag
    price_span = soup.find("span", id="metal-price")
    if not price_span:
        raise ValueError("Price element not found on the page")

    # Extract numeric price
    price_text = price_span.get_text(strip=True)
    # Expect something like "£84.32 per gram"
    price_value = float(price_text.replace("£", "").split()[0])

    print(f"✅ Current gold price per gram: £{price_value}")
    return price_value


def update_json(file_name, new_price):
    """Append today's date and price to a JSON file."""
    file_path = os.path.join(DATA_DIR, file_name)
    today = datetime.now().strftime("%Y-%m-%d")

    # Load existing data or create new list
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Check if today's entry already exists
    if data and data[-1]["date"] == today:
        print(f"⚠️ Already updated for today in {file_name}")
        return

    # Append new entry
    data.append({"date": today, "price": round(new_price, 2)})

    # Trim data (optional)
    if "6month" in file_name and len(data) > 180:
        data = data[-180:]
    elif "year" in file_name and len(data) > 365:
        data = data[-365:]

    # Save JSON
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"💾 Updated {file_name} with {today}: £{new_price}")


def main():
    try:
        price = fetch_gold_price()

        # Update all relevant JSONs
        update_json("gold_today.json", price)
        update_json("gold_week.json", price)
        update_json("gold_month.json", price)
        update_json("gold_6month.json", price)
        update_json("gold_year.json", price)
        update_json("gold_5y.json", price)
        update_json("gold_10y.json", price)
        update_json("gold_15y.json", price)
        update_json("gold_20y.json", price)

        print("\n✅ All JSON files updated successfully.")
    except Exception as e:
        print("❌ Error:", e)


if __name__ == "__main__":
    main()
