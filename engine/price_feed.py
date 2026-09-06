"""
Live Cryptocurrency Price Feed Module for TraceX / SIH26182.
Powered by CoinGecko API with dynamic caching and USD/INR conversions.
"""

import os
import time
import requests
from typing import Dict, Any

# In-memory cached rates with fallback defaults
_CACHED_RATES = {
    "BTC": {"usd": 81131.0, "inr": 7664859.0},
    "ETH": {"usd": 2525.2, "inr": 238568.0},
    "SOL": {"usd": 104.21, "inr": 9844.83},
    "TRON": {"usd": 0.328, "inr": 30.99},
    "USDT": {"usd": 1.0, "inr": 94.46},
    "BNB": {"usd": 580.0, "inr": 54800.0},
    "POLYGON": {"usd": 0.55, "inr": 52.0},
}
_LAST_FETCH_TIME = 0
CACHE_TTL = 300  # 5 minutes


def get_live_prices() -> Dict[str, Dict[str, float]]:
    """
    Fetch live crypto prices from CoinGecko.
    Uses COINGECKO_DEMO_API_KEY from environment.
    """
    global _CACHED_RATES, _LAST_FETCH_TIME
    now = time.time()
    
    # Return cache if within TTL
    if now - _LAST_FETCH_TIME < CACHE_TTL:
        return _CACHED_RATES

    api_key = os.getenv("COINGECKO_DEMO_API_KEY", "CG-waBsjQZ4qKCCq21TyijPNeJS")
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,tron,tether,binancecoin,matic-network&vs_currencies=usd,inr"
    headers = {
        "User-Agent": "TraceX-Forensic-Engine/2.0",
    }
    if api_key:
        headers["x-cg-demo-api-key"] = api_key

    try:
        resp = requests.get(url, headers=headers, timeout=6)
        if resp.status_code == 200:
            data = resp.json()
            if "bitcoin" in data:
                _CACHED_RATES["BTC"] = {"usd": data["bitcoin"].get("usd", 81000.0), "inr": data["bitcoin"].get("inr", 7600000.0)}
            if "ethereum" in data:
                _CACHED_RATES["ETH"] = {"usd": data["ethereum"].get("usd", 2500.0), "inr": data["ethereum"].get("inr", 235000.0)}
            if "solana" in data:
                _CACHED_RATES["SOL"] = {"usd": data["solana"].get("usd", 100.0), "inr": data["solana"].get("inr", 9500.0)}
            if "tron" in data:
                _CACHED_RATES["TRON"] = {"usd": data["tron"].get("usd", 0.32), "inr": data["tron"].get("inr", 30.0)}
            if "tether" in data:
                _CACHED_RATES["USDT"] = {"usd": data["tether"].get("usd", 1.0), "inr": data["tether"].get("inr", 94.0)}
            if "binancecoin" in data:
                _CACHED_RATES["BNB"] = {"usd": data["binancecoin"].get("usd", 580.0), "inr": data["binancecoin"].get("inr", 54800.0)}
            if "matic-network" in data:
                _CACHED_RATES["POLYGON"] = {"usd": data["matic-network"].get("usd", 0.55), "inr": data["matic-network"].get("inr", 52.0)}
            
            _LAST_FETCH_TIME = now
    except Exception:
        # Keep serving cached rates on network or rate limit failure
        pass

    return _CACHED_RATES


def convert_crypto_value(amount: float, chain: str) -> Dict[str, float]:
    """Convert a cryptocurrency amount to live USD and INR valuations."""
    rates = get_live_prices()
    c = chain.upper() if chain else "ETH"
    rate_info = rates.get(c, rates.get("ETH", {"usd": 2500.0, "inr": 235000.0}))
    usd = amount * rate_info["usd"]
    inr = amount * rate_info["inr"]
    return {
        "amount": amount,
        "chain": c,
        "usd_rate": rate_info["usd"],
        "inr_rate": rate_info["inr"],
        "usd_value": round(usd, 2),
        "inr_value": round(inr, 2),
    }
