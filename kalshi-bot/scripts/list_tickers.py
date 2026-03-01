import requests
import json

url = "https://api.elections.kalshi.com/trade-api/v2/markets"
response = requests.get(url, params={"status": "open", "limit": 100})
markets = response.json().get("markets", [])
tickers = [m['ticker'] for m in markets]
print(tickers)
