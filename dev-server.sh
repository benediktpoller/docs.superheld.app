#!/bin/bash

# Hugo Development Server Starter für superheld.app

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
HUGO_DIR="$SCRIPT_DIR/hugo-site"

if [ ! -d "$HUGO_DIR" ]; then
    echo "❌ Fehler: hugo-site/ Verzeichnis nicht gefunden"
    echo "Führen Sie dieses Skript vom Projekt-Stammverzeichnis aus"
    exit 1
fi

echo "🚀 Starte Hugo Development Server..."
echo "📂 Verzeichnis: $HUGO_DIR"
echo ""
echo "Hugo Server läuft unter: http://127.0.0.1:1313"
echo "Browser öffnet sich automatisch in wenigen Sekunden..."
echo ""
echo "Zum Stoppen: Ctrl+C drücken"
echo ""

cd "$HUGO_DIR"
hugo server --buildDrafts --disableFastRender -O
