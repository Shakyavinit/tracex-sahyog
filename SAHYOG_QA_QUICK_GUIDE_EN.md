# 🎯 TraceX (SAHYOG) — Executive Q&A Quick Guide
### Smart India Hackathon 2026 | Problem Statement: SIH26182 (Ministry of Home Affairs / I4C)
> **Executive Purpose**: A rapid, high-impact technical and operational reference guide designed for law enforcement officers, forensic analysts, and hackathon evaluators to understand the complete TraceX system in 5 minutes.

---

## 📌 Section 1: Problem Statement & System Essentials

### Q1: What is TraceX (SAHYOG) and what real-world crisis does it solve?
**Answer:**
In modern cyber financial crimes (UPI phishing, digital arrest scams, fraudulent investment apps, ransomware), criminal syndicates rapidly convert illicit fiat (INR) into cryptocurrency—predominantly **USDT (TRC-20)** and **Bitcoin**—to evade immediate bank account freezes.
* **The Operational Bottleneck**: Blockchain ledgers are pseudonymous. Investigating Officers (IOs) see only raw alphanumeric addresses (e.g., `TR7NHqje...` or `0x3892...`) with zero visible identity, nationality, or banking details. Tracing these manually across blockchain explorers takes weeks, by which time funds are laundered and cashed out.
* **The TraceX Solution**: TraceX is an autonomous crypto-forensic intelligence engine that traces illicit funds from the victim's wallet across complex multi-hop transaction trails to the terminal **Virtual Asset Service Provider (VASP/Exchange)** in **1 to 3 seconds**, generating court-admissible debit freeze notices in real time.

---

### Q2: What is a VASP and why is it the pivotal target of crypto investigations?
**Answer:**
**VASP** stands for **Virtual Asset Service Provider**—centralized cryptocurrency exchanges such as **CoinDCX, WazirX, Binance, ZebPay, and Mudrex**.
* **The Inevitable Cashout Chokepoint**: A scammer cannot spend USDT or Bitcoin to buy real estate, groceries, or luxury goods in India directly. To monetize the stolen assets, they must route funds to an exchange that operates fiat ramps (INR bank withdrawals or P2P trading desks).
* **KYC Identity Binding**: Regulated VASPs are mandated under PMLA to collect verified **Know Your Customer (KYC)** data—including **Aadhaar, PAN, verified phone numbers, bank accounts, and device IP logs**.
* **The Strategic Objective**: If law enforcement identifies the exchange's deposit address before the fraudster completes the fiat withdrawal, the funds can be frozen under statutory order, and the perpetrator's real identity can be subpoenaed.

---

## 🔄 Section 2: End-to-End System Workflow

### Q3: What is the step-by-step end-to-end workflow of TraceX?
**Answer:**
TraceX operates through an automated 5-stage pipeline:

```
┌────────────────────────────────────────────────────────┐
│  Stage 1: INGESTION & TARGET INPUT                     │
│  IO enters suspect crypto address, FIR & Case metadata │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Stage 2: PROTOCOL & BLOCKCHAIN DETECTION              │
│  Automatic detection: TRON (Base58), BTC, EVM (Hex)    │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Stage 3: MULTI-HOP GRAPH TRAVERSAL                    │
│  BFS algorithm explores UTXO/Account trails (Hop 0-3)  │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Stage 4: VASP ATTRIBUTION & AML TYPOLOGY ENGINE       │
│  Cluster matching + FATF money laundering risk scoring │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│  Stage 5: STATUTORY LEGAL DISPATCH & AI COPILOT        │
│  Sec 106 Freeze Notice + Sec 65B Hash + Sub-Second Q&A │
└────────────────────────────────────────────────────────┘
```

1. **Stage 1 (Ingestion)**: The Investigating Officer inputs the suspect wallet address, victim FIR number, and date of incident into the TraceX portal.
2. **Stage 2 (Protocol Detection)**: The engine validates checksums and identifies the underlying protocol (TRON TRC-20, Bitcoin SegWit/Taproot, or Ethereum EVM).
3. **Stage 3 (Multi-Hop Tracing)**: The engine executes an automated Breadth-First Search (BFS) algorithm to retrieve on-chain transfers, distinguishing change outputs from pass-through mule hops.
4. **Stage 4 (VASP Attribution & AML Screening)**: The terminal destination is matched against a database of verified exchange hot/deposit wallets, while FATF heuristics evaluate money laundering patterns.
5. **Stage 5 (Legal Enforcement & AI Guidance)**: The system automatically synthesizes a **Section 106 BNSS Debit Freeze Directive**, a **Section 91 BNSS KYC Requisition**, and enables the **Groq LPU-powered AI Copilot** for interactive tactical guidance.

---

### Q4: What are Multi-Hop Transaction Trails (Hop 0, Hop 1, Hop 2, Hop 3)?
**Answer:**
Cyber syndicates rarely deposit stolen funds directly from the crime wallet into an exchange. They route funds through intermediate "mule" or "buffer" wallets to create synthetic transaction volume:
* **Hop 0 (Genesis / Inception Wallet)**: The initial wallet where the victim's stolen funds or ransomware ransom was originally received.
* **Hop 1 (Primary Mule Wallet)**: The first split or layering stage. Funds are often partitioned into multiple smaller transactions (peeling chain) to evade detection thresholds.
* **Hop 2 (Secondary Aggregator / Transit Mule)**: Intermediary wallets that recombine partitioned funds or swap tokens across chains to obfuscate the paper trail.
* **Hop 3 (Terminal Gateway / Exchange Deposit)**: The final unhosted deposit address assigned to a specific user on a centralized exchange (e.g., CoinDCX or Binance). Once funds land here, they are queued for cashout.

---

### Q5: How is the VASP Attribution Confidence Score calculated?
**Answer:**
Attribution is backed by a rigorous deterministic mathematical formula combining cluster matching, hop proximity, regulatory registration, and illicit mixer penalties:

$$\text{Confidence Score} = \text{Match} (+50\%) + \text{Proximity} (+25\%) + \text{Regulation} (+21\%) - \text{Mixer Penalty} (-30\%)$$

* **Direct Cluster Match (+50%)**: Awarded when the destination address matches a verified hot wallet, sweeper address, or deposit infrastructure cluster of a known VASP.
* **Proximity Score (+25%)**: Awarded based on geodesic distance from Genesis. Transitions completed within $\le 2$ hops receive the full $+25\%$; paths requiring $3\text{--}4$ hops receive $+15\%$.
* **Regulatory Alignment (+21%)**: Awarded if the identified VASP is registered as a Reporting Entity with **FIU-IND (India)** or comparable AML regulators (e.g., FinCEN, FCA), ensuring actionable legal compliance channels.
* **Mixer / Anonymizer Penalty (-30%)**: Subtracted if funds traversed through a non-custodial privacy mixer (e.g., Tornado Cash, Blender.io), reflecting broken custodial continuity.

**Standard Outcome**: Clean multi-hop paths to verified exchanges typically yield a **92% Confidence Score (High Confidence)**. If the score falls below $65\%$, automated dispatch is locked and marked *"Manual Forensic Review Required"*.

---

## 🌐 Section 3: API Architecture & Ecosystem Breakdown

### Q6: Which API does what in TraceX? (Complete Reference Matrix)
**Answer:**

| No. | API / Service Name | Layer / Type | Core Forensic Role |
| :---: | :--- | :--- | :--- |
| **1** | **TronGrid API** | Blockchain RPC | Fetches real-time **USDT (TRC-20)** transfers, token contract events, TRX bandwidth/energy, and account balances on TRON. |
| **2** | **Etherscan API v2** | Blockchain Indexer | Tracks **Ethereum & EVM** contract calls, ERC-20 stablecoin movements, internal transactions, and gas provenance. |
| **3** | **Blockstream Esplora API** | Blockchain Indexer | Analyzes **Bitcoin (BTC)** mainnet UTXO inputs/outputs, mempool congestion, fee rates, and wallet transaction histories. |
| **4** | **Bitquery GraphQL v2** | Cross-Chain Analytics | Traces decentralized exchange (DEX) liquidity pool swaps (Uniswap, PancakeSwap) and cross-chain bridge hops. |
| **5** | **CoinGecko API** | Market Intelligence | Provides real-time and historical spot rates in USD and **₹ INR** for accurate statutory seizure valuation in Indian courts. |
| **6** | **OFAC SDN Sanctions Database** | AML & Sanctions | Cross-references addresses against US Treasury sanctioned entities, state-sponsored cyber syndicates (Lazarus), and banned mixers. |
| **7** | **ChainAbuse API** | Threat Intelligence | Ingests real-time community-reported cyber threat intelligence, malicious contract reports, and scam address flags. |
| **8** | **Groq LPU API (`qwen/qwen3.8-27b`)** | Inference Hardware | **Primary AI Copilot**: Delivers ultra-low latency (<1.0s) forensic intelligence and legal guidance in English and Hindi. |
| **9** | **Google Gemini API (`gemini-3.5-flash`)** | Cloud GenAI | **Enterprise Cloud Failover**: Handles deep legal synthesis, complex typology reasoning, and acts as resilient backup. |
| **10**| **Neo4j Aura Cloud DB** | Graph Database | Stores persistent entity graphs with wallets modeled as **Nodes** and transfers as **Directed Weighted Edges**. |

---

## 📊 Section 4: Risk Score & FATF Typology Engine

### Q7: What is the Risk Score and how is it calculated from 0 to 100?
**Answer:**
The TraceX Risk Score is a quantitative measure of money laundering probability, calculated according to typologies established by the **Financial Action Task Force (FATF)** and **Interpol**:

* **Baseline Score**: **20 Points** (Default forensic anomaly) or **35 Points** (Target pre-flagged in external crime databases).

**Additive Typology Weights:**
1. **Peeling Chain (+20 Points)**: Fraudster executes sequential transfers peeling off small amounts ($<15\%$ variation) while forwarding the bulk balance to a new address.
2. **Rapid Cashout (+25 Points)**: Inflow funds are forwarded to an exchange gateway within $<30$ minutes of receipt (anti-detection velocity).
3. **Layering / Fan-Out (+30 Points)**: Funds from a single wallet are dispersed across $\ge 5$ recipient mule accounts simultaneously.
4. **Mixer / Privacy Protocol (+40 Points)**: Address has direct or 1-hop indirect interaction with Tornado Cash, ChipMixer, or privacy-enhancing contracts.
5. **Cross-Chain Bridge (+25 Points)**: Funds hop across independent blockchains (e.g., Bitcoin $\to$ Ethereum $\to$ TRON) via bridge protocols.
6. **Unhosted Transit Concentration (+15 Points)**: Transit path relies exclusively on private, unhosted wallets lacking KYC compliance.

**Risk Classification Tiers:**
* `0 to 25`: **MINIMAL RISK** — Standard retail or normal user activity.
* `26 to 50`: **LOW RISK** — Low-velocity transfer; standard monitoring.
* `51 to 70`: **MEDIUM RISK** — Suspicious velocity or intermediate mule hops detected.
* `71 to 85`: **HIGH RISK** — High-confidence money laundering structure (Peeling + Layering).
* `86 to 100`: **CRITICAL RISK** — Active cybercrime syndicate, sanctioned entity, or emergency cashout in progress.

---

## ⚖️ Section 5: Statutory & Legal Framework (Indian Law)

### Q8: What are Section 106 & Section 91 BNSS notices, and how is Section 65B BSA compliance achieved?
**Answer:**
TraceX directly aligns with India's overhauled criminal justice system under the **Bharatiya Nagarik Suraksha Sanhita (BNSS 2023)** and **Bharatiya Sakshya Adhiniyam (BSA 2023)**:

1. **Section 106 BNSS 2023 / Sec 102 CrPC (Debit Freeze Directive)**:
   * **Target**: Compliance and Law Enforcement Nodal Officer of the identified VASP (e.g., CoinDCX, Binance).
   * **Mandate**: Orders the immediate electronic debit freeze of the identified deposit wallet and linked trading account, preventing the scammer from withdrawing fiat to bank accounts or executing P2P sales.
2. **Section 91 BNSS 2023 / Sec 91 CrPC (KYC & Audit Logs Requisition)**:
   * **Target**: VASP Legal Directorate.
   * **Mandate**: Directs the exchange to surrender complete KYC records (Aadhaar, PAN card, verified mobile number, linked bank accounts, login IP logs with timestamps) within 24 hours.
3. **Section 65B BSA 2023 / Indian Evidence Act (Certificate of Electronic Evidence)**:
   * Every forensic dossier generated by TraceX is stamped with a **SHA-256 cryptographic hash**, system hardware UUID, timestamp, and immutable blockchain block headers, satisfying the strict evidentiary standards required by Indian trial courts.

---

## 🤖 Section 6: Dual-Engine AI Copilot Architecture

### Q9: Why does TraceX utilize a Dual-Engine AI Copilot (Groq LPU + Gemini Flash)?
**Answer:**
Law enforcement field operations cannot tolerate standard cloud LLM latency (10 to 15 seconds), which can cause suspects to complete cashouts before an officer receives actionable advice:

1. **Primary Engine — Groq LPU (`qwen/qwen3.8-27b`)**:
   * **Latency**: **800ms to 1.2 seconds** (sub-second response).
   * **Function**: Provides instant, tactically grounded tactical answers in plain English or Hindi (e.g., *"Funds have hit CoinDCX deposit address. Click button below to dispatch Section 106 freeze notice immediately."*).
2. **Failover Cloud Engine — Google Gemini 3.5 Flash**:
   * **Latency**: 5 to 7 seconds.
   * **Function**: Automatically takes over if the primary Groq endpoint experiences rate-limiting, network throttling, or when multi-document legal synthesis is required.
3. **Deterministic Forensic Guardrails**:
   * The AI engines are bound to strict system prompts that ingest live JSON forensic telemetry. The AI cannot hallucinate non-existent wallets, fabricate balances, or cite non-existent statutory sections.

---

## 🎤 Section 7: Two-Minute Winning Elevator Pitch for Judges

### Q10: How should a team pitch TraceX to hackathon evaluators in 2 minutes?
**Answer (Deliver these 4 core pillars with confidence):**

> 1. **The Problem**: *"Judges, when a citizen is defrauded of Rs. 10 Lakhs in an online scam, cybercriminals convert that money into cryptocurrency within minutes. Police investigations stall because blockchain addresses are pseudonymous—just random strings of characters without names or phone numbers."*
> 
> 2. **The Innovation**: *"Our system, **TraceX (SAHYOG)**, uses an automated Breadth-First Search graph traversal engine to trace the money across Bitcoin, Ethereum, and TRON, connecting that anonymous wallet to the exit exchange—like CoinDCX or Binance—in **just 1 to 3 seconds** with a **92% attribution confidence score**."*
> 
> 3. **The Autonomous Action**: *"TraceX doesn't just draw pretty graphs. It evaluates FATF money laundering typologies and instantly generates ready-to-dispatch **Section 106 BNSS Debit Freeze Directives** and **Section 91 BNSS KYC Summons** with Section 65B BSA cryptographic certification."*
> 
> 4. **The Officer's Copilot**: *"Powered by a **Dual-Engine AI Copilot on Groq LPU and Gemini**, investigating officers get instant tactical intelligence in under 1 second. TraceX transforms months of manual forensic backlog into real-time asset recovery."*

---
*TraceX (SAHYOG) — SIH26182 Executive Reference Guide | Ministry of Home Affairs / I4C*
