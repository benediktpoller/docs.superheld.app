#!/bin/bash
#
# Lokale Workflow-Validierung
# Simuliert die GitHub Actions Workflows lokal
#

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Lokale GitHub Actions Workflow Validierung"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Farben
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Fehler-Zähler
FAILED=0

# 1. Hugo Build Test
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣  Hugo Build (wie in build-deploy.yml)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

cd hugo-site
if hugo --minify 2>&1 | grep -q "ERROR\|error"; then
  echo -e "${RED}❌ Hugo Build fehlgeschlagen${NC}"
  FAILED=$((FAILED+1))
else
  echo -e "${GREEN}✅ Hugo Build erfolgreich${NC}"
fi
cd ..

# 2. Python Dependencies
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2️⃣  Python Dependencies (wie in accessibility.yml)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

source .venv/bin/activate 2>/dev/null || {
  echo -e "${YELLOW}⚠️  venv nicht aktiviert, aktiviere...${NC}"
  python3 -m venv .venv
  source .venv/bin/activate
}

if pip install -r tests/requirements.txt -q 2>&1; then
  echo -e "${GREEN}✅ Dependencies installiert${NC}"
else
  echo -e "${RED}❌ Dependencies Installation fehlgeschlagen${NC}"
  FAILED=$((FAILED+1))
fi

# 3. Hugo Server starten
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3️⃣  Hugo Server Start (wie in accessibility.yml)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Töte alte Hugo Server Prozesse
pkill -f "hugo server" 2>/dev/null || true
sleep 1

# Starte neuen Hugo Server
cd hugo-site
hugo server --buildDrafts &>/dev/null &
HUGO_PID=$!
cd ..
sleep 3

if curl -s http://localhost:1313 > /dev/null 2>&1; then
  echo -e "${GREEN}✅ Hugo Server läuft auf http://localhost:1313${NC}"
else
  echo -e "${RED}❌ Hugo Server startet nicht${NC}"
  kill $HUGO_PID 2>/dev/null || true
  FAILED=$((FAILED+1))
fi

# 4. WCAG AAA Tests
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  WCAG AAA Accessibility Tests"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if python -m pytest tests/test_wcag_aaa.py -v --tb=short 2>&1 | tee /tmp/test-output.txt | tail -20; then
  TEST_RESULT=0
else
  TEST_RESULT=$?
fi

# Zähle bestandene/fehlgeschlagene Tests
PASSED=$(grep -c "PASSED" /tmp/test-output.txt 2>/dev/null || echo 0)
FAILED_TESTS=$(grep -c "FAILED" /tmp/test-output.txt 2>/dev/null || echo 0)

if [ $TEST_RESULT -eq 0 ]; then
  echo -e "${GREEN}✅ Alle $PASSED Tests bestanden${NC}"
else
  echo -e "${RED}❌ $FAILED_TESTS Tests fehlgeschlagen, $PASSED bestanden${NC}"
  FAILED=$((FAILED+1))
fi

# 5. Zusammenfassung
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Zusammenfassung"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Cleanup
pkill -f "hugo server" 2>/dev/null || true

if [ $FAILED -eq 0 ]; then
  echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${GREEN}✅ ALLE WORKFLOWS VALIDIERT - Ready für GitHub Actions!${NC}"
  echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  exit 0
else
  echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  echo -e "${RED}❌ $FAILED Validierungen fehlgeschlagen${NC}"
  echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
  exit 1
fi
