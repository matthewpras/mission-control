import json
import time
import datetime

class KalshiPaperTrader:
    def __init__(self):
        self.portfolio_file = "data/paper_portfolio.json"
        self.trade_log = "logs/trades.log"
        self.initialize_portfolio()

    def initialize_portfolio(self):
        try:
            with open(self.portfolio_file, 'r') as f:
                self.portfolio = json.load(f)
        except FileNotFoundError:
            self.portfolio = {
                "balance": 1000.00,  # Starting with $1000 paper money
                "positions": [],
                "history": []
            }
            self.save_portfolio()

    def save_portfolio(self):
        with open(self.portfolio_file, 'w') as f:
            json.dump(self.portfolio, f, indent=4)

    def log_trade(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.trade_log, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")

    def simulate_trade(self, ticker, price_cents, quantity, side="YES"):
        cost = (price_cents / 100) * quantity
        if self.portfolio["balance"] >= cost:
            self.portfolio["balance"] -= cost
            position = {
                "ticker": ticker,
                "entry_price": price_cents,
                "quantity": quantity,
                "side": side,
                "timestamp": time.time()
            }
            self.portfolio["positions"].append(position)
            self.save_portfolio()
            self.log_trade(f"BOUGHT {quantity} {ticker} @ {price_cents}c | Balance: ${self.portfolio['balance']:.2f}")
            return True
        return False

if __name__ == "__main__":
    trader = KalshiPaperTrader()
    print("Kalshi Paper Trader Initialized.")
    # Example simulation
    # trader.simulate_trade("FED-26MAR-T525", 65, 10)
