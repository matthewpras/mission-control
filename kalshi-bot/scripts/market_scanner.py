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
        self.target_series = ["KXECONSTAT", "RATECUT", "KXU3", "KXGDP", "KXPCECORE", "BTC"]

    def get_active_markets(self):
        try:
            found_markets = []
            for series in self.target_series:
                params = {"status": "open", "limit": 10, "series_ticker": series}
                # Sort BTC by high volume to find active strikes
                if series == "BTC":
                    params["sort"] = "volume_24h:desc"
                
                response = requests.get(f"{self.base_url}/markets", params=params)
                if response.status_code == 200:
                    found_markets.extend(response.json().get("markets", []))
            return found_markets
        except Exception as e:
            print(f"Scanner Exception: {e}")
            return []

    def run_scan(self):
        print(f"--- Scan Start: {time.ctime()} ---")
        try:
            markets = self.get_active_markets()
            
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            history_file = os.path.join(base_dir, "data", "history.csv")
            
            # Ensure data dir exists
            os.makedirs(os.path.join(base_dir, "data"), exist_ok=True)

            with open(history_file, "a") as f:
                for m in markets:
                    ticker = m['ticker']
                    current_prob = m.get('yes_bid', 0)
                    timestamp = int(time.time())
                    f.write(f"{timestamp},{ticker},{current_prob}\n")
                    
                    if ticker in self.last_probs:
                        last_prob = self.last_probs[ticker]
                        change = current_prob - last_prob
                        
                        # Thresholds: 5% for Econ, 2% for BTC (higher volatility)
                        threshold = 2 if "BTC" in ticker else 5
                        
                        if abs(change) >= threshold:
                            print(f"ALERT: {ticker} moved {change}% to {current_prob}%")
                            self.trader.log_trade(f"SCANNER DETECTED SPIKE: {ticker} ({change}%)")
                            
                            # EXECUTE TRADE: Side depends on spike direction (Mean Reversion)
                            # If it spiked UP, we bet NO. If it crashed DOWN, we bet YES.
                            side = "NO" if change > 0 else "YES"
                            # Trade 5% of balance per trade
                            quantity = int((self.trader.portfolio["balance"] * 0.05) / (current_prob / 100 or 0.01))
                            if quantity > 0:
                                self.trader.simulate_trade(ticker, current_prob, quantity, side=side)
                    
                    self.last_probs[ticker] = current_prob
        except Exception as e:
            print(f"Loop Exception: {e}")

    def start_monitoring(self, interval_sec=300): # 5 minute interval for BTC
        print(f"Starting Kalshi Market Scanner (Interval: {interval_sec}s)...")
        # Initial Heartbeat
        self.trader.notify_telegram("📡 **Kalshi Bot Online**\nMonitoring Econ Stats + BTC Strike Prices. Real-time alerts enabled.")
        while True:
            try:
                self.run_scan()
            except:
                pass
            time.sleep(interval_sec)

if __name__ == "__main__":
    scanner = KalshiMarketScanner()
    scanner.start_monitoring(interval_sec=300) # 5-minute resolution for real trading
