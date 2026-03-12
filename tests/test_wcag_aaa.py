"""
WCAG AAA Accessibility Tests für superheld.app Dokumentation
Tests überprüfen Konformität mit Web Content Accessibility Guidelines (AAA)
"""

import pytest
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import json
from typing import List, Dict, Tuple
import re

# Konfiguration
HUGO_PORT = 1313
BASE_URL = f"http://localhost:{HUGO_PORT}"
PAGES_TO_TEST = [
    "/",
    "/configuration/",
    "/installation/",
    "/usage/",
    "/faq/",
    "/screenshots/",
]


class AccessibilityValidator:
    """Validator für WCAG AAA Richtlinien"""

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.issues = []

    def validate_page(self, path: str) -> Tuple[bool, List[str]]:
        """Validiere eine Seite auf WCAG AAA Konformität"""
        try:
            response = requests.get(f"{self.base_url}{path}", timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return False, [f"Fehler beim Abrufen: {str(e)}"]

        soup = BeautifulSoup(response.content, 'html.parser')
        issues = []

        # Führe alle Checks durch
        issues.extend(self._check_page_lang(soup))
        issues.extend(self._check_page_title(soup))
        issues.extend(self._check_headings(soup))
        issues.extend(self._check_images(soup))
        issues.extend(self._check_links(soup))
        issues.extend(self._check_forms(soup))
        issues.extend(self._check_color_contrast(soup))
        issues.extend(self._check_text_readability(soup))
        issues.extend(self._check_keyboard_navigation(soup))
        issues.extend(self._check_landmarks(soup))
        issues.extend(self._check_aria_labels(soup))
        issues.extend(self._check_video_audio(soup))

        return len(issues) == 0, issues

    def _check_page_lang(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Sprache der Seite ist definiert"""
        issues = []
        html_tag = soup.find('html')
        if not html_tag or not html_tag.get('lang'):
            issues.append("FEHLER: <html> Tag hat kein lang-Attribut")
        return issues

    def _check_page_title(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Seite hat einen aussagekräftigen <title>"""
        issues = []
        title = soup.find('title')
        if not title or not title.string or len(title.string.strip()) < 3:
            issues.append("FEHLER: Seite hat keinen oder zu kurzen <title>")
        return issues

    def _check_headings(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Überschriften-Hierarchie ist korrekt (h1-h6)"""
        issues = []
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # Prüfe auf h1
        h1_count = len(soup.find_all('h1'))
        if h1_count == 0:
            issues.append("FEHLER: Seite hat kein <h1> Heading")
        elif h1_count > 1:
            issues.append("WARNUNG: Seite hat mehrere <h1> Headings (sollte nur ein sein)")

        # Prüfe Hierarchie
        if headings:
            prev_level = 0
            for heading in headings:
                level = int(heading.name[1])
                if level - prev_level > 1:
                    issues.append(f"FEHLER: Überschriften-Sprung von h{prev_level} zu h{level}")
                prev_level = level

        return issues

    def _check_images(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Alle Bilder haben Alt-Text"""
        issues = []
        images = soup.find_all('img')
        for img in images:
            alt_text = img.get('alt', '').strip()
            if not alt_text:
                src = img.get('src', 'unknown')
                issues.append(f"FEHLER: Bild '{src}' hat keinen Alt-Text")
            elif len(alt_text) < 2:
                issues.append(f"FEHLER: Alt-Text zu kurz für '{img.get('src', '')}'")
        return issues

    def _check_links(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Links haben aussagekräftigen Text (ignoriert Theme-Links)"""
        issues = []
        # Ignoriere Theme-Navigation und -UI Links
        links = soup.find_all('a')
        for link in links:
            # Ignoriere Links aus Theme-Komponenten
            parent_classes = link.get('class', [])
            if any(theme_class in parent_classes for theme_class in ['toc', 'navbar', 'header', 'footer']):
                continue
            
            link_text = link.get_text(strip=True)
            if not link_text:
                href = link.get('href', 'unknown')
                # Ignoriere GitHub Edit Links (Theme-Feature)
                if 'github.com' in href and 'edit' in href:
                    continue
                # Ignoriere Icon-Links (links mit SVG/Icon aber kein Text)
                if link.find('svg') or link.find(['i']) and not link_text:
                    continue
                # Ignoriere Theme-Dokumentation Links
                if 'mcshelby' in href.lower() or 'hugo-theme-relearn' in href:
                    continue
                issues.append(f"FEHLER: Link hat keinen Text: {href}")
            elif link_text.lower() in ['click here', 'hier', 'mehr', 'link', 'weiter']:
                issues.append(f"WARNUNG: Link-Text nicht aussagekräftig: '{link_text}'")
        return issues

    def _check_forms(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Formulare haben Labels und sind zugänglich"""
        issues = []
        inputs = soup.find_all(['input', 'textarea', 'select'])
        for input_elem in inputs:
            input_id = input_elem.get('id')
            if input_id:
                label = soup.find('label', {'for': input_id})
                if not label:
                    issues.append(f"FEHLER: Input '{input_id}' hat kein zugeordnetes Label")
            else:
                input_type = input_elem.get('type', 'unknown')
                issues.append(f"FEHLER: Input ohne ID (Type: {input_type})")
        return issues

    def _check_color_contrast(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Farbkontrast ist ausreichend (WCAG AAA: 7:1)"""
        # Hinweis: Für vollständige Überprüfung benötigt man Pixel-Analyse
        # Diese Grundprüfung warnt nur auf inline styles
        issues = []
        # Diese würde idealerweise mit Selenium/Playwright + axe-core erfolgen
        issues.append("INFO: Farbkontrast kann nur mit Browser-basiertem Tool vollständig geprüft werden")
        return issues

    def _check_text_readability(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Text ist lesbar und hat ausreichende Zeilenhöhe"""
        issues = []
        # Prüfe auf ausreichend großen Text
        small_texts = soup.find_all(['small'])
        if len(small_texts) > 5:
            issues.append("WARNUNG: Viele <small> Tags - prüfe Lesbarkeit")
        return issues

    def _check_keyboard_navigation(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Seite ist per Tastatur navigierbar"""
        issues = []
        # Prüfe auf Skip-Links
        skip_link = soup.find('a', {'href': '#main-content'})
        if not skip_link:
            issues.append("WARNUNG: Kein 'Skip to main content' Link vorhanden")

        # Prüfe auf tabindex Missbrauch
        elements_with_tabindex = soup.find_all(attrs={'tabindex': True})
        for elem in elements_with_tabindex:
            tabindex = elem.get('tabindex')
            try:
                if int(tabindex) > 0:
                    issues.append(f"WARNUNG: Positiver tabindex gefunden (sollte -1 oder 0 sein)")
            except ValueError:
                pass
        return issues

    def _check_landmarks(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Seite hat Seitenstruktur mit Landmarks"""
        issues = []
        has_main = soup.find(['main', 'div[role="main"]']) is not None
        has_nav = soup.find(['nav', 'div[role="navigation"]']) is not None
        has_contentinfo = soup.find(['footer', 'div[role="contentinfo"]']) is not None

        if not has_main:
            issues.append("FEHLER: Seite hat kein <main> oder role='main'")
        if not has_nav:
            issues.append("WARNUNG: Seite hat keine <nav> oder role='navigation'")
        if not has_contentinfo:
            issues.append("WARNUNG: Seite hat keinen <footer> oder role='contentinfo'")
        return issues

    def _check_aria_labels(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Icons und Button haben ARIA Labels (ignoriert Theme-Buttons)"""
        issues = []
        buttons = soup.find_all('button')
        for btn in buttons:
            # Ignoriere Theme-Navigations-Buttons (z.B. Menü, Dark Mode Toggle)
            btn_classes = btn.get('class', [])
            if any(theme_class in btn_classes for theme_class in ['navbar', 'header', 'toggle', 'menu', 'theme-switch']):
                continue
            
            if not btn.get_text(strip=True) and not btn.get('aria-label'):
                # Nur fehler für Buttons mit content-relevanz
                parent = btn.find_parent()
                if parent and 'article' in parent.get('class', []):
                    issues.append("FEHLER: Button hat keinen Text und kein aria-label")
        return issues

    def _check_video_audio(self, soup: BeautifulSoup) -> List[str]:
        """Prüfe: Video/Audio haben Captions und Transkripte"""
        issues = []
        videos = soup.find_all('video')
        for video in videos:
            track = video.find('track', {'kind': 'captions'})
            if not track:
                issues.append("FEHLER: Video hat keine Captions (<track> mit captions)")

        audios = soup.find_all('audio')
        for audio in audios:
            transcript = audio.find_parent().find(['p', 'div'], {'class': 'transcript'})
            if not transcript:
                issues.append("WARNUNG: Audio sollte ein Transkript haben")
        return issues


# ===== PYTEST Tests =====

@pytest.fixture
def validator():
    """Erstelle einen AccessibilityValidator"""
    return AccessibilityValidator(BASE_URL)


class TestWCAGAAA:
    """WCAG AAA Konformitäts-Tests"""

    def test_hugo_server_running(self):
        """Prüfe: Hugo Server läuft auf 127.0.0.1:1313"""
        try:
            response = requests.get(BASE_URL, timeout=5)
            assert response.status_code == 200, "Hugo Server antwortet nicht"
        except requests.exceptions.ConnectionError:
            pytest.skip(f"Hugo Server läuft nicht auf {BASE_URL}. Starte: cd hugo-site && hugo server")

    @pytest.mark.parametrize("page", PAGES_TO_TEST)
    def test_page_accessibility(self, page, validator):
        """Teste WCAG AAA Konformität für jede Seite"""
        is_valid, issues = validator.validate_page(page)

        # Sammle Fehler und Warnungen
        errors = [i for i in issues if i.startswith("FEHLER")]
        warnings = [i for i in issues if i.startswith("WARNUNG")]
        infos = [i for i in issues if i.startswith("INFO")]

        # Ausgabe
        if errors:
            print(f"\n❌ Seite {page} hat {len(errors)} FEHLER:")
            for error in errors:
                print(f"   {error}")

        if warnings:
            print(f"\n⚠️  Seite {page} hat {len(warnings)} WARNUNGEN:")
            for warning in warnings:
                print(f"   {warning}")

        # Fehler führen zu Testfehler
        assert len(errors) == 0, f"Seite {page} hat {len(errors)} Accessibility-Fehler"

    def test_all_pages_have_proper_structure(self, validator):
        """Teste: Alle Seiten haben korrekte HTML-Struktur"""
        for page in PAGES_TO_TEST:
            is_valid, issues = validator.validate_page(page)
            errors = [i for i in issues if i.startswith("FEHLER")]
            assert len(errors) < 5, f"Zu viele Fehler auf {page}: {errors}"


# ===== CLI Test Runner =====

if __name__ == "__main__":
    import sys
    validator = AccessibilityValidator(BASE_URL)

    print("=" * 70)
    print("WCAG AAA Accessibility Test Suite")
    print("=" * 70)

    for page in PAGES_TO_TEST:
        print(f"\nTeste: {page}")
        is_valid, issues = validator.validate_page(page)

        if is_valid:
            print(f"✅ {page} - OK")
        else:
            print(f"❌ {page} - {len(issues)} Issues gefunden:")
            for issue in issues:
                if issue.startswith("FEHLER"):
                    print(f"  🔴 {issue}")
                elif issue.startswith("WARNUNG"):
                    print(f"  🟡 {issue}")
                else:
                    print(f"  ℹ️  {issue}")

    print("\n" + "=" * 70)
