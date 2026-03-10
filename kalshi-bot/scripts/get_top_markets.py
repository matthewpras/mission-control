import requests
import json

url = "https://api.elections.kalshi.com/trade-api/v2/markets"
params = {
    "status": "open",
    "limit": 20,
    "sort": "volume_24h:desc"
}
response = requests.get(url, params=params)
if response.status_code == 200:
    markets = response.json().get("markets", [])
    for m in markets:
        try:
            title = m['title'].encode('ascii', 'ignore').decode('ascii')
            print(f"Ticker: {m['ticker']} | Title: {title} | Vol24h: {m.get('volume_24h', 0)} | Yes: {m['yes_bid']}c / No: {m['no_bid']}c")
        except:
            continue
else:
    print(f"Error: {response.status_code}")
