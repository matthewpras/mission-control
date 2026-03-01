import requests
import json

url = "https://trading-api.kalshi.com/v2/markets"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
print(f"Status Code: {response.status_code}")
try:
    print(json.dumps(response.json(), indent=2)[:500])
except:
    print(response.text)
