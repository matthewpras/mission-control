import requests
import json

url = "https://api.elections.kalshi.com/v2/markets"
response = requests.get(url)
print(f"Status Code: {response.status_code}")
try:
    print(json.dumps(response.json(), indent=2)[:500])
except:
    print(response.text)
