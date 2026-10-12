# CHRONOSCOUTS: SYSTEM SITREP & PRODUCT SPEC
Owner: K. Michael Talbert (Bleak / BleakNarratives)
Repository: BleakNarratives/ChronoScouts
Target Environment: Termux / Android (Samsung A9)
Status: Core Engine & RAG Indexing Live

## 1. Executive Summary
ChronoScouts is a sovereign, headless multi-agent swarm that crawls SEC EDGAR filings and financial market feeds. It extracts operational distress indicators, debt covenant breaches, and liquidity strains, normalizes payloads, and indexes data into a persistent SQLite FTS5 store (scout_rag_store.db).

## 2. Ingestion & Execution Loop
fixtures/market_signals.json -> harnesses/scout_runner.py -> dist/Executive_Digest_Sample.md
