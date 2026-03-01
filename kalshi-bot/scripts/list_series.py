import requests
import json

url = "https://api.elections.kalshi.com/trade-api/v2/series"
response = requests.get(url, params={"limit": 100})
series = response.json().get("series", [])
tickers = [s['ticker'] for s in series]
print(tickers)
