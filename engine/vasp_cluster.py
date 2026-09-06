"""
VASP Cluster Database — Known Exchange Deposit Patterns & Hot Wallet Addresses
Used by the VASP Attribution Engine to identify nearest VASP in transaction graph.
"""

VASP_CLUSTERS = {
    # ─── INDIAN VASPs ───────────────────────────────────────────────────────────
    "WazirX": {
        "country": "India",
        "registration": "PMLA Registered - FIU-IND (Registration Ref: VDA-004)",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "TRON", "BNB"],
        "nodal_email": "compliance@wazirx.com",
        "nodal_officer": "Compliance Officer",
        "legal_address": "WazirX Trade Private Limited, Mumbai, Maharashtra, India",
        "hot_wallet_patterns": [],
        "deposit_address_heuristics": {"address_reuse": "high", "volume_usd_min": 10},
        "risk_level": "MEDIUM",
        "freeze_authority": "FIU-IND / PMLA Adjudicating Authority",
        "provenance": "FIU-IND Reporting Entity Registry",
        "last_verified": "2026-09-04",
    },
    "CoinDCX": {
        "country": "India",
        "registration": "PMLA Registered - FIU-IND",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "TRON", "BNB", "POLYGON"],
        "nodal_email": "legal@coindcx.com",
        "nodal_officer": "Chief Compliance Officer",
        "legal_address": "CoinDCX, Siechem Technologies Pvt Ltd, Mumbai, India",
        "hot_wallet_patterns": [],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 5},
        "risk_level": "MEDIUM",
        "freeze_authority": "FIU-IND / PMLA Adjudicating Authority",
    },
    "ZebPay": {
        "country": "India",
        "registration": "PMLA Registered - FIU-IND",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH"],
        "nodal_email": "compliance@zebpay.com",
        "nodal_officer": "Compliance Officer",
        "legal_address": "Awlencan Innovations India Pvt Ltd, Ahmedabad, India",
        "hot_wallet_patterns": [],
        "deposit_address_heuristics": {"address_reuse": "medium", "volume_usd_min": 1},
        "risk_level": "LOW",
        "freeze_authority": "FIU-IND / PMLA Adjudicating Authority",
    },
    "Mudrex": {
        "country": "India",
        "registration": "PMLA Registered - FIU-IND",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "BNB"],
        "nodal_email": "compliance@mudrex.com",
        "nodal_officer": "Compliance Officer",
        "legal_address": "Easyfi Network Private Limited, Bengaluru, India",
        "hot_wallet_patterns": [],
        "deposit_address_heuristics": {"address_reuse": "medium", "volume_usd_min": 5},
        "risk_level": "LOW",
        "freeze_authority": "FIU-IND / PMLA Adjudicating Authority",
    },
    "CoinSwitch": {
        "country": "India",
        "registration": "PMLA Registered - FIU-IND",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "TRON"],
        "nodal_email": "legal@coinswitch.co",
        "nodal_officer": "Chief Compliance Officer",
        "legal_address": "CoinSwitch Kuber, Bengaluru, India",
        "hot_wallet_patterns": [],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 1},
        "risk_level": "LOW",
        "freeze_authority": "FIU-IND / PMLA Adjudicating Authority",
    },

    # ─── GLOBAL VASPs ─────────────────────────────────────────────────────────
    "Binance": {
        "country": "International (Cayman Islands)",
        "registration": "FIU-IND (India), FINTRAC (Canada), BaFin (Germany)",
        "vasp_type": "Centralized Exchange (World's Largest)",
        "chains": ["BTC", "ETH", "TRON", "BNB", "POLYGON", "SOL"],
        "nodal_email": "law-enforcement@binance.com",
        "nodal_officer": "Law Enforcement Response Team",
        "legal_address": "Binance Holdings Ltd, Cayman Islands",
        "hot_wallet_patterns": [
            "0x28c6c06298d514db089934071355e5743bf21d60",  # Binance Hot Wallet 14 (ETH)
            "0xdfd5293d8e347dff59e4571400924b33ee2841b4",  # Binance Hot Wallet 16 (ETH)
            "0xbe0eb53f46cd790cd13851d5eff43d12404d33e8",  # Binance 7 (ETH)
            "0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be",
            "0xd551234ae421e3bcba99a0da6d736074f22192ff",
            "0x564286362092D8e7936f0549571a803B203aAceD",
            "1NDyJtNTjmwk5xPNhjgAMu4HDHigtobu1s",          # Binance BTC Hot
            "12cgpFdJViXbwHbhrA3TuW1EGnL25Zqc3P",          # Binance BTC Hot
            "34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo",          # Binance Cold Wallet BTC
            "TPYn4n8SkG9nnEtCdFnuJDWHubasRdbzxU",          # Binance Hot Wallet (TRON)
            "TMuA6YqfCeX8EhbfYEg5y7S4DqzSJireY9",          # Binance TRC20 Hot Wallet
        ],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 10},
        "risk_level": "LOW",
        "freeze_authority": "MLAT / INTERPOL NCB / FIU-IND Disclosure Request",
    },
    "Huobi/HTX": {
        "country": "International",
        "registration": "Multiple jurisdictions",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "TRON"],
        "nodal_email": "compliance@htx.com",
        "nodal_officer": "Compliance Officer",
        "legal_address": "HTX (Formerly Huobi), Seychelles",
        "hot_wallet_patterns": [
            "0xab5c66752a9e8167967685f1450532fb96d5d24f",
            "0x6748f50f686bfbca6fe8ad62b22228b87f31ff2b",
            "12vAqkTrNmR7r3UMQrtiNNHpRXCybFmQqb",
            "TFrzFkE9Fv6x72rJk6V84xY5V5kC7W19XN",          # HTX TRON Hot Wallet
        ],
        "deposit_address_heuristics": {"address_reuse": "medium", "volume_usd_min": 50},
        "risk_level": "MEDIUM",
        "freeze_authority": "MLAT / FIU-IND Disclosure Request",
    },
    "OKX": {
        "country": "International (Seychelles)",
        "registration": "Various jurisdictions",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "TRON", "BNB", "POLYGON", "SOL"],
        "nodal_email": "compliance@okx.com",
        "nodal_officer": "Compliance Department",
        "legal_address": "OKX, Victoria, Mahe, Seychelles",
        "hot_wallet_patterns": [
            "0x6cc5f688a315f3dc28a7781717a9a798a59fda7b",
        ],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 10},
        "risk_level": "LOW",
        "freeze_authority": "MLAT / FIU-IND Disclosure Request",
    },
    "KuCoin": {
        "country": "International (Seychelles)",
        "registration": "Various jurisdictions",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH", "TRON", "BNB"],
        "nodal_email": "support@kucoin.com",
        "nodal_officer": "Compliance Officer",
        "legal_address": "KuCoin, Seychelles",
        "hot_wallet_patterns": [
            "0x2b5634c42055806a59e9107ed44d43c426e58258",
        ],
        "deposit_address_heuristics": {"address_reuse": "medium", "volume_usd_min": 20},
        "risk_level": "MEDIUM",
        "freeze_authority": "MLAT / FIU-IND Disclosure Request",
    },
    "Bybit": {
        "country": "International (Dubai, UAE)",
        "registration": "VARA (Dubai), Various jurisdictions",
        "vasp_type": "Centralized Exchange / Derivatives",
        "chains": ["BTC", "ETH", "TRON", "BNB"],
        "nodal_email": "compliance@bybit.com",
        "nodal_officer": "Chief Compliance Officer",
        "legal_address": "Bybit Fintech Ltd, Dubai, UAE",
        "hot_wallet_patterns": [
            "0xf89d7b9c864f589bbf53a82105107622b35eaa40",
        ],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 50},
        "risk_level": "LOW",
        "freeze_authority": "MLAT / VARA Dubai / FIU-IND Disclosure Request",
    },
    "Kraken": {
        "country": "USA",
        "registration": "FinCEN, FCA (UK)",
        "vasp_type": "Centralized Exchange",
        "chains": ["BTC", "ETH"],
        "nodal_email": "law-enforcement@kraken.com",
        "nodal_officer": "Law Enforcement Response Team",
        "legal_address": "Payward Inc, San Francisco, California, USA",
        "hot_wallet_patterns": [
            "0x267be1c1d684f78cb4f6a176c4911b741e4ffdc0",
        ],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 50},
        "risk_level": "LOW",
        "freeze_authority": "MLAT / MLA Treaty with India-USA",
    },
    "Coinbase": {
        "country": "USA",
        "registration": "FinCEN, NYDFS BitLicense, FCA (UK)",
        "vasp_type": "Centralized Exchange (NASDAQ Listed)",
        "chains": ["BTC", "ETH", "POLYGON", "SOL"],
        "nodal_email": "law-enforcement@coinbase.com",
        "nodal_officer": "Law Enforcement Response Team",
        "legal_address": "Coinbase Global Inc, San Francisco, California, USA",
        "hot_wallet_patterns": [
            "0x71660c4005ba85c37ccec55d0c4493e66fe775d3",
        ],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 100},
        "risk_level": "LOW",
        "freeze_authority": "MLAT / MLA Treaty with India-USA",
    },

    # ─── HIGH-RISK / MIXER / DARKNET ──────────────────────────────────────────
    "Tornado Cash": {
        "country": "N/A (Decentralized Protocol - Sanctioned by OFAC)",
        "registration": "OFAC SDN Listed - Prohibited Entity",
        "vasp_type": "Crypto Mixer / Tumbler (Privacy Protocol)",
        "chains": ["ETH", "BNB", "POLYGON"],
        "nodal_email": "N/A (Decentralized)",
        "nodal_officer": "N/A",
        "legal_address": "Sanctioned - No Legal Address",
        "hot_wallet_patterns": [
            "0xd90e2f925da726b50c4ed8d0fb90ad053324f31b",
            "0x910cbd523d972eb0a6f4cae4618ad62622b39dbf",
            "0xa160cdab225685da1d56aa342ad8841c3b53f291",
        ],
        "deposit_address_heuristics": {"address_reuse": "very_low", "volume_usd_min": 100},
        "risk_level": "CRITICAL",
        "freeze_authority": "OFAC Sanctions / CBI / ED Attachment Order",
    },
    "ChipMixer": {
        "country": "N/A (Darknet - Seized by FBI/Europol in 2023)",
        "registration": "Criminal Enterprise - Seized",
        "vasp_type": "Bitcoin Mixer (Darknet)",
        "chains": ["BTC"],
        "nodal_email": "N/A",
        "nodal_officer": "N/A",
        "legal_address": "N/A",
        "hot_wallet_patterns": [
            "1CgpF1SQFxRKKXGHRBBwNR9FNXRg69sX4u",
        ],
        "deposit_address_heuristics": {"address_reuse": "low", "volume_usd_min": 100},
        "risk_level": "CRITICAL",
        "freeze_authority": "CBI / ED / MLAT",
    },
    "LocalBitcoins": {
        "country": "Finland",
        "registration": "FIN-FSA (Finland)",
        "vasp_type": "P2P Exchange (Ceased Operations 2023)",
        "chains": ["BTC"],
        "nodal_email": "N/A",
        "nodal_officer": "N/A",
        "legal_address": "LocalBitcoins Ltd, Helsinki, Finland",
        "hot_wallet_patterns": [],
        "deposit_address_heuristics": {"address_reuse": "high", "volume_usd_min": 1},
        "risk_level": "HIGH",
        "freeze_authority": "MLAT / FIN-FSA",
    },
}

# Known mixer/tumbler contract addresses (ETH)
MIXER_CONTRACTS = {
    "0xd90e2f925da726b50c4ed8d0fb90ad053324f31b": "Tornado Cash 0.1 ETH Pool",
    "0x9ad122c22b14202b4490edaf288fdb3c7cb3ff5e": "Tornado Cash 10 ETH Pool",
    "0x910cbd523d972eb0a6f4cae4618ad62622b39dbf": "Tornado Cash 100 ETH Pool",
    "0xa160cdab225685da1d56aa342ad8841c3b53f291": "Tornado Cash 1000 ETH Pool",
    "0x12D66f87A04A9E220C9D49f61E00a9278b0BFBA2": "Tornado Cash BNB Pool",
    "0x47ce0c6ed5b0ce3d3a51fdb1c52dc66a7c3c2936": "Tornado Cash USDC Pool",
}

# Known DeFi Bridges used in laundering
DEFI_BRIDGES = {
    # Across Protocol
    "0x5c7bcabeed66d30d10e5cb36757d54d80d23a1da": "Across Protocol SpokePool",
    "0x4d9079bb4165aeb4084c526a326959cfad2f7781": "Across Protocol HubPool",
    # Stargate / LayerZero
    "0xaf5191b0de27e6514942c6797ed96a9cf6babffa": "Stargate Router (LayerZero)",
    "0x8731d54e9d02c213766ea528bac7dd6004386a5b": "Stargate Router ETH Pool",
    # Synapse Bridge
    "0x2796317b0bf8529607744923bca0249764a77d11": "Synapse Bridge Router",
    # Hop Protocol
    "0xb8901acb9305435f9f0c3a15261ab4e54f64d1f2": "Hop Protocol Bridge",
    # Wormhole
    "0x98f3c9e6e3face36baad05fe09d375eff1764732": "Wormhole Core Bridge",
    # Legacy / Other Bridges
    "0x3014ca10b91cb3d0ad85fef7a3cb95bcac9c0f79": "AnySwap Multi-Chain Bridge",
    "0x1116898dda4015ed8ddefb84b6e8bc24528af2d8": "cBridge (Celer Network)",
    "0x40ec5b33f54e0e8a33a975908c5ba1c14e5bbbdf": "Polygon ERC20 Bridge",
    "thpvauhoh2qn2y9thczml3h815hhfhn5yc": "TRON Cross-Chain Bridge",
}

# Chain ID to Explorer mapping
CHAIN_EXPLORERS = {
    "BTC": {
        "name": "Bitcoin",
        "explorer_url": "https://blockchair.com/bitcoin/address/{address}",
        "api_url": "https://blockchain.info/rawaddr/{address}",
        "symbol": "₿",
    },
    "ETH": {
        "name": "Ethereum",
        "explorer_url": "https://etherscan.io/address/{address}",
        "api_url": "https://api.etherscan.io/api",
        "symbol": "Ξ",
    },
    "TRON": {
        "name": "TRON / TRC-20 (USDT)",
        "explorer_url": "https://tronscan.org/#/address/{address}",
        "api_url": "https://apilist.tronscanapi.com/api/accountv2",
        "symbol": "TRX",
    },
    "BNB": {
        "name": "BNB Smart Chain",
        "explorer_url": "https://bscscan.com/address/{address}",
        "api_url": "https://api.bscscan.com/api",
        "symbol": "BNB",
    },
    "POLYGON": {
        "name": "Polygon / MATIC",
        "explorer_url": "https://polygonscan.com/address/{address}",
        "api_url": "https://api.polygonscan.com/api",
        "symbol": "MATIC",
    },
    "SOL": {
        "name": "Solana",
        "explorer_url": "https://solscan.io/account/{address}",
        "api_url": "https://api.mainnet-beta.solana.com",
        "symbol": "SOL",
    },
}

def lookup_vasp_by_address(address: str) -> dict | None:
    """Check if a wallet address belongs to a known VASP cluster with exact matching."""
    raw_addr = (address or "").strip()
    addr_lower = raw_addr.lower()
    for vasp_name, vasp_info in VASP_CLUSTERS.items():
        for pattern in vasp_info.get("hot_wallet_patterns", []):
            p = pattern.strip()
            # EVM addresses are case-insensitive; BTC/TRON Base58 are case-sensitive
            if p.startswith("0x"):
                if p.lower() == addr_lower:
                    is_ind = vasp_info.get("country", "").strip().lower() == "india"
                    return {"vasp": vasp_name, "is_indian": is_ind, **vasp_info}
            else:
                if p == raw_addr or p.lower() == addr_lower:
                    is_ind = vasp_info.get("country", "").strip().lower() == "india"
                    return {"vasp": vasp_name, "is_indian": is_ind, **vasp_info}
    return None

def is_indian_vasp(vasp_name: str) -> bool:
    """Return True if VASP is an Indian registered reporting entity under FIU-IND."""
    info = VASP_CLUSTERS.get(vasp_name, {})
    return info.get("country", "").strip().lower() == "india"

def lookup_mixer(address: str) -> str | None:
    """Check if an address is a known mixer."""
    return MIXER_CONTRACTS.get(address.lower())

def lookup_bridge(address: str) -> str | None:
    """Check if an address is a known DeFi bridge."""
    return DEFI_BRIDGES.get(address.lower())

def get_all_vasps() -> dict:
    return VASP_CLUSTERS
