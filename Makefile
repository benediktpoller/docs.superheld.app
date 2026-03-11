# superheld.app documentation Makefile

.PHONY: help server dev test test-watch build build-minify clean install ci

help:
	@echo "superheld.app Dokumentation - Makefile Commands"
	@echo ""
	@echo "Development:"
	@echo "  make dev              Starte Hugo Development Server"
	@echo "  make test             Führe WCAG AAA Tests durch"
	@echo "  make test-watch       Führe Tests mit Watch aus"
	@echo ""
	@echo "Build:"
	@echo "  make build            Baue Hugo Site"
	@echo "  make build-minify     Baue minified Site (Production)"
	@echo ""
	@echo "Setup:"
	@echo "  make install          Installiere Dependencies"
	@echo ""
	@echo "Maintenance:"
	@echo "  make clean            Räume auf (caches, build output)"
	@echo "  make lint             Führe Content Validierung durch"

# Development
dev:
	@cd hugo-site && hugo server --buildDrafts --disableFastRender -O

server:
	@cd hugo-site && hugo server --buildDrafts --disableFastRender

# Testing
test:
	@python run_tests.py

test-watch:
	@python -m pytest tests/test_wcag_aaa.py -v --tb=short --watch

# Build
build:
	@echo "🔨 Baue Hugo Site..."
	@cd hugo-site && hugo
	@echo "✅ Build abgeschlossen in hugo-site/public/"

build-minify:
	@echo "🔨 Baue minified Hugo Site..."
	@cd hugo-site && hugo --minify
	@echo "✅ Minified build abgeschlossen in hugo-site/public/"

# Setup
install:
	@echo "📦 Installiere Dependencies..."
	@pip install -r tests/requirements.txt
	@echo "✅ Installation abgeschlossen"

# Maintenance
clean:
	@echo "🧹 Räume auf..."
	@rm -rf hugo-site/resources/_gen/
	@rm -rf hugo-site/public/
	@rm -rf .pytest_cache/
	@rm -rf __pycache__/
	@find . -type d -name __pycache__ -exec rm -rf {} +
	@echo "✅ Cleanup abgeschlossen"

lint:
	@echo "🔍 Validiere Content..."
	@find hugo-site/content -name "*.md" -exec grep -l "^##  " {} \; | wc -l | xargs echo "Überschriften mit doppeltem Space:"
	@echo "✅ Lint abgeschlossen"

# CI/CD Local Simulation
ci: clean install build-minify test
	@echo "✅ Alle CI/CD Checks bestanden!"

.DEFAULT_GOAL := help
