import os
import json
import base64
import time
from datetime import datetime
from dotenv import load_dotenv
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import requests

# Load environment variables
load_dotenv()

# --- Configuration ---
# Default to demo, but allow override
ENV_TYPE = os.getenv("KALSHI_API_ENV", "demo")
BASE_URL = "https://demo-api.kalshi.co/trade-api/v2"

if ENV_TYPE == "prod":
    BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

def load_private_key(path):
    """Loads the RSA private key from the specified path."""
    print(f"[*] Loading private key from: {path}")
    try:
        with open(path, "rb") as key_file:
            return serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
    except FileNotFoundError:
        print(f"[!] Private key file not found at {path}")
        return None
    except Exception as e:
        print(f"[!] Error loading private key: {e}")
        return None

def sign_request(private_key, method, path, timestamp):
    """Generates the RSA-SHA256 signature for Kalshi V2 auth."""
    # The message to sign is: timestamp + method + path (e.g., "1678888888000GET/trade-api/v2/exchange/status")
    # Note: path MUST include the full path from the host, e.g., /trade-api/v2/portfolio/balance
    
    msg = f"{timestamp}{method}{path}".encode('utf-8')
    
    signature = private_key.sign(
        msg,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.DIGEST_LENGTH
        ),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

def get_headers(method, endpoint):
    """Constructs the headers for an authenticated request."""
    key_id = os.getenv("KALSHI_KEY_ID")
    key_path = os.getenv("KALSHI_PRIVATE_KEY_PATH")
    
    if not key_id or not key_path:
        print("[!] Missing credentials in .env")
        return None

    private_key = load_private_key(key_path)
    if not private_key:
        return None
    
    timestamp = str(int(time.time() * 1000)) # Milliseconds
    
    # Strip query parameters from endpoint before using it for signing
    clean_endpoint = endpoint.split('?')[0]
    
    # Path for signing: The API documentation specifies using the path component of the URL.
    # For V2, all endpoints start with /trade-api/v2
    sign_path = f"/trade-api/v2{clean_endpoint}"
    
    signature = sign_request(private_key, method, sign_path, timestamp)
    
    return {
        "KALSHI-ACCESS-KEY": key_id,
        "KALSHI-ACCESS-SIGNATURE": signature,
        "KALSHI-ACCESS-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }

def authenticated_request(method, endpoint, params=None, payload=None):
    """Performs an authenticated request to Kalshi."""
    url = f"{BASE_URL}{endpoint}"
    headers = get_headers(method, endpoint)
    
    if not headers:
        return None
    
    print(f"[*] Requesting {method} {url}...")
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
             print(f"[!] 401 Unauthorized. Check Key ID and Private Key signature.")
             print(f"Response: {response.text}")
             return None
        else:
            print(f"[!] API Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"[!] Request failed: {e}")
        return None

def place_order(ticker, client_order_id, count, price, side, type="limit", action="buy"):
    """Places an order on Kalshi. price is in USD cents."""
    endpoint = "/orders"
    payload = {
        "ticker": ticker,
        "client_order_id": client_order_id,
        "count": count, # number of contracts
        "action": action, # "buy" or "sell"
        "type": type, # "limit" or "market"
        "side": side, # "yes" or "no"
    }

    # Limit orders require a price
    if type == "limit":
        if side == "yes":
            payload["yes_price"] = price
        elif side == "no":
            payload["no_price"] = price
    
    print(f"\n[*] PROPOSING ORDER: {json.dumps(payload, indent=2)}")
    # Important: For now, we will do a dry run or manual confirmation.
    # For actual execution, uncomment the line below:
    # return authenticated_request("POST", endpoint, payload=payload)
    return None # Return None for now, to prevent accidental trades.

def main():
    print("--- OPERATION ORACLE: PAPER TRADER V0.4 ---") # Version bump
    print(f"[*] Environment: {ENV_TYPE}")
    
    # 1. Get Account Balance (Verifies Auth)
    print("\n[*] Fetching Account Balance...")
    balance = authenticated_request("GET", "/portfolio/balance")
    
    if balance:
        print(f"Balance: {json.dumps(balance, indent=2)}")
    else:
        print("Failed to fetch balance.")

    # 2. Check Orders (Another Authenticated Endpoint)
    print("\n[*] Fetching Orders...")
    orders = authenticated_request("GET", "/portfolio/orders")
    if orders:
        print(f"Orders: {json.dumps(orders, indent=2)}")
    else:
        print("Failed to fetch orders.")

    # 3. Check Exchange Status (Authenticated Endpoint)
    print("\n[*] Checking Exchange Status (authenticated)...")
    exchange_status = authenticated_request("GET", "/exchange/status")
    if exchange_status:
        print(f"Exchange Status: {json.dumps(exchange_status, indent=2)}")
    else:
        print("Failed to fetch authenticated exchange status.")

    # 4. List some markets (Example)
    print("\n[*] Fetching Active Markets (Limit 3)...")
    markets = authenticated_request("GET", "/markets", params={"status": "open", "limit": 5})
    first_market_ticker = None
    if markets and markets.get('markets'):
        print(f"Markets found: {len(markets.get('markets', []))}")
        for m in markets.get('markets', []):
            print(f" - {m.get('ticker')}: {m.get('title')}")
            if not first_market_ticker:
                first_market_ticker = m.get('ticker')

        if first_market_ticker:
            print(f"\n[*] Fetching details for first open market ({first_market_ticker})...")
            market_details = authenticated_request("GET", f"/markets/{first_market_ticker}")
            if market_details:
                print(f"Market Details: {json.dumps(market_details, indent=2)}")
            else:
                print(f"Failed to fetch details for market {first_market_ticker}.")
    else:
        print("No open markets found or failed to fetch markets.")

    # 5. Test Trade (Dry Run)
    if first_market_ticker:
        print(f"\n[*] Attempting a test trade on {first_market_ticker} (Dry Run)...")
        # Example: Buy 1 'yes' contract for 10 cents (0.10 USD)
        # client_order_id needs to be unique per order
        test_order_id = f"test-order-{int(time.time())}"
        trade_result = place_order(
            ticker=first_market_ticker,
            client_order_id=test_order_id,
            count=1,
            price=10, # 10 cents
            side="yes",
            type="limit"
        )
        if trade_result:
            print(f"Test Trade Result: {json.dumps(trade_result, indent=2)}")
        else:
            print("Test trade was a dry run (no actual order placed).")
    else:
        print("Skipping test trade as no open markets were found.")

if __name__ == "__main__":
    main()