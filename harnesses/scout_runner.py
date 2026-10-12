#!/usr/bin/env python3
"""
scout_runner.py — ChronoScouts Engine
Connects ChronoScouts schema, SQLite FTS5 RAG store, and SEC EDGAR telemetry.
"""

import os
import sys
import json
import sqlite3
import time

sys.path.insert(0, os.path.abspath("."))

DB_PATH = "scout_rag_store.db"

def init_rag_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS scraped_knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT,
            title TEXT,
            content TEXT,
            scraped_at REAL
        )
    """)
    cur.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS knowledge_fts
        USING fts5(domain UNINDEXED, title, content);
    """)
    conn.commit()
    conn.close()

def safe_load_signals(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else data.get("targets", [])
    except Exception as e:
        print(f"[!] Warning parsing {file_path}: {e}")
        return []

def archive_signals(signals):
    if not signals: return 0
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    count = 0
    for s in signals:
        try:
            ticker = s.get("ticker", s.get("entity", "UNKNOWN"))
            severity = s.get("severity", "INFO")
            content = json.dumps(s)
            cur.execute("""
                INSERT INTO scraped_knowledge (domain, title, content, scraped_at)
                VALUES (?, ?, ?, ?)
            """, (ticker, f"ChronoScout Signal [{severity}]", content, time.time()))
            count += 1
        except Exception as e:
            print(f"[!] Archival error: {e}")
    conn.commit()
    conn.close()
    return count

def run_harness():
    init_rag_db()
    print("=== ChronoScouts Engine Active ===")
    fixture_path = "fixtures/market_signals.json"
    signals = safe_load_signals(fixture_path)
    if signals:
        archived = archive_signals(signals)
        print(f"[+] Ingested {len(signals)} signals from {fixture_path}")
        print(f"[+] Archived {archived} records into {DB_PATH}")
    else:
        print("[*] No active signals found.")

if __name__ == "__main__":
    run_harness()
