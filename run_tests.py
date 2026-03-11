#!/usr/bin/env python3
"""
WCAG AAA Accessibility Test Runner
Startet Hugo Server und führt automatisierte Tests durch
"""

import subprocess
import sys
import time
import os
from pathlib import Path
import signal
import platform

def main():
    print("=" * 70)
    print("WCAG AAA Accessibility Test Suite")
    print("=" * 70)
    print()

    # Prüfe Hugo-Verzeichnis
    hugo_dir = Path("hugo-site")
    if not hugo_dir.exists():
        print("❌ Fehler: hugo-site/ Verzeichnis nicht gefunden")
        print("Führen Sie dieses Skript vom Projekt-Stammverzeichnis aus")
        sys.exit(1)

    # Prüfe venv
    venv_dir = Path(".venv")
    if not venv_dir.exists():
        print("❌ Fehler: Virtual Environment nicht gefunden")
        print("Erstelle zuerst: python3 -m venv .venv")
        sys.exit(1)

    # Installiere Requirements
    print("📦 Installiere Test-Abhängigkeiten...")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", "-r", "tests/requirements.txt"],
        check=True
    )

    # Starte Hugo Server
    print("🚀 Starte Hugo Server...")
    os.chdir(hugo_dir)
    
    hugo_process = subprocess.Popen(
        ["hugo", "server", "--buildDrafts"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    os.chdir("..")
    
    # Warte bis Server läuft
    time.sleep(3)

    try:
        print("🧪 Führe Accessibility Tests durch...")
        print()

        # Starte Tests
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/test_wcag_aaa.py", "-v", "--tb=short"],
            cwd="."
        )

        print()
        print("=" * 70)
        if result.returncode == 0:
            print("✅ Alle Tests bestanden!")
        else:
            print("❌ Einige Tests fehlgeschlagen")
        print("=" * 70)

        return result.returncode

    finally:
        # Stoppe Hugo Server
        print()
        print("🛑 Stoppe Hugo Server...")
        if platform.system() == "Windows":
            hugo_process.terminate()
        else:
            os.killpg(os.getpgid(hugo_process.pid), signal.SIGTERM)
        
        try:
            hugo_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            hugo_process.kill()


if __name__ == "__main__":
    sys.exit(main())
