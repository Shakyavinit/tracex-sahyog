"""
TraceX — SIH26182 Synthetic Benchmark Cases
Complies with SIH26182 Demo Data Policy:
- Clearly marked as SYNTHETIC BENCHMARK DATA.
- Contains NO real complainant names, fake FIR numbers, or sensitive police records.
- Standardized case identifiers: DEMO-SIH26182-001 to DEMO-SIH26182-004.
"""

DEMO_CASES = [
    {
        "case_id": "DEMO-SIH26182-001",
        "title": "TRON Multi-Hop Layering Benchmark (USDT TRC-20)",
        "crime_category": "Synthetic Fraud / Layering Dispersion",
        "mode": "SYNTHETIC_DEMO",
        "disclaimer": "SYNTHETIC RESEARCH BENCHMARK — FOR SIH26182 EVALUATION ONLY",
        "description": (
            "Synthetic simulation of fund movement across 3 intermediate mule wallets "
            "on TRON network before reaching centralized exchange deposit address. "
            "Designed to evaluate multi-hop path reconstruction and latency."
        ),
        "suspect_address": "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t",
        "chain": "TRON",
        "amount_lost_inr": 480000,
        "amount_crypto": 5780,
        "asset": "USDT",
        "tags": ["Benchmark", "TRON", "USDT", "Multi-Hop", "Synthetic"],
    },
    {
        "case_id": "DEMO-SIH26182-002",
        "title": "Bitcoin Multi-Hop Peel Chain Benchmark (BTC UTXO)",
        "crime_category": "Synthetic Ransomware / Peel Chain",
        "mode": "SYNTHETIC_DEMO",
        "disclaimer": "SYNTHETIC RESEARCH BENCHMARK — FOR SIH26182 EVALUATION ONLY",
        "description": (
            "Synthetic benchmark modeling a 4-hop Bitcoin peel chain where small fractions "
            "peel off to unhosted change outputs while main volume routes to a regulated VASP. "
            "Evaluates UTXO traversal and rapid cashout typology detection."
        ),
        "suspect_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
        "chain": "BTC",
        "amount_lost_inr": 3500000,
        "amount_crypto": 0.52,
        "asset": "BTC",
        "tags": ["Benchmark", "Bitcoin", "BTC", "Peel Chain", "Synthetic"],
    },
    {
        "case_id": "DEMO-SIH26182-003",
        "title": "Ethereum Privacy Pool Interaction Benchmark (Tornado Cash Break)",
        "crime_category": "Synthetic Mixer Laundering",
        "mode": "SYNTHETIC_DEMO",
        "disclaimer": "SYNTHETIC RESEARCH BENCHMARK — FOR SIH26182 EVALUATION ONLY",
        "description": (
            "Synthetic test case modeling fund traversal into an OFAC-sanctioned Tornado Cash mixer pool. "
            "TraceX identifies the mixer break, lowers confidence, and flags compliance alerts."
        ),
        "suspect_address": "0x12D66f87A04A9E220743712cE6d9bB1B5616B8Fc",
        "chain": "ETH",
        "amount_lost_inr": 820000,
        "amount_crypto": 3.8,
        "asset": "ETH",
        "tags": ["Benchmark", "Ethereum", "Mixer", "Tornado Cash", "Synthetic"],
    },
    {
        "case_id": "DEMO-SIH26182-004",
        "title": "Direct Exchange Hot Wallet Verification Benchmark (Hop-0 Binance)",
        "crime_category": "Public Exchange Infrastructure Verification",
        "mode": "SYNTHETIC_DEMO",
        "disclaimer": "PUBLIC LABEL VERIFICATION BENCHMARK — FOR SIH26182 EVALUATION ONLY",
        "description": (
            "Public benchmark using verified Binance Hot Wallet 14 (0x3f5ce5...). "
            "Evaluates Hop-0 instant VASP recognition: TraceX must identify it directly at Hop 0 "
            "without generating fictitious intermediary hops."
        ),
        "suspect_address": "0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be",
        "chain": "ETH",
        "amount_lost_inr": 2500000,
        "amount_crypto": 11.4,
        "asset": "ETH",
        "tags": ["Benchmark", "Hop 0", "Direct VASP", "Binance", "Public Label"],
    },
]

def get_demo_cases() -> list:
    return DEMO_CASES

def get_case_by_id(case_id: str) -> dict | None:
    for case in DEMO_CASES:
        if case["case_id"] == case_id:
            return case
    return None
