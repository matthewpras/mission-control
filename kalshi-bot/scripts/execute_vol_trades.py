import sys
import os
import time

sys.path.append(os.path.dirname(__file__))
from paper_trader import KalshiPaperTrader

def vol_research_and_trade():
    print("Conducting high-volatility market research...")
    trader = KalshiPaperTrader()
    
    # High-volatility targets based on previous top markets scan (Sports, Crypto, Entertainment)
    # Using dummy/recent tickers from the KXMVECROSSCATEGORY and Oscars
    targets = [
        {"ticker": "KXMVECROSSCATEGORY-S202676AF3A320DF-B623DF371B7", "price": 15, "qty": 20}, # NBA Player Props
        {"ticker": "KXMVEOSCARS-S20262B701784206-E6D68B2D8A4", "price": 25, "qty": 10}, # Oscars
        {"ticker": "KXMVECROSSCATEGORY-S202610A71E40B91-7A9D50A40A4", "price": 16, "qty": 20}, # Premier League
        {"ticker": "KXMVECROSSCATEGORY-S2026C5F9771720A-DA0657581E6", "price": 10, "qty": 30} # NBA Parlay
    ]
    
    for t in targets:
        print(f"Executing high-vol trade: {t['ticker']}...")
        trader.simulate_trade(t['ticker'], t['price'], t['qty'], side="YES")
        time.sleep(1)
        
    print("Vol trades completed.")

if __name__ == "__main__":
    vol_research_and_trade()