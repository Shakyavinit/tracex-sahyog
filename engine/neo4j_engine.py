"""
TraceX — Neo4j Aura Cloud Graph Engine
Enterprise Blockchain Graph Intelligence & Cypher Forensics
Connects to Neo4j Aura (Instance: VINI [Virtual Asset Investigation & Network Intelligence] / afbde657)
"""

import os
import time
import logging
import re
from typing import Dict, Any, List, Optional
from neo4j import GraphDatabase, Driver

logger = logging.getLogger("tracex.neo4j")

# Credentials from environment or defaults
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://afbde657.databases.neo4j.io")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "afbde657")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "hBT80gGZ4iWQWpBevaQXfCTDFWvSoFgHNj7zNSYzuOg")
AURA_INSTANCEID = os.getenv("AURA_INSTANCEID", "afbde657")
AURA_INSTANCENAME = os.getenv("AURA_INSTANCENAME", "VINI")
VINI_FULL_NAME = os.getenv("VINI_FULL_NAME", "Virtual Asset Investigation & Network Intelligence")

_driver: Optional[Driver] = None


def get_driver() -> Optional[Driver]:
    """Obtain or initialize singleton Neo4j driver with auto-reconnect."""
    global _driver
    if _driver is not None:
        try:
            return _driver
        except Exception:
            _driver = None

    if not NEO4J_URI or not NEO4J_PASSWORD:
        return None

    try:
        _driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USERNAME, NEO4J_PASSWORD),
            max_connection_lifetime=30 * 60,
            max_connection_pool_size=50,
            connection_acquisition_timeout=15.0
        )
        return _driver
    except Exception as e:
        logger.error(f"Failed to initialize Neo4j driver: {e}")
        return None


def init_neo4j_schema():
    """Create uniqueness constraints and full-text indexes for forensics."""
    driver = get_driver()
    if not driver:
        return False
    try:
        with driver.session() as session:
            session.run("CREATE CONSTRAINT wallet_addr_unique IF NOT EXISTS FOR (w:Wallet) REQUIRE w.address IS UNIQUE")
            session.run("CREATE CONSTRAINT vasp_name_unique IF NOT EXISTS FOR (v:VASP) REQUIRE v.name IS UNIQUE")
            session.run("CREATE CONSTRAINT case_id_unique IF NOT EXISTS FOR (c:Case) REQUIRE c.case_id IS UNIQUE")
        return True
    except Exception as e:
        logger.warning(f"Schema initialization warning: {e}")
        return False


def check_neo4j_status() -> Dict[str, Any]:
    """Verify live connectivity and fetch graph telemetry."""
    driver = get_driver()
    if not driver:
        return {
            "status": "offline",
            "error": "Driver not initialized",
            "instance_name": AURA_INSTANCENAME,
            "full_name": VINI_FULL_NAME,
            "instance_id": AURA_INSTANCEID,
        }

    t0 = time.time()
    try:
        driver.verify_connectivity()
        with driver.session() as session:
            res_nodes = session.run("MATCH (n) RETURN count(n) AS node_count")
            node_count = res_nodes.single()["node_count"]

            res_rels = session.run("MATCH ()-[r]->() RETURN count(r) AS rel_count")
            rel_count = res_rels.single()["rel_count"]

        latency_ms = round((time.time() - t0) * 1000, 1)
        return {
            "status": "connected",
            "instance_name": AURA_INSTANCENAME,
            "full_name": VINI_FULL_NAME,
            "instance_id": AURA_INSTANCEID,
            "uri": NEO4J_URI.split("@")[-1],
            "node_count": node_count,
            "relationship_count": rel_count,
            "latency_ms": latency_ms,
            "cloud": "Neo4j Aura Cloud",
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "instance_name": AURA_INSTANCENAME,
            "full_name": VINI_FULL_NAME,
            "instance_id": AURA_INSTANCEID,
            "latency_ms": round((time.time() - t0) * 1000, 1)
        }


def sync_trace_to_neo4j(trace_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ingest a complete cryptographic trace into Neo4j Aura.
    Creates Case, Wallets, Transactions, and Terminal VASP nodes.
    """
    driver = get_driver()
    if not driver:
        return {"success": False, "error": "No Neo4j connection"}

    case_id = trace_data.get("case_id") or f"TRACE-{int(time.time())}"
    chain = trace_data.get("chain", "ETH")
    suspect_address = trace_data.get("suspect_address", "")
    nearest_vasp = trace_data.get("nearest_vasp", {})
    vasp_name = nearest_vasp.get("name", "Unknown VASP")
    nodes = trace_data.get("nodes", [])
    edges = trace_data.get("edges", [])

    try:
        with driver.session() as session:
            # 1. Create or update Case node
            session.run("""
                MERGE (c:Case {case_id: $case_id})
                SET c.chain = $chain,
                    c.suspect_address = $suspect_address,
                    c.updated_at = datetime(),
                    c.risk_score = $risk_score,
                    c.terminal_vasp = $vasp_name
            """, {
                "case_id": case_id,
                "chain": chain,
                "suspect_address": suspect_address,
                "risk_score": trace_data.get("composite_risk_score", 0),
                "vasp_name": vasp_name
            })

            # 2. Ingest Wallet nodes
            for n in nodes:
                addr = n.get("id") or n.get("address")
                if not addr:
                    continue
                session.run("""
                    MERGE (w:Wallet {address: $address})
                    SET w.chain = $chain,
                        w.label = $label,
                        w.type = $type,
                        w.hop = $hop,
                        w.balance = $balance,
                        w.risk_score = $risk_score,
                        w.last_seen = datetime()
                    WITH w
                    MATCH (c:Case {case_id: $case_id})
                    MERGE (c)-[:CONTAINS_NODE]->(w)
                """, {
                    "address": addr,
                    "chain": chain,
                    "label": n.get("label", ""),
                    "type": n.get("type", "wallet"),
                    "hop": n.get("hop", 0),
                    "balance": str(n.get("balance", "0")),
                    "risk_score": n.get("risk_score", 0),
                    "case_id": case_id
                })

            # 3. Ingest Transaction Relationships
            for e in edges:
                src = e.get("source") or e.get("from")
                tgt = e.get("target") or e.get("to")
                if not src or not tgt:
                    continue
                session.run("""
                    MATCH (s:Wallet {address: $src})
                    MATCH (t:Wallet {address: $tgt})
                    MERGE (s)-[r:TRANSFERRED {tx_hash: $tx_hash}]->(t)
                    SET r.amount = $amount,
                        r.asset = $asset,
                        r.hop = $hop,
                        r.timestamp = datetime()
                """, {
                    "src": src,
                    "tgt": tgt,
                    "tx_hash": e.get("tx_hash") or f"tx_{int(time.time())}_{src[:6]}_{tgt[:6]}",
                    "amount": float(re.sub(r'[^0-9.]', '', str(e.get("amount", 0))) or 0),
                    "asset": e.get("asset") or chain,
                    "hop": int(e.get("hop", 1))
                })

            # 4. Ingest Terminal VASP Entity and Link Deposit Address
            if vasp_name and nearest_vasp:
                deposit_addr = nearest_vasp.get("deposit_address")
                session.run("""
                    MERGE (v:VASP {name: $name})
                    SET v.vasp_type = $vasp_type,
                        v.country = $country,
                        v.nodal_email = $nodal_email,
                        v.is_fiu_compliant = $is_fiu_compliant,
                        v.registration = $registration,
                        v.last_updated = datetime()
                    WITH v
                    MATCH (c:Case {case_id: $case_id})
                    MERGE (c)-[:ATTRIBUTED_TO]->(v)
                """, {
                    "name": vasp_name,
                    "vasp_type": nearest_vasp.get("vasp_type", "Centralized Exchange"),
                    "country": nearest_vasp.get("country", "India"),
                    "nodal_email": nearest_vasp.get("nodal_email", "compliance@vasp.com"),
                    "is_fiu_compliant": bool(nearest_vasp.get("is_indian", True)),
                    "registration": nearest_vasp.get("registration", "PMLA Registered"),
                    "case_id": case_id
                })

                if deposit_addr:
                    session.run("""
                        MATCH (w:Wallet {address: $deposit_addr})
                        MATCH (v:VASP {name: $name})
                        MERGE (w)-[:DEPOSIT_GATEWAY_FOR]->(v)
                    """, {
                        "deposit_addr": deposit_addr,
                        "name": vasp_name
                    })

        return {
            "success": True,
            "case_id": case_id,
            "nodes_ingested": len(nodes),
            "edges_ingested": len(edges),
            "vasp_attributed": vasp_name,
            "cloud_status": "synced_to_neo4j_aura"
        }
    except Exception as e:
        logger.error(f"Neo4j sync error: {e}")
        return {"success": False, "error": str(e)}


def execute_cypher(query: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Execute raw Cypher query for custom forensic interrogation."""
    driver = get_driver()
    if not driver:
        return {"success": False, "error": "No Neo4j connection"}

    params = params or {}
    t0 = time.time()
    try:
        with driver.session() as session:
            result = session.run(query, params)
            keys = result.keys()
            records = []
            for record in result:
                row = {}
                for k in keys:
                    val = record[k]
                    # Format Neo4j types to JSON serializable
                    if hasattr(val, "id") and hasattr(val, "items"):
                        row[k] = dict(val.items())
                    elif hasattr(val, "nodes") and hasattr(val, "relationships"):
                        row[k] = f"Path(nodes={len(val.nodes)}, rels={len(val.relationships)})"
                    else:
                        row[k] = str(val)
                records.append(row)

        return {
            "success": True,
            "columns": list(keys),
            "count": len(records),
            "data": records[:100],  # Limit to 100 rows for security
            "execution_ms": round((time.time() - t0) * 1000, 1)
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "execution_ms": round((time.time() - t0) * 1000, 1)
        }