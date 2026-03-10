import json
import os

PORTFOLIO_FILE = "kalshi-bot/data/paper_portfolio.json"

def settle_unemployment():
    # The official BLS February 2026 Unemployment Rate is 4.4%
    OFFICIAL_RATE = 4.4
    WINNING_TICKER = "KXU3-26FEB-T4.4"
    
    with open(PORTFOLIO_FILE, 'r') as f:
        data = json.load(f)
        
    positions = data["positions"]
    initial_balance = data["balance"]
    new_balance = initial_balance
    
    active_positions = []
    settled_profit = 0
    settled_loss = 0
    
    print(f"Official February Unemployment Rate: {OFFICIAL_RATE}%")
    print("Settling KXU3-26FEB contracts...\n")
    
    for p in positions:
        ticker = p["ticker"]
        
        # Only process February Unemployment contracts
        if "KXU3-26FEB" in ticker:
            cost = (p["entry_price"] / 100) * p["quantity"]
            
            # Logic: If it's the winning ticker AND side is YES -> payout $1 per share
            # If it's a losing ticker AND side is NO -> payout $1 per share
            payout = 0
            if ticker == WINNING_TICKER and p["side"] == "YES":
                payout = p["quantity"] * 1.00
                print(f"WON: {p['quantity']}x {ticker} (YES). Cost: ${cost:.2f} | Payout: +${payout:.2f}")
                
            elif ticker != WINNING_TICKER and p["side"] == "NO":
                payout = p["quantity"] * 1.00
                print(f"WON (Hedge): {p['quantity']}x {ticker} (NO). Cost: ${cost:.2f} | Payout: +${payout:.2f}")
                
            else:
                print(f"LOST: {p['quantity']}x {ticker} ({p['side']}). Cost: ${cost:.2f} | Payout: $0.00")
            
            new_balance += payout
            if payout > 0:
                settled_profit += (payout - cost)
            else:
                settled_loss += cost
                
            # Log to history
            data["history"].append({
                "ticker": ticker,
                "side": p["side"],
                "quantity": p["quantity"],
                "entry_price": p["entry_price"],
                "settled_at": "4.4%",
                "payout": payout,
                "profit_loss": payout - cost
            })
        else:
            # Keep non-unemployment contracts active (like GDP)
            active_positions.append(p)
            
    # Update portfolio state
    data["balance"] = new_balance
    data["positions"] = active_positions
    
    with open(PORTFOLIO_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        
    print("\n--- SETTLEMENT SUMMARY ---")
    print(f"Total Won (Net Profit): +${settled_profit:.2f}")
    print(f"Total Lost (Sunk Cost): -${settled_loss:.2f}")
    net_pnl = settled_profit - settled_loss
    print(f"Net Unemployment PnL: ${net_pnl:.2f}")
    print(f"\nOld Balance: ${initial_balance:.2f}")
    print(f"New Cash Balance: ${new_balance:.2f}")

if __name__ == "__main__":
    settle_unemployment()