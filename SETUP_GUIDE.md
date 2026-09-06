# 🛡️ TraceX — Setup & Deployment Guide
### **Autonomous Blockchain Intelligence & Forensic VASP Attribution Engine**
**Theme**: Ministry of Home Affairs (MHA) // Indian Cyber Crime Coordination Centre (I4C)  
**Problem Statement ID**: 26182  
**System Version**: TraceX v2.0-PRO  

---

## 🚀 Quick Start (1-Minute Launch)

### Option 1: Linux / macOS
Open your terminal in this folder and run:
```bash
# 1. (Optional but recommended) Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the engine
./start.sh
# OR manually:
python3 -m uvicorn app:app --host 0.0.0.0 --port 8765 --reload
```
Dashboard will open automatically at: **`http://localhost:8765`**

---

### Option 2: Windows
1. Make sure **Python 3.9+** is installed (with *"Add Python to PATH"* checked).
2. Simply **double-click `start.bat`**  
   *(It will automatically install dependencies and launch `http://localhost:8765` in your default browser)*.
3. Or open Command Prompt (CMD) in this folder:
```cmd
python -m pip install -r requirements.txt
python -m uvicorn app:app --host 0.0.0.0 --port 8765 --reload
```

---

## 📋 System Prerequisites
- **Python**: Version 3.9, 3.10, 3.11, or 3.12
- **Internet Access**: Required for live on-chain explorer calls, CoinGecko price tickers, and Gemini/Groq AI copilot responses.
- **Web Browser**: Chrome, Edge, Brave, Firefox, or Safari.

---

## 🔑 API Keys Configuration (`.env`)

The system uses a backend `.env` file for all blockchain and AI services. A pre-configured `.env` is already included.

If you want to use your own keys, edit `.env`:
```env
# ─── Blockchain Gateways ───
ETHERSCAN_API_KEY=your_etherscan_v2_key
TRONGRID_API_KEY=your_trongrid_api_key
BITQUERY_ACCESS_TOKEN=your_bitquery_oauth_or_access_token
COINGECKO_DEMO_API_KEY=your_coingecko_demo_key

# ─── AI Copilot Dual-Engine ───
GEMINI_API_KEY=your_google_gemini_api_key
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_user_access_token

# ─── Copilot Routing Config ───
AI_PRIMARY_PROVIDER=gemini
AI_FALLBACK_PROVIDER=groq
```

> **Security Note:** All API keys remain strictly secure on the backend server. The frontend never exposes secret tokens.

---

## 📂 Project Architecture

```
sahyog-engine/
├── app.py                     # FastAPI backend routes & core API dispatch
├── dashboard.html             # High-tech cyber LEA command dashboard UI
├── requirements.txt           # Python package dependencies
├── start.sh                   # Linux / Mac launcher script
├── start.bat                  # Windows 1-click launcher script
├── SETUP_GUIDE.md             # This comprehensive deployment guide
├── .env                       # Pre-configured API keys & secrets
├── .env.example               # Sanitized template for public git repos
├── data/
│   └── sahyog.db             # Local SQLite database for audit & case histories
└── engine/                    # Core Forensic & Attribution Subsystems
    ├── address_validator.py   # Multi-chain address validation (EVM, TRON Base58, BTC)
    ├── ai_copilot.py          # Gemini 3.6 Flash + Groq automatic failover copilot
    ├── api_tester.py          # Postman-style live API health & benchmark tester
    ├── demo_cases.py          # Pre-loaded synthetic benchmark crime scenarios
    ├── graph_tracer.py        # NetworkX multi-hop transaction graph & VASP attribution
    ├── notice_generator.py    # Section 91 BNSS 2023 / CrPC legal requisition generator
    ├── ofac_sanctions.py      # US Treasury OFAC SDN Sanctions list screening
    ├── price_feed.py          # CoinGecko spot pricing & INR/USD valuation
    ├── real_api.py            # Live on-chain indexing (Etherscan, TronGrid, Bitquery, Esplora)
    ├── typology.py            # FATF Red Flag Typologies (Peel Chain, Mixer, Structuring)
    └── vasp_cluster.py        # 15+ Regulated VASP cluster heuristics & nodal emails
```

---

## 🎯 How to Use Key Features

### 1. 🏛️ SIH 26182 System Dossier Pop Box
- When opening the website for the first time, an official **Welcome Dossier Pop Box** appears displaying the Ministry of Home Affairs / I4C Problem Statement context.
- Click **`⚡ ENTER FORENSIC COMMAND CENTER`** to close the popup and use the main workspace.
- To re-open it at any time, click **`🏛️ SIH-26182 BRIEF`** in the top navigation bar.

### 2. ⚡ Pre-Loaded Benchmark Cases
- In the left sidebar under `[ 02 // DOSSIER VAULT ]`, click any case:
  - **Case 01:** Cyber Task Scam (TRON USDT / HTX Hot Wallet)
  - **Case 02:** Ransomware Extortion (Ethereum / Binance 14)
  - **Case 03:** Investment Fraud / Ponzi (Bitcoin Peel Chain / CoinDCX)
  - **Case 04:** Phishing Drainer (Multi-Hop EVM Structuring)
- The system automatically plots the transaction graph, labels nodes (Suspect, Mule, Mixer, Terminal Deposit), and attributes the nearest regulated VASP.

### 3. 🔍 Live On-Chain Tracing Mode
- Click the top right **`MODE: DEMO BENCHMARK`** pill to switch to **`MODE: LIVE ON-CHAIN`**.
- Paste any real suspect wallet address (BTC, ETH, TRON `T...`, BNB, SOL) in the sidebar.
- Click **`⚡ TRACE & ATTRIBUTE VASP`** to query live blockchain nodes in real-time!

### 4. 🧠 AI Investigator Copilot
- Scroll to the **Forensic Copilot Panel (Pane 7)**:
  - **Executive Briefing:** Click *"Refresh Summary"* to generate a crime brief.
  - **Section 91 BNSS Case Report:** Click *"Court Report"* to synthesize a complete court-admissible legal requisition.
  - **Interactive Chat:** Ask questions like:
    - *"What FATF money laundering typologies are present in this trace?"*
    - *"Which VASP should receive the Section 91 notice and why?"*
    - *"List the step-by-step LEA action items for the investigating officer."*
  - Watch the **cyber neural radar loading animation** and enjoy clean, structured markdown with **1-click Copy buttons**!

### 5. 🚀 Postman-Style API Health Tester
- Click the **`7/7 APIS LIVE`** radar pill or the **TX logo** in the top header.
- A popup console opens showing live ping benchmarks, HTTP status codes, latency in milliseconds, and raw JSON payloads for all 7 connected gateways!

---

## 🛠️ Troubleshooting & FAQ

#### Q1: "Port 8765 is already in use"
- **Linux/Mac:** Run `lsof -ti:8765 | xargs kill -9`
- **Windows:** Run `netstat -ano | findstr :8765` and kill the PID: `taskkill /F /PID <PID>`

#### Q2: "ModuleNotFoundError: No module named 'fastapi'"
- Run `pip install -r requirements.txt` to install all required packages.

#### Q3: "Direct IP access is not allowed" or proxy error
- If you are running on a corporate network or proxy, run uvicorn with direct localhost:
  `http://127.0.0.1:8765` or `http://localhost:8765`.

---

## ⚖️ Legal & Compliance Disclaimer
*This system is designed for authorized Law Enforcement Agencies (LEAs), cyber crime investigators, and academic research under Ministry of Home Affairs (MHA) / I4C evaluation frameworks. All legal notices and dossiers generated are drafts subject to human verification under Section 91 BNSS 2023 / Section 91 CrPC.*
