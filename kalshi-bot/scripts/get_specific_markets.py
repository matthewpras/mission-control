import requests
import json

url = "https://api.elections.kalshi.com/trade-api/v2/markets"
target_series = ["FED", "INX", "NASDAQ100", "BTC", "CPI", "KXU3", "GOLD"]
found_markets = []

for series in target_series:
    params = {
        "status": "open",
        "limit": 5,
        "series_ticker": series
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        found_markets.extend(response.json().get("markets", []))

for m in found_markets:
    title = m['title'].encode('ascii', 'ignore').decode('ascii')
    print(f"Ticker: {m['ticker']} | Title: {title} | Yes: {m['yes_bid']}c / No: {m['no_bid']}c")
