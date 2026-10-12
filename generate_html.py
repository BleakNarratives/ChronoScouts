#!/usr/bin/env python3
import json, os, time

fixture_path = "fixtures/market_signals.json"
output_path = "dist/index.html"
os.makedirs("dist", exist_ok=True)

if os.path.exists(fixture_path):
    with open(fixture_path, "r", encoding="utf-8") as f:
        signals = json.load(f)
    
    rows = ""
    for s in signals:
        ticker = s.get("ticker", "N/A")
        sev = s.get("severity", "INFO")
        conf = s.get("confidence", "0.0")
        summary = s.get("summary", "No details")
        flags = ", ".join(s.get("signals", []))
        
        badge_bg = "#7f1d1d" if sev == "CRITICAL" else "#78350f"
        badge_fg = "#fca5a5" if sev == "CRITICAL" else "#fde047"

        rows += f"""
        <div style="background:#121826; border:1px solid #1e293b; padding:16px; margin-bottom:12px; border-radius:8px;">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <span style="font-weight:bold; font-size:18px; color:#f8fafc;">{ticker}</span>
                <span style="background:{badge_bg}; color:{badge_fg}; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:bold;">{sev}</span>
                <span style="color:#38bdf8; font-size:13px;">Confidence: {conf}</span>
            </div>
            <div style="margin:8px 0; color:#cbd5e1;">{summary}</div>
            <div style="font-size:13px; color:#64748b;"><strong>Flags:</strong> {flags}</div>
        </div>"""

    html_content = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>ChronoScouts Executive Telemetry</title>
    </head>
    <body style="background:#0b0f19; color:#e2e8f0; font-family:-apple-system, sans-serif; padding:20px; max-width:800px; margin:0 auto;">
        <h1 style="color:#00ffcc; border-bottom:2px solid #1e293b; padding-bottom:10px;">CHRONOSCOUTS: EXECUTIVE BRIEFING</h1>
        <div style="color:#94a3b8; margin-bottom:20px;">Generated: {time.strftime('%b %d, %Y - %H:%M UTC')} | SEC EDGAR & Market Telemetry</div>
        {rows}
        <div style="text-align:center; margin-top:30px; font-size:12px; color:#475569;">
            Powered by ChronoScouts & RootBase Sovereign Intelligence
        </div>
    </body>
    </html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[+] Client HTML briefing written to {output_path}")
