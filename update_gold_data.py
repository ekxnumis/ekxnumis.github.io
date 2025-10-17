import requests
import json
import os
import time
from datetime import datetime, timedelta

# ========================
# Configuration
# ========================
API_KEY = "401c08752f6bf01b023d4d70cdf20131"
BASE_URL = "https://api.metalpriceapi.com/v1"
CURRENCY = "GBP"
CACHE_FILE = os.path.join("_data", "gold_prices.json")
CACHE_TTL = 3600  # 1 hour in seconds

# ========================
# Helper Functions
# ========================

def fetch_price(endpoint, params=None):
    """Fetch data from MetalpriceAPI with error handling."""
    url = f"{BASE_URL}/{endpoint}"
    if params is None:
        params = {}
    params["api_key"] = API_KEY

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"❌ Error fetching from {url}: {e}")
        return None

def fetch_all_gold_data():
    """Fetch live and historical gold data."""
    print("🔄 Fetching latest gold data...")

    live_data = fetch_price("latest", {"base": "XAU", "currencies": CURRENCY})
    if not live_data:
        return None

    now = datetime.utcnow()
    historical_data = {}

    ranges = {
        "week": now - timedelta(days=7),
        "month": now - timedelta(days=30),
        "6month": now - timedelta(days=182),
        "year": now - timedelta(days=365),
        "5year": now - timedelta(days=1825),
        "10year": now - timedelta(days=3650),
        "15year": now - timedelta(days=5475),
        "20year": now - timedelta(days=7300)
    }

    for label, date in ranges.items():
        formatted_date = date.strftime("%Y-%m-%d")
        hist = fetch_price("timeseries", {
            "base": "XAU",
            "currencies": CURRENCY,
            "start_date": formatted_date,
            "end_date": now.strftime("%Y-%m-%d")
        })
        if hist:
            historical_data[label] = hist

    return {
        "timestamp": now.isoformat(),
        "live": live_data,
        "historical": historical_data
    }

# ========================
# Main Caching Logic
# ========================

def is_cache_valid():
    """Check if the cache file is still valid (less than 1 hour old)."""
    if not os.path.exists(CACHE_FILE):
        return False
    age = time.time() - os.path.getmtime(CACHE_FILE)
    return age < CACHE_TTL

def load_cached_data():
    """Load data from cache file."""
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_to_cache(data):
    """Write new data to cache file."""
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Updated cache file: {CACHE_FILE}")

def main():
    if is_cache_valid():
        print("✅ Cache is still fresh — no need to fetch new data.")
        cached = load_cached_data()
        print(f"Last update: {cached.get('timestamp', 'unknown')}")
        return

    print("🕒 Cache expired — fetching fresh data...")
    data = fetch_all_gold_data()
    if data:
        save_to_cache(data)
    else:
        print("⚠️ Failed to fetch new data, keeping old cache if it exists.")

if __name__ == "__main__":
    main()
