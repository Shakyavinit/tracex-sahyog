"""
TraceX API Key Manager Module
Handles direct saving, reloading, and live validation of API keys from the Dashboard UI.
"""

import os
import requests
from typing import Dict, Any

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")


def get_all_configured_keys() -> Dict[str, Any]:
    """Read all API keys currently configured in .env and environment."""
    keys = {
        "ETHERSCAN_API_KEY": os.getenv("ETHERSCAN_API_KEY", ""),
        "TRONGRID_API_KEY": os.getenv("TRONGRID_API_KEY", ""),
        "BITQUERY_ACCESS_TOKEN": os.getenv("BITQUERY_ACCESS_TOKEN", ""),
        "COINGECKO_DEMO_API_KEY": os.getenv("COINGECKO_DEMO_API_KEY", ""),
        "CHAINABUSE_API_KEY": os.getenv("CHAINABUSE_API_KEY", ""),
    }

    # Also check .env directly
    if os.path.exists(ENV_PATH):
        try:
            with open(ENV_PATH, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip()
                        if "KEY" in k or "TOKEN" in k:
                            keys[k] = v
        except Exception:
            pass

    # Build response with preview masking
    result = {}
    for k, v in keys.items():
        val = v.strip()
        masked = ""
        if val:
            if len(val) > 10:
                masked = f"{val[:6]}...{val[-4:]}"
            else:
                masked = f"{val[:2]}***"
        result[k] = {
            "key_name": k,
            "raw_value": val,
            "masked_value": masked,
            "is_set": bool(val),
        }
    return result


def update_api_key(key_name: str, key_value: str) -> Dict[str, Any]:
    """Save/update an API key in .env and runtime os.environ."""
    key_name = key_name.strip().upper()
    key_value = key_value.strip()

    # Update runtime environment immediately
    os.environ[key_name] = key_value

    # Update .env file
    lines = []
    found = False
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, "r") as f:
            lines = f.readlines()

    new_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            k, _ = stripped.split("=", 1)
            if k.strip().upper() == key_name:
                new_lines.append(f"{key_name}={key_value}\n")
                found = True
                continue
        new_lines.append(line)

    if not found:
        new_lines.append(f"{key_name}={key_value}\n")

    with open(ENV_PATH, "w") as f:
        f.writelines(new_lines)

    return {
        "status": "SAVED",
        "key_name": key_name,
        "is_set": bool(key_value),
        "message": f"{key_name} successfully saved & activated in runtime environment!",
    }


def validate_key(key_name: str, key_value: str) -> Dict[str, Any]:
    """Perform a live verification test on an entered API key."""
    k = key_name.strip().upper()
    v = key_value.strip()

    if not v:
        return {"valid": False, "provider": k, "message": "Key cannot be empty."}

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) TraceX-Key-Validator/2.0"}

    try:
        if "ETHERSCAN" in k:
            url = f"https://api.etherscan.io/v2/api?chainid=1&module=account&action=balance&address=0x28C6c06298d514Db089934071355E5743bf21d60&tag=latest&apikey={v}"
            resp = requests.get(url, headers=headers, timeout=6)
            data = resp.json()
            if data.get("status") == "1":
                return {"valid": True, "provider": "Etherscan V2", "message": "Key verified! Connected to Ethereum Mainnet."}
            err = data.get("result", "Invalid key response")
            return {"valid": False, "provider": "Etherscan V2", "message": f"Etherscan rejected key: {err}"}

        elif "TRONGRID" in k:
            url = "https://api.trongrid.io/v1/accounts/T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb"
            resp = requests.get(url, headers={**headers, "TRON-PRO-API-KEY": v}, timeout=6)
            if resp.status_code == 200:
                return {"valid": True, "provider": "TronGrid Pro", "message": "Key verified! Connected to TRON Mainnet."}
            return {"valid": False, "provider": "TronGrid Pro", "message": f"TronGrid returned HTTP {resp.status_code}"}

        elif "BITQUERY" in k:
            url = "https://streaming.bitquery.io/graphql"
            query = "query { EVM(dataset: realtime, network: eth) { Blocks(limit: {count: 1}) { Block { Number } } } }"
            resp = requests.post(url, json={"query": query}, headers={**headers, "Authorization": f"Bearer {v}"}, timeout=6)
            if resp.status_code == 200:
                data = resp.json()
                if "errors" not in data:
                    return {"valid": True, "provider": "Bitquery V2", "message": "Token verified! Connected to Bitquery GraphQL stream."}
                return {"valid": False, "provider": "Bitquery V2", "message": data["errors"][0].get("message", "Token error")}
            return {"valid": False, "provider": "Bitquery V2", "message": f"Bitquery returned HTTP {resp.status_code}"}

        elif "COINGECKO" in k:
            url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
            resp = requests.get(url, headers={**headers, "x-cg-demo-api-key": v}, timeout=6)
            if resp.status_code == 200:
                return {"valid": True, "provider": "CoinGecko", "message": "Key verified! Connected to CoinGecko Spot Feed."}
            return {"valid": False, "provider": "CoinGecko", "message": f"CoinGecko returned HTTP {resp.status_code}"}

        else:
            # Generic key saved
            return {"valid": True, "provider": k, "message": f"{k} saved. Configured for custom usage."}

    except Exception as e:
        return {"valid": False, "provider": k, "message": f"Validation test error: {str(e)}"}
