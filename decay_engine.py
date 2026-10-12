#!/usr/bin/env python3
"""
decay_engine.py — ChronoScouts Temporal Decay Engine
Formula: S_decayed = S_base * e^(-lambda * t_hours)
"""

import math, os, sqlite3, time

DB_PATH = "scout_rag_store.db"
HALF_LIFE_HOURS = 72.0
LAMBDA = math.log(2) / HALF_LIFE_HOURS

def apply_temporal_decay():
    if not os.path.exists(DB_PATH):
        print(f"[!] Database {DB_PATH} not found. Run scout_runner.py first.")
        return

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, domain, title, content, scraped_at FROM scraped_knowledge")
    rows = cur.fetchall()
    now = time.time()

    print(f"[*] Applying ChronoScouts Decay Filter to {len(rows)} signals...")
    for r in rows:
        sig_id, domain, title, content, scraped_at = r
        age_hours = (now - scraped_at) / 3600.0
        base_confidence = 0.85
        decayed_conf = base_confidence * math.exp(-LAMBDA * age_hours)
        print(f"  • [{domain}] Age: {round(age_hours, 2)}h | Decayed Confidence: {round(decayed_conf, 2)}")
    
    conn.close()

if __name__ == "__main__":
    apply_temporal_decay()
