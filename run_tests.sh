#!/bin/bash

# WCAG AAA Test Script für superheld.app Dokumentation
# Dieses Skript startet den Hugo Server und führt die Accessibility Tests durch

set -e

echo "================================"
echo "WCAG AAA Accessibility Tests"
echo "================================"
echo ""

# Prüfe, ob wir im richtigen Verzeichnis sind
if [ ! -d "hugo-site" ]; then
    echo "❌ Fehler: hugo-site/ Verzeichnis nicht gefunden"
    echo "Starten Sie dieses Skript aus dem Projekt-Stammverzeichnis"
    exit 1
fi

# Prüfe Python-Umgebung
if [ ! -d ".venv" ]; then
    echo "❌ Fehler: Python Virtual Environment nicht gefunden"
    echo "Erstellen Sie zuerst: python3 -m venv .venv"
    exit 1
fi

# Aktiviere venv
source .venv/bin/activate

# Installiere Requirements
echo "📦 Installiere Test-Abhängigkeiten..."
pip install -q -r tests/requirements.txt

# Starte Hugo Server im Hintergrund
echo "🚀 Starte Hugo Server..."
cd hugo-site
hugo server --buildDrafts &
HUGO_PID=$!
cd ..

# Warte kurz bis Server läuft
sleep 3

echo ""
echo "🧪 Führe Accessibility Tests durch..."
echo ""

# Führe Tests durch
python -m pytest tests/test_wcag_aaa.py -v --tb=short

TEST_RESULT=$?

# Räume auf - stoppe Hugo Server
echo ""
echo "🛑 Stoppe Hugo Server..."
kill $HUGO_PID 2>/dev/null || true
wait $HUGO_PID 2>/dev/null || true

echo ""
echo "================================"
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ Alle Tests bestanden!"
else
    echo "❌ Einige Tests fehlgeschlagen"
fi
echo "================================"

exit $TEST_RESULT
