#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════
#   SAHYOG Blockchain Intelligence & VASP Attribution Engine — Start Script
# ═══════════════════════════════════════════════════════════════════════════
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT=8765

echo ""
echo "  ██████╗  █████╗ ██╗  ██╗██╗   ██╗ ██████╗  ██████╗ "
echo "  ██╔══██╗██╔══██╗██║  ██║╚██╗ ██╔╝██╔═══██╗██╔════╝ "
echo "  ███████║███████║███████║ ╚████╔╝ ██║   ██║██║  ███╗"
echo "  ██╔════╝██╔══██║██╔══██║  ╚██╔╝  ██║   ██║██║   ██║"
echo "  ██║     ██║  ██║██║  ██║   ██║   ╚██████╔╝╚██████╔╝"
echo "  ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ "
echo ""
echo "  Blockchain Intelligence & VASP Attribution Engine v2.0"
echo "  Ministry of Home Affairs | Government of India"
echo "  ───────────────────────────────────────────────────────"

# Check port
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "  [!] Port $PORT already in use. Killing old process..."
    lsof -ti:$PORT | xargs kill -9 2>/dev/null
    sleep 1
fi

echo "  [+] Starting FastAPI backend on port $PORT..."
cd "$DIR"
python3 -m uvicorn app:app --host 0.0.0.0 --port $PORT --reload > /tmp/sahyog-engine.log 2>&1 &
sleep 2

if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "  [✓] Engine running at: http://localhost:$PORT"
    echo "  [✓] API docs:          http://localhost:$PORT/docs"
    echo ""
    echo "  [+] Opening dashboard in browser..."
    xdg-open "http://localhost:$PORT" 2>/dev/null || \
    sensible-browser "http://localhost:$PORT" 2>/dev/null || \
    python3 -m webbrowser "http://localhost:$PORT"
else
    echo "  [!] Engine failed to start. Check: /tmp/sahyog-engine.log"
    tail -20 /tmp/sahyog-engine.log
fi
