#!/usr/bin/env python3
"""
Hugo Development Server Starter
Startet den Hugo server aus dem richtigen Verzeichnis
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    # Bestimme das Projekt-Stammverzeichnis
    script_dir = Path(__file__).parent.absolute()
    hugo_dir = script_dir / "hugo-site"
    
    if not hugo_dir.exists():
        print("❌ Fehler: hugo-site/ Verzeichnis nicht gefunden")
        print(f"Stelle sicher, dass du dieses Skript von {script_dir} ausführst")
        sys.exit(1)
    
    print("🚀 Starte Hugo Development Server...")
    print(f"📂 Verzeichnis: {hugo_dir}")
    print()
    print("Hugo Server läuft unter: http://127.0.0.1:1313")
    print("Browser öffnet sich automatisch...")
    print()
    print("Zum Stoppen: Ctrl+C drücken")
    print()
    
    # Wechsle zum Hugo-Verzeichnis
    os.chdir(hugo_dir)
    
    # Starte Hugo mit den richtigen Optionen
    try:
        subprocess.run(
            [
                "hugo",
                "server",
                "--buildDrafts",
                "--disableFastRender",
                "-O"  # Öffne Browser automatisch
            ],
            check=True
        )
    except FileNotFoundError:
        print("❌ Fehler: Hugo nicht gefunden")
        print("Installiere Hugo: brew install hugo (macOS) oder siehe https://gohugo.io/installation/")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Hugo Server beendet")
        sys.exit(0)

if __name__ == "__main__":
    main()
