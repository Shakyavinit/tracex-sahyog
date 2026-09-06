"""
TraceX — Cryptographic Wallet Address Validation Engine
Complies with SIH26182 validation requirements:
- Validates BTC (P2PKH, P2SH, Bech32/Taproot)
- Validates EVM (Ethereum, BNB Chain, Polygon)
- Validates TRON (TRX / TRC-20)
- Validates Solana
- Strict format & character set verification
- Distinguishes multi-chain EVM ambiguity
"""
import re

BASE58_ALPHABET = set("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
HEX_ALPHABET = set("0123456789abcdefABCDEF")

# Regex patterns
BTC_P2PKH_PATTERN = re.compile(r"^1[1-9A-HJ-NP-Za-km-z]{25,34}$")
BTC_P2SH_PATTERN = re.compile(r"^3[1-9A-HJ-NP-Za-km-z]{25,34}$")
BTC_BECH32_PATTERN = re.compile(r"^(bc1q|bc1p)[02-9ac-hj-np-z]{38,58}$", re.IGNORECASE)

EVM_PATTERN = re.compile(r"^0x[0-9a-fA-F]{40}$")
TRON_PATTERN = re.compile(r"^T[1-9A-HJ-NP-Za-km-z]{33}$")
SOLANA_PATTERN = re.compile(r"^[1-9A-HJ-NP-Za-km-z]{32,44}$")


def validate_btc_address(addr: str) -> bool:
    """Validate Bitcoin address formats (Legacy P2PKH, P2SH, SegWit Bech32)."""
    if not addr or len(addr) < 26 or len(addr) > 62:
        return False
    if BTC_P2PKH_PATTERN.match(addr):
        return True
    if BTC_P2SH_PATTERN.match(addr):
        return True
    if BTC_BECH32_PATTERN.match(addr):
        return True
    return False


def validate_evm_address(addr: str) -> bool:
    """Validate Ethereum / EVM address format (0x + 40 hex chars)."""
    if not addr or len(addr) != 42:
        return False
    return bool(EVM_PATTERN.match(addr))


def validate_tron_address(addr: str) -> bool:
    """Validate TRON address format (T + 33 base58 chars)."""
    if not addr or len(addr) != 34:
        return False
    return bool(TRON_PATTERN.match(addr))


def validate_solana_address(addr: str) -> bool:
    """Validate Solana address format (32-44 base58 chars)."""
    if not addr or len(addr) < 32 or len(addr) > 44:
        return False
    # Avoid collisions with TRON or BTC addresses
    if addr.startswith("T") and len(addr) == 34:
        return False
    if (addr.startswith("1") or addr.startswith("3")) and len(addr) <= 35:
        return False
    return bool(SOLANA_PATTERN.match(addr))


def validate_and_classify_address(address: str, expected_chain: str | None = None) -> dict:
    """
    Validates a cryptocurrency wallet address and detects the blockchain network.
    Returns:
        {
            "is_valid": bool,
            "detected_chain": str | None,
            "chain_family": str | None,
            "error": str | None,
            "is_evm_ambiguous": bool,
            "supported_evm_chains": list
        }
    """
    addr = (address or "").strip()
    
    if not addr:
        return {
            "is_valid": False,
            "detected_chain": None,
            "chain_family": None,
            "error": "Wallet address cannot be empty.",
            "is_evm_ambiguous": False,
            "supported_evm_chains": []
        }

    # Blockchain-specific early rejection guidance
    if addr.startswith("0x"):
        if len(addr) != 42:
            return {
                "is_valid": False,
                "detected_chain": "EVM",
                "chain_family": "EVM",
                "error": f"Invalid EVM/Ethereum address: Expected exactly 42 characters ('0x' + 40 hex digits), but received {len(addr)} characters.",
                "is_evm_ambiguous": False,
                "supported_evm_chains": []
            }
    elif addr.startswith("T"):
        if len(addr) != 34:
            return {
                "is_valid": False,
                "detected_chain": "TRON",
                "chain_family": "TRON",
                "error": f"Invalid TRON address: Expected exactly 34 Base58 characters starting with 'T', but received {len(addr)} characters.",
                "is_evm_ambiguous": False,
                "supported_evm_chains": []
            }
    elif addr.startswith("1") or addr.startswith("3") or addr.startswith("bc1"):
        if len(addr) < 26 or len(addr) > 62:
            return {
                "is_valid": False,
                "detected_chain": "BTC",
                "chain_family": "UTXO",
                "error": f"Invalid Bitcoin address: Expected 26–62 characters (P2PKH, P2SH, or Bech32), but received {len(addr)} characters.",
                "is_evm_ambiguous": False,
                "supported_evm_chains": []
            }

    # Minimum sanity length check for other formats
    if len(addr) < 25 or len(addr) > 65:
        return {
            "is_valid": False,
            "detected_chain": None,
            "chain_family": None,
            "error": f"Invalid cryptocurrency address length ({len(addr)} characters). Valid formats: EVM (42 chars), TRON (34 chars), BTC (26-62 chars), Solana (32-44 chars).",
            "is_evm_ambiguous": False,
            "supported_evm_chains": []
        }

    detected_chain = None
    chain_family = None
    is_evm_ambiguous = False
    supported_evm = []

    # 1. EVM check (ETH, BNB, Polygon)
    if validate_evm_address(addr):
        chain_family = "EVM"
        is_evm_ambiguous = True
        supported_evm = ["ETH", "BNB", "POLYGON"]
        detected_chain = expected_chain.upper() if expected_chain and expected_chain.upper() in supported_evm else "ETH"
    # 2. Bitcoin check
    elif validate_btc_address(addr):
        chain_family = "UTXO"
        detected_chain = "BTC"
    # 3. TRON check
    elif validate_tron_address(addr):
        chain_family = "TRON"
        detected_chain = "TRON"
    # 4. Solana check
    elif validate_solana_address(addr):
        chain_family = "SOLANA"
        detected_chain = "SOL"
    else:
        return {
            "is_valid": False,
            "detected_chain": None,
            "chain_family": None,
            "error": "Invalid wallet address format. Does not match BTC, EVM (ETH/BNB/Polygon), TRON, or Solana cryptographic encoding rules.",
            "is_evm_ambiguous": False,
            "supported_evm_chains": []
        }

    # Chain mismatch check if expected_chain was provided
    if expected_chain and expected_chain.upper() not in ["AUTO", "ALL", ""]:
        exp = expected_chain.upper()
        if exp in ["ETH", "ETHEREUM", "BNB", "BSC", "POLYGON", "MATIC"]:
            if chain_family != "EVM":
                return {
                    "is_valid": False,
                    "detected_chain": detected_chain,
                    "chain_family": chain_family,
                    "error": f"Address format ({detected_chain}) does not match selected chain: {exp}. EVM addresses must start with 0x.",
                    "is_evm_ambiguous": False,
                    "supported_evm_chains": []
                }
            detected_chain = "BNB" if exp in ["BNB", "BSC"] else ("POLYGON" if exp in ["POLYGON", "MATIC"] else "ETH")
        elif exp in ["BTC", "BITCOIN"]:
            if detected_chain != "BTC":
                return {
                    "is_valid": False,
                    "detected_chain": detected_chain,
                    "chain_family": chain_family,
                    "error": f"Address format ({detected_chain}) does not match selected chain: BTC.",
                    "is_evm_ambiguous": False,
                    "supported_evm_chains": []
                }
        elif exp in ["TRON", "TRX", "USDT_TRC20"]:
            if detected_chain != "TRON":
                return {
                    "is_valid": False,
                    "detected_chain": detected_chain,
                    "chain_family": chain_family,
                    "error": f"Address format ({detected_chain}) does not match selected chain: TRON (must start with 'T').",
                    "is_evm_ambiguous": False,
                    "supported_evm_chains": []
                }
        elif exp in ["SOL", "SOLANA"]:
            if detected_chain != "SOL":
                return {
                    "is_valid": False,
                    "detected_chain": detected_chain,
                    "chain_family": chain_family,
                    "error": f"Address format ({detected_chain}) does not match selected chain: SOL.",
                    "is_evm_ambiguous": False,
                    "supported_evm_chains": []
                }

    return {
        "is_valid": True,
        "detected_chain": detected_chain,
        "chain_family": chain_family,
        "error": None,
        "is_evm_ambiguous": is_evm_ambiguous,
        "supported_evm_chains": supported_evm
    }
