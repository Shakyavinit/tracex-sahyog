import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette
DARK_BG = RGBColor(6, 8, 16)
SURFACE = RGBColor(13, 16, 30)
CARD_BG = RGBColor(18, 22, 43)
ACCENT_BLUE = RGBColor(79, 110, 247)
ACCENT_GREEN = RGBColor(52, 211, 153)
ACCENT_RED = RGBColor(244, 63, 94)
ACCENT_WARN = RGBColor(245, 158, 11)
TEXT_WHITE = RGBColor(240, 244, 250)
TEXT_MUTED = RGBColor(148, 163, 184)

def set_slide_background(slide, color=DARK_BG):
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = color
    bg_shape.line.fill.background()
    return bg_shape

def create_header(slide, title_text, category_text="MINISTRY OF HOME AFFAIRS (MHA) | I4C - CIS DIVISION"):
    tb_cat = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.4))
    p_cat = tb_cat.text_frame.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = ACCENT_BLUE
    
    tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
    p_title = tb_title.text_frame.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = TEXT_WHITE

def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=None):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
    else:
        card.line.fill.background()
    return card

# ─── SLIDE 1: Title Slide ─────────────────────────────────────────────
s1 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(s1)

tb_emblem = s1.shapes.add_textbox(Inches(0.8), Inches(1.0), Inches(11.5), Inches(0.6))
p_e = tb_emblem.text_frame.paragraphs[0]
p_e.text = "🏛️ PROBLEM STATEMENT ID: 26182 | MHA I4C CIS DIVISION | TraceX ENGINE"
p_e.font.size = Pt(13)
p_e.font.bold = True
p_e.font.color.rgb = ACCENT_GREEN

tb_main = s1.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(11.5), Inches(2.2))
p_m = tb_main.text_frame.paragraphs[0]
p_m.text = "TraceX — Automated Attribution of Unknown Wallets\nto Nearest Virtual Asset Service Providers (VASPs)"
p_m.font.size = Pt(32)
p_m.font.bold = True
p_m.font.color.rgb = TEXT_WHITE

p_sub = tb_main.text_frame.add_paragraph()
p_sub.text = "Integrated with SAHYOG Portal via Blockchain Intelligence APIs & Graph Analytics"
p_sub.font.size = Pt(18)
p_sub.font.color.rgb = ACCENT_BLUE

# Metrics Cards on Title Slide
cards_data = [
    ("⚡ LATENCY REDUCTION", "< 5 Seconds", "From 48-72h manual tracing to instant attribution"),
    ("🌐 MULTI-CHAIN COVERAGE", "6+ Blockchains", "BTC, ETH, TRON (USDT), BNB, SOL, Polygon"),
    ("📜 STATUTORY NOTICES", "Sec 91 CrPC", "Auto-generated freezing & KYC disclosure notices")
]
for i, (title, stat, desc) in enumerate(cards_data):
    left = Inches(0.8 + i * 4.0)
    add_card(s1, left, Inches(4.5), Inches(3.7), Inches(2.2))
    tb_c = s1.shapes.add_textbox(left + Inches(0.2), Inches(4.7), Inches(3.3), Inches(1.8))
    p1 = tb_c.text_frame.paragraphs[0]
    p1.text = title
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_GREEN
    
    p2 = tb_c.text_frame.add_paragraph()
    p2.text = stat
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    
    p3 = tb_c.text_frame.add_paragraph()
    p3.text = desc
    p3.font.size = Pt(11)
    p3.font.color.rgb = TEXT_MUTED

# ─── SLIDE 2: Problem Analysis & Existing Bottlenecks ──────────────────
s2 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(s2)
create_header(s2, "The Investigative Challenge: Unhosted Wallets & Laundering Layers")

left_card = add_card(s2, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
tb_lc = s2.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
p = tb_lc.text_frame.paragraphs[0]
p.text = "🔴 Existing Investigation Bottlenecks"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = ACCENT_RED

points_left = [
    ("Unhosted Wallet Blindspot", "Perpetrators route fraud proceeds into self-custodial wallets (MetaMask, Trust Wallet) with zero KYC records."),
    ("Complex Multi-Hop Layering", "Funds pass through peel chains, smurfing networks, and cross-chain bridges to deliberately obscure origin."),
    ("Manual Blockchain Exploration", "LEAs manually inspect block explorers; tracing a 5-hop path to an exchange takes days."),
    ("Critical Freezing Delay", "By the time an exchange is manually identified, criminal syndicates cash out to fiat, rendering asset recovery impossible.")
]
for title, desc in points_left:
    p1 = tb_lc.text_frame.add_paragraph()
    p1.text = f"• {title}: "
    p1.font.bold = True
    p1.font.size = Pt(13)
    p1.font.color.rgb = TEXT_WHITE
    p2 = tb_lc.text_frame.add_paragraph()
    p2.text = f"   {desc}"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED

right_card = add_card(s2, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), border_color=ACCENT_BLUE)
tb_rc = s2.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
p = tb_rc.text_frame.paragraphs[0]
p.text = "🟢 The Solution: TraceX Attribution Engine"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

points_right = [
    ("Instant Graph Attribution", "Graph traversal algorithm automatically locates the nearest centralized exchange receiving deposits in seconds."),
    ("Multi-Chain Parsing", "Handles Bitcoin UTXO, Ethereum EVM, TRON TRC-20, and Solana account models seamlessly."),
    ("FATF Typology Scoring", "Detects peel chains, mixer hops (Tornado Cash), rapid cashouts, and fan-out dispersion in real-time."),
    ("Automated Freezing Notices", "Synthesizes statutory Section 91 CrPC / Section 69B IT Act directives with auto-populated VASP nodal contacts.")
]
for title, desc in points_right:
    p1 = tb_rc.text_frame.add_paragraph()
    p1.text = f"✔ {title}: "
    p1.font.bold = True
    p1.font.size = Pt(13)
    p1.font.color.rgb = TEXT_WHITE
    p2 = tb_rc.text_frame.add_paragraph()
    p2.text = f"   {desc}"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED

# ─── SLIDE 3: End-to-End Investigation Workflow ────────────────────────
s3 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(s3)
create_header(s3, "End-to-End Investigation Workflow (Step-by-Step)")

workflow_steps = [
    ("Step 1: Input", "Suspect Wallet", "Suspect crypto address reported on SAHYOG. Chain is auto-detected.", ACCENT_BLUE),
    ("Step 2: Analysis", "Graph Traversal", "NetworkX builds directed graph; traces mule hops & peel chains.", ACCENT_BLUE),
    ("Step 3: Screening", "AML & Sanctions", "Live query to PublicAML (OFAC) & Chainabuse scam databases.", ACCENT_WARN),
    ("Step 4: Attribution", "Nearest VASP Match", "Identifies exchange cluster (Binance, CoinDCX, etc.) + confidence %.", ACCENT_GREEN),
    ("Step 5: Action", "Section 91 CrPC", "Auto-generates legal notice with INR value & compliance nodal email.", ACCENT_RED)
]

for i, (step_num, title, desc, col) in enumerate(workflow_steps):
    left = Inches(0.8 + i * 2.4)
    card = add_card(s3, left, Inches(2.0), Inches(2.25), Inches(4.6), border_color=col)
    
    tb = s3.shapes.add_textbox(left + Inches(0.15), Inches(2.2), Inches(1.95), Inches(4.2))
    p1 = tb.text_frame.paragraphs[0]
    p1.text = step_num
    p1.font.size = Pt(11)
    p1.font.bold = True
    p1.font.color.rgb = col
    
    p2 = tb.text_frame.add_paragraph()
    p2.text = title
    p2.font.size = Pt(15)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    
    p3 = tb.text_frame.add_paragraph()
    p3.text = "\n" + desc
    p3.font.size = Pt(11)
    p3.font.color.rgb = TEXT_MUTED

# ─── SLIDE 4: System Architecture & Technical Stack ────────────────────
s4 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(s4)
create_header(s4, "System Architecture: Modular & Scalable Design")

arch_blocks = [
    ("🖥️ Presentation Layer", "LEA Forensic Dashboard", [
        "Single-Page Interactive Dashboard (HTML5/Canvas)",
        "Canvas fund flow graph visualization",
        "Risk gauge & FATF typologies display",
        "Section 91 CrPC notice generator & copy tool"
    ], ACCENT_BLUE),
    ("⚡ Core Backend Gateway", "FastAPI Service (app.py)", [
        "High-performance REST API endpoints",
        "Integrated SQLite database (sahyog.db)",
        "OpenAPI / Swagger documentation (/docs)",
        "Multi-chain address format detection"
    ], ACCENT_GREEN),
    ("🧠 Intelligence & Attribution", "NetworkX Graph Tracer", [
        "Directed multi-hop transaction tracing",
        "FATF typology detection (Peel chain, mixers)",
        "15+ VASP registry (Indian & Global exchanges)",
        "Confidence calculation algorithm"
    ], ACCENT_WARN),
    ("🔗 Real Data Interface", "Blockchain & AML APIs", [
        "PublicAML API (Live OFAC/UN sanctions)",
        "Chainabuse API (Live scam database)",
        "Blockchair / TronScan / Etherscan (Balances)",
        "Graceful simulated fallback model"
    ], ACCENT_RED)
]

for i, (layer_title, comp_name, features, col) in enumerate(arch_blocks):
    col_idx = i % 2
    row_idx = i // 2
    left = Inches(0.8 + col_idx * 5.9)
    top = Inches(1.8 + row_idx * 2.6)
    
    add_card(s4, left, top, Inches(5.6), Inches(2.4), border_color=col)
    tb = s4.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(5.2), Inches(2.1))
    
    p1 = tb.text_frame.paragraphs[0]
    p1.text = f"{layer_title} — {comp_name}"
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = col
    
    for f in features:
        p = tb.text_frame.add_paragraph()
        p.text = f"• {f}"
        p.font.size = Pt(11)
        p.font.color.rgb = TEXT_MUTED

# ─── SLIDE 5: VASP Attribution & Legal Notice Engine ──────────────────
s5 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(s5)
create_header(s5, "VASP Attribution & Lawful Disclosure Notice Generator")

left_card = add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
tb_l = s5.shapes.add_textbox(Inches(1.1), Inches(2.0), Inches(5.0), Inches(4.5))
p = tb_l.text_frame.paragraphs[0]
p.text = "🏦 VASP Cluster Registry & Verification"
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = ACCENT_BLUE

vasp_info = [
    ("Indian VASPs (PMLA / FIU-IND)", "WazirX, CoinDCX, ZebPay, Mudrex, CoinSwitch — Nodal officers, registered addresses & compliance emails."),
    ("International Exchanges", "Binance, OKX, Bybit, KuCoin, Kraken, Coinbase — Escalation via MLAT, INTERPOL I-24/7, and Egmont Group channels."),
    ("Mixers & Sanctioned Pools", "Tornado Cash (ETH/BNB pools), ChipMixer — Explicit OFAC SDN flagging."),
    ("DeFi Bridges", "AnySwap, cBridge, Polygon Bridge cross-chain transfer signatures.")
]
for title, desc in vasp_info:
    p1 = tb_l.text_frame.add_paragraph()
    p1.text = f"• {title}: "
    p1.font.bold = True
    p1.font.size = Pt(12)
    p1.font.color.rgb = TEXT_WHITE
    p2 = tb_l.text_frame.add_paragraph()
    p2.text = f"   {desc}"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = TEXT_MUTED

right_card = add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0), border_color=ACCENT_GREEN)
tb_r = s5.shapes.add_textbox(Inches(7.1), Inches(2.0), Inches(5.1), Inches(4.5))
p = tb_r.text_frame.paragraphs[0]
p.text = "📜 Statutory Notice Synthesis (Court-Ready)"
p.font.size = Pt(17)
p.font.bold = True
p.font.color.rgb = ACCENT_GREEN

notice_points = [
    ("Statutory Directives", "Issued under Section 91 & 102 CrPC, Section 69B IT Act, and PMLA (2002) Section 17."),
    ("Information Demanded", "Full KYC (Aadhaar/PAN), bank account linkage, counterparty wallet records, IP logs & device fingerprints."),
    ("Immediate Asset Hold", "Directs VASP to impose immediate 30-day operational freeze on the target deposit wallet."),
    ("Tamper-Proof Audit Hash", "Unique SHA-256 evidence integrity hash embedded for evidentiary admissibility in Indian courts.")
]
for title, desc in notice_points:
    p1 = tb_r.text_frame.add_paragraph()
    p1.text = f"✔ {title}: "
    p1.font.bold = True
    p1.font.size = Pt(12)
    p1.font.color.rgb = TEXT_WHITE
    p2 = tb_r.text_frame.add_paragraph()
    p2.text = f"   {desc}"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = TEXT_MUTED

# ─── SLIDE 6: Impact, Evaluation & Operational Benefits ────────────────
s6 = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_background(s6)
create_header(s6, "Operational Impact & Expected Deliverables")

impact_boxes = [
    ("⚡ Instant Turnaround", "Reduces investigation latency from 48-72 hours to under 5 seconds, enabling immediate asset freezing before cashout."),
    ("🎯 High Attribution Accuracy", "Heuristic graph analysis coupled with known deposit cluster patterns yields attribution confidence scores above 85%."),
    ("🛡️ Proactive Risk Intelligence", "Automated detection of FATF typologies (peel chains, mixer funnels) flags high-risk illicit syndicates."),
    ("⚖️ Seamless Legal Compliance", "Standardized Section 91 CrPC notice templates ensure rapid acceptance by VASP legal response teams."),
    ("🇮🇳 National Security & LEA Support", "Equips I4C, State Cyber Crime Police Stations, and central agencies with indigenous intelligence capabilities."),
    ("🌐 Multi-Jurisdictional Tracing", "Supports cross-border investigative routing through INTERPOL NCB New Delhi and FIU-IND channels.")
]

for i, (title, desc) in enumerate(impact_boxes):
    col_idx = i % 3
    row_idx = i // 3
    left = Inches(0.8 + col_idx * 3.9)
    top = Inches(1.8 + row_idx * 2.5)
    
    add_card(s6, left, top, Inches(3.7), Inches(2.3))
    tb = s6.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), Inches(3.3), Inches(2.0))
    
    p1 = tb.text_frame.paragraphs[0]
    p1.text = title
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = ACCENT_GREEN
    
    p2 = tb.text_frame.add_paragraph()
    p2.text = "\n" + desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED

output_pptx = "/home/mrx/Documents/dark web/HACK/sahyog-engine/SAHYOG_Workflow_Presentation_PS26182.pptx"
prs.save(output_pptx)
print(f"Presentation saved successfully to {output_pptx}")
