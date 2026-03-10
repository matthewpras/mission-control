import json

def calculate_projection():
    with open("kalshi-bot/data/paper_portfolio.json", "r") as f:
        data = json.load(f)
        
    positions = data["positions"]
    balance = data["balance"]
    
    # Calculate total capital deployed
    deployed = 1000.0 - balance
    
    # Group by ticker
    tickers = {}
    for p in positions:
        t = p["ticker"]
        if t not in tickers:
            tickers[t] = {"YES": 0, "NO": 0, "cost_YES": 0, "cost_NO": 0}
        
        cost = (p["entry_price"] / 100) * p["quantity"]
        if p["side"] == "YES":
            tickers[t]["YES"] += p["quantity"]
            tickers[t]["cost_YES"] += cost
        else:
            tickers[t]["NO"] += p["quantity"]
            tickers[t]["cost_NO"] += cost
            
    print(f"Current Cash Balance: ${balance:.2f}")
    print(f"Capital Deployed: ${deployed:.2f}")
    print("\n--- Position Breakdown ---")
    
    max_payout = 0
    # For a given economic stat (e.g. unemployment rate), only one Ticker can be YES.
    # Actually, it's easier: for each ticker, what is the payout if YES wins vs if NO wins?
    for t, data in tickers.items():
        # If YES wins, payout is $1 * YES quantity
        payout_yes = data["YES"] * 1.00
        # If NO wins, payout is $1 * NO quantity
        payout_no = data["NO"] * 1.00
        
        print(f"\n{t}:")
        print(f"  YES Position: {data['YES']} shares (Cost: ${data['cost_YES']:.2f}) -> Payout if YES: ${payout_yes:.2f}")
        print(f"  NO Position:  {data['NO']} shares (Cost: ${data['cost_NO']:.2f}) -> Payout if NO: ${payout_no:.2f}")

calculate_projection()