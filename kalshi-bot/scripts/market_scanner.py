import requests
import time
import json
import os
from paper_trader import KalshiPaperTrader

class KalshiMarketScanner:
    def __init__(self):
        self.base_url = "https://api.elections.kalshi.com/trade-api/v2"
        self.trader = KalshiPaperTrader()
        self.last_probs = {}  # ticker: last_probability_cents
        self.target_series = ["KXECONSTAT", "RATECUT", "KXU3", "KXGDP", "KXPCECORE"]

    def get_active_markets(self):
        try:
            found_markets = []
            for series in self.target_series:
                response = requests.get(f"{self.base_url}/markets", params={"status": "open", "limit": 20, "series_ticker": series})
                if response.status_code == 200:
                    found_markets.extend(response.json().get("markets", []))
                else:
                    print(f"Error fetching series {series}: {response.status_code}")
            return found_markets
        except Exception as e:
            print(f"Scanner Exception: {e}")
            return []

    def run_scan(self):
        print(f"--- Scan Start: {time.ctime()} ---")
        markets = self.get_active_markets()
        
        # Save historical data to CSV
        with open("data/history.csv", "a") as f:
            for m in markets:
                ticker = m['ticker']
                current_prob = m.get('yes_bid', 0)
                timestamp = int(time.time())
                f.write(f"{timestamp},{ticker},{current_prob}\n")
                
                if ticker in self.last_probs:
                    last_prob = self.last_probs[ticker]
                    change = current_prob - last_prob
                    if abs(change) >= 5:
                        print(f"ALERT: {ticker} moved {change}% to {current_prob}%")
                        self.trader.log_trade(f"SCANNER DETECTED SPIKE: {ticker} ({change}%)")
                
                self.last_probs[ticker] = current_prob
                print(f"Market: {ticker} | Prob: {current_prob}%")

    def start_monitoring(self, interval_sec=600):
        print(f"Starting Kalshi Market Scanner (Interval: {interval_sec}s)...")
        while True:
            self.run_scan()
            time.sleep(interval_sec)

if __name__ == "__main__":
    scanner = KalshiMarketScanner()
    scanner.run_scan() # Single run for status check
