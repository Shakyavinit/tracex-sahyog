# 🛡️ TraceX — Team Pitch & Quick Reference Guide
**Problem Statement ID:** 26182  
**Title:** Automated Attribution of Unknown Cryptocurrency Wallets to Nearest Virtual Asset Service Providers (VASPs)  
**Organization:** Ministry of Home Affairs (MHA) | Indian Cyber Crime Coordination Centre (I4C), CIS Division  

---

## 1. 🎯 Executive Overview (What is TraceX?)
* **Short Intro:** **TraceX** is an AI-assisted blockchain intelligence prototype engineered as a decision-support system aligned with Ministry of Home Affairs (MHA / I4C) **SAHYOG Portal** specifications.
* **Core Problem:** In cryptocurrency fraud cases (task scams, ransomware, fraudulent investment schemes), perpetrators rapidly route illicit proceeds into unhosted, self-custodial wallets (such as MetaMask, TrustWallet, or private TRON/BTC addresses) that lack Know-Your-Customer (KYC) records.
* **TraceX Solution:** TraceX reconstructs transaction paths across intermediary mule accounts (peel chains, layering hops) to identify the **destination Centralized Exchange (e.g., Binance, CoinDCX, WazirX, ZebPay)**. This allows Law Enforcement Agencies (LEAs) to review and serve statutory Section 91 disclosure and asset-preservation directives before funds can be liquidated into fiat currency.

---

## 2. 🔑 Integrated Telemetry & APIs (Zero-Cost Architecture)
> **Key Architectural Highlight:** The entire platform operates with **zero paid subscriptions**. All integrated endpoints leverage **100% open, high-reliability public/free-tier APIs (evaluation configuration)**:

| API Provider | Endpoint Domain | Authentication | Core Functional Scope |
| :--- | :--- | :--- | :--- |
| **PublicAML API** | `intelapi.publicaml.org` | ❌ **No Key (Free Open API)** | Screening against US OFAC, UN Sanctions, and terrorist financing lists. |
| **Chainabuse API** | `api.chainabuse.com` | ❌ **Free Tier / Open** | Queries global decentralized scam, fraud, and cybercrime complaint registries. |
| **TronScan API** | `apilist.tronscanapi.com` | ❌ **Open Endpoint** | TRON network query for USDT (TRC-20) balances, energy, and transfer metrics. |
| **Blockchair API** | `api.blockchair.com` | ❌ **Free Tier / Open** | Bitcoin (BTC) on-chain UTXO balance and chronological timestamp telemetry. |
| **Etherscan API** | `api.etherscan.io` | ❌ **Free Tier / Community** | Ethereum (ETH) and ERC-20 smart contract balance and transaction history. |

---

## 3. ⚡ Core Capabilities & Technical Innovations

1. **Multi-Chain Address Auto-Detection:**
   * Automatically classifies Bitcoin (BTC legacy/SegWit/Taproot), Ethereum (EVM), TRON (USDT TRC-20), BNB Chain, Solana, and Polygon addresses by cryptographic format.

2. **Nearest VASP Attribution & Path Traversal:**
   * Perpetrators rarely deposit directly into an exchange; they layer proceeds across 3–6 intermediary mule wallets. TraceX traverses transaction hops to pinpoint the **terminal VASP** and compute a calibrated **Attribution Confidence Score (%)**.

3. **Forensic Valuation Telemetry (INR ₹ & USD $):**
   * Computes indicative market valuation of traced assets in both Indian Rupees (₹ INR) and US Dollars ($ USD) using reference price oracles.

4. **Automated FATF Money Laundering Typology Detection:**
   * Detects and classifies structured laundering patterns:
     * **Peel Chains (IOC-001):** Incremental peeling of small amounts while routing principal volume.
     * **Mixers / Tumblers (IOC-002):** Interactions with Tornado Cash, ChipMixer, or privacy protocols.
     * **Rapid Cashout (IOC-003):** High-velocity routing to an exchange within 30 minutes of initial theft.
     * **Layering Dispersion (IOC-004):** Splitting funds from 1 source into 5–10 mule wallets.

5. **1-Click Draft Section 91 BNSS / CrPC Requisitions (Subject to IO Review):**
   * Generates a fully formatted draft statutory disclosure and asset-preservation notice auto-populated with the exchange's **Registered Nodal Officer Email, Legal Headquarters Address, FIR Reference, Wallet Coordinates, and a 30-Day Asset Preservation Mandate**.
   * One-click **Print / PDF Export**, **Clipboard Copy**, and **Download (.txt)** options for authorized officer verification.

6. **Interactive Vector Topology Map:**
   * High-definition, hardware-accelerated canvas rendering illustrating the end-to-end criminal pipeline:
     `Suspect Origin 🔴` ➔ `Unhosted Mule Layer 🟡` ➔ `Mixer Flag ⚫` ➔ `Exchange Deposit 🟢`

---

## 4. 💡 30-Second Elevator Pitch
> *"TraceX is a prototype blockchain forensic intelligence decision-support system that traces illicit fund flows from unhosted suspect wallets across multi-hop peel chains toward destination centralized exchanges (e.g., Binance, CoinDCX, WazirX). It integrates on-chain queries, cryptographic OFAC sanctions verification, public scam intelligence feeds, and automated FATF money laundering typology classification. Upon attributing the terminal VASP, it synthesizes a draft Section 91 BNSS / CrPC asset-preservation requisition directive for Investigating Officer review. All integrated APIs are configured with evaluation keys and operate in demonstration mode. Final legal action requires authorized IO review and approval."*
