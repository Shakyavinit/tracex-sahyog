"""
Money Laundering Typology Detector
Detects patterns like Peel Chains, Rapid Cashouts, Mixer Funneling,
Cross-chain bridges, and other laundering techniques used in VDA crimes.
"""

from typing import Any


# Typology definitions used in investigation reports
TYPOLOGY_DEFINITIONS = {
    "peel_chain": {
        "name": "Peel Chain",
        "ioc": "IOC-001",
        "description": (
            "A sequence of transactions where each successive wallet receives a slightly "
            "smaller amount than the previous one, 'peeling off' small amounts to intermediary "
            "wallets to obscure the trail. Commonly used in ransomware proceeds laundering."
        ),
        "risk_score_contribution": 20,
        "references": "FATF Guidance on Virtual Assets (2019), Chainalysis Crypto Crime Report 2024",
    },
    "mixer_interaction": {
        "name": "Mixer / Tumbler Interaction",
        "ioc": "IOC-002",
        "description": (
            "Funds passed through a mixing or tumbling service such as Tornado Cash, ChipMixer, "
            "or CoinJoin to break the on-chain link between source and destination wallets. "
            "Interaction with OFAC-sanctioned mixers constitutes a separate legal violation."
        ),
        "risk_score_contribution": 40,
        "references": "OFAC SDN List, FATF Recommendation 16",
    },
    "rapid_cashout": {
        "name": "Rapid Cashout",
        "ioc": "IOC-003",
        "description": (
            "Funds are received and immediately (within minutes to hours) transferred onward "
            "to an exchange, reducing the window for LEA intervention. Classic pattern in "
            "investment scam and cyber fraud proceeds."
        ),
        "risk_score_contribution": 25,
        "references": "FIU-IND AML Guidance Note 2023",
    },
    "layering_dispersion": {
        "name": "Layering / Fan-Out Dispersion",
        "ioc": "IOC-004",
        "description": (
            "A single wallet receives funds and then distributes them across a large number "
            "of wallets (10+) in small equal amounts to obscure the aggregated crime proceeds. "
            "Common in darknet marketplace withdrawals and mule network operations."
        ),
        "risk_score_contribution": 30,
        "references": "FATF Guidance on VDA, Europol IOCTA 2023",
    },
    "cross_chain_bridge": {
        "name": "Cross-Chain Bridge (Chain-Hopping)",
        "ioc": "IOC-005",
        "description": (
            "Funds are converted from one blockchain to another (e.g., BTC -> ETH -> TRON) "
            "using bridge protocols to exploit gaps in cross-chain monitoring. A common "
            "technique used in ransomware and darknet drug market laundering."
        ),
        "risk_score_contribution": 25,
        "references": "FATF Report on DeFi 2023, Chainalysis Bridge Tracking Report",
    },
    "defi_protocol_funneling": {
        "name": "DeFi Protocol Funneling",
        "ioc": "IOC-006",
        "description": (
            "Funds routed through Decentralized Finance protocols (DEXs, lending platforms, "
            "liquidity pools) to obscure provenance. Difficult to trace as many DeFi protocols "
            "are non-custodial and do not maintain KYC records."
        ),
        "risk_score_contribution": 20,
        "references": "FATF Report on DeFi Oct 2021",
    },
    "smurfing": {
        "name": "Smurfing (Structuring)",
        "ioc": "IOC-007",
        "description": (
            "Large crime proceeds are broken into many small sub-threshold transactions to avoid "
            "triggering automated monitoring systems. Each individual transaction appears benign "
            "but collectively represent significant criminal funds."
        ),
        "risk_score_contribution": 30,
        "references": "PMLA Section 3, FATF Recommendation 20",
    },
    "unhosted_wallet_concentration": {
        "name": "Unhosted Wallet Concentration",
        "ioc": "IOC-008",
        "description": (
            "Funds consolidated into an unhosted (self-custodial) wallet not associated with "
            "any regulated VASP, making attribution and asset freezing extremely difficult. "
            "This is the critical gap the SAHYOG-VASP Attribution Engine addresses."
        ),
        "risk_score_contribution": 15,
        "references": "MAS Notice PSN02, FIU-IND Guidance on Unhosted Wallets 2024",
    },
}


def analyze_typologies(graph_data: dict) -> dict:
    """
    Analyze a traced transaction graph and detect laundering typologies.
    Returns detected typologies and a composite risk score.
    """
    nodes = graph_data.get("nodes", [])
    edges = graph_data.get("edges", [])
    metadata = graph_data.get("metadata", {})

    detected = []
    base_score = metadata.get("base_risk_score", 10)
    total_score = base_score

    hop_count = metadata.get("hop_count", 0)
    has_mixer = metadata.get("has_mixer", False)
    has_bridge = metadata.get("has_bridge", False)
    rapid_transfer = metadata.get("rapid_transfer", False)
    output_count = metadata.get("output_wallets_count", 1)
    amount_variance = metadata.get("amount_variance_pct", 0)
    chain_hops = metadata.get("chain_hops", 1)

    # ── Peel Chain Detection ─────────────────────────────────────────────────
    if hop_count >= 3 and amount_variance > 0 and amount_variance < 15:
        detected.append({
            "typology": "peel_chain",
            **TYPOLOGY_DEFINITIONS["peel_chain"],
            "evidence": f"Detected {hop_count} sequential hops with consistent amount reduction (~{amount_variance:.1f}% per hop)"
        })
        total_score += TYPOLOGY_DEFINITIONS["peel_chain"]["risk_score_contribution"]

    # ── Mixer Interaction ────────────────────────────────────────────────────
    if has_mixer:
        detected.append({
            "typology": "mixer_interaction",
            **TYPOLOGY_DEFINITIONS["mixer_interaction"],
            "evidence": "Transaction path passes through confirmed OFAC-listed or known mixer/tumbler contract address"
        })
        total_score += TYPOLOGY_DEFINITIONS["mixer_interaction"]["risk_score_contribution"]

    # ── Rapid Cashout ────────────────────────────────────────────────────────
    if rapid_transfer:
        detected.append({
            "typology": "rapid_cashout",
            **TYPOLOGY_DEFINITIONS["rapid_cashout"],
            "evidence": "Funds forwarded to exchange within short time window of receipt (< 30 min)"
        })
        total_score += TYPOLOGY_DEFINITIONS["rapid_cashout"]["risk_score_contribution"]

    # ── Layering / Dispersion ────────────────────────────────────────────────
    if output_count >= 5:
        detected.append({
            "typology": "layering_dispersion",
            **TYPOLOGY_DEFINITIONS["layering_dispersion"],
            "evidence": f"Single wallet splits funds to {output_count} separate destination wallets"
        })
        total_score += TYPOLOGY_DEFINITIONS["layering_dispersion"]["risk_score_contribution"]

    # ── Cross-chain Bridge ───────────────────────────────────────────────────
    if has_bridge or chain_hops > 1:
        detected.append({
            "typology": "cross_chain_bridge",
            **TYPOLOGY_DEFINITIONS["cross_chain_bridge"],
            "evidence": f"Transaction path spans {chain_hops} blockchain network(s), indicating cross-chain hop"
        })
        total_score += TYPOLOGY_DEFINITIONS["cross_chain_bridge"]["risk_score_contribution"]

    # ── Unhosted Wallet ──────────────────────────────────────────────────────
    if metadata.get("unhosted_intermediaries", 0) > 0:
        detected.append({
            "typology": "unhosted_wallet_concentration",
            **TYPOLOGY_DEFINITIONS["unhosted_wallet_concentration"],
            "evidence": f"{metadata['unhosted_intermediaries']} unhosted/self-custodial wallets detected in transaction path"
        })
        total_score += TYPOLOGY_DEFINITIONS["unhosted_wallet_concentration"]["risk_score_contribution"]

    # ── Cap at 100 ───────────────────────────────────────────────────────────
    total_score = min(total_score, 100)

    return {
        "detected_typologies": detected,
        "typology_count": len(detected),
        "composite_risk_score": total_score,
        "risk_category": _get_risk_category(total_score),
        "risk_color": _get_risk_color(total_score),
    }


def _get_risk_category(score: int) -> str:
    if score >= 80:
        return "CRITICAL"
    elif score >= 60:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    elif score >= 20:
        return "LOW"
    return "MINIMAL"


def _get_risk_color(score: int) -> str:
    if score >= 80:
        return "#ef4444"
    elif score >= 60:
        return "#f97316"
    elif score >= 40:
        return "#f59e0b"
    elif score >= 20:
        return "#3b82f6"
    return "#10b981"
