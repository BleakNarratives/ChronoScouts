# ChronoScouts (RootBase Fabric)
> Autonomous SEC EDGAR & Time-Series Market Distress Signal Intelligence Engine

ChronoScouts is a sovereign, headless multi-agent swarm that crawls SEC EDGAR filings and market feeds to detect operational distress, debt covenant breaches, and liquidity strains in real time.

## Architecture
    * Ingestion Layer: Headless Python scrapers emitting normalized JSON feeds (fixtures/market_signals.json).
    * Harness & Normalization: harnesses/scout_runner.py with ChronoScout adapters.
    * Storage & RAG: Persistent SQLite FTS5 database (scout_rag_store.db).
    * Artifact Delivery: Executive Signal Briefings rendered to dist/index.html and dist/Executive_Digest_Sample.md.

## Execution
    python3 harnesses/scout_runner.py
