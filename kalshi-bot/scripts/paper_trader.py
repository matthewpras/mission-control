import json
import time
import datetime
import os

class KalshiPaperTrader:
    def __init__(self):
        # Set paths relative to this script's directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.portfolio_file = os.path.join(base_dir, "data", "paper_portfolio.json")
        self.trade_log = os.path.join(base_dir, "logs", "trades.log")
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

    def notify_telegram(self, message):
        import subprocess
        try:
            cmd = [
                "openclaw", "message", "send",
                "--channel", "telegram",
                "--target", "-1003882600560",
                "--thread-id", "167",
                "--message", message
            ]
            subprocess.run(cmd, check=True, shell=True)
        except Exception as e:
            print(f"Telegram notification failed: {e}")

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
            log_msg = f"BOUGHT {quantity} {ticker} @ {price_cents}c | Balance: ${self.portfolio['balance']:.2f}"
            self.log_trade(log_msg)
            
            # Send real-time notification
            self.notify_telegram(f"🚀 **KALSHI TRADE EXECUTED**\n\n**Action:** {side} {quantity} shares\n**Market:** {ticker}\n**Price:** {price_cents}c\n**Remaining Balance:** ${self.portfolio['balance']:.2f}")
            
            return True
        return False

if __name__ == "__main__":
    trader = KalshiPaperTrader()
    print("Kalshi Paper Trader Initialized.")
    # Example simulation
    # trader.simulate_trade("FED-26MAR-T525", 65, 10)
