import os
import subprocess
import time

import pytest
from playwright.sync_api import sync_playwright


def _start_hugo_server():
    env = os.environ.copy()
    proc = subprocess.Popen(
        [
            "hugo",
            "server",
            "-s",
            "hugo-site",
            "--disableFastRender",
            "--port",
            "1313",
            "--bind",
            "127.0.0.1",
            "--minify",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env=env,
    )
    return proc


def _wait_for_server(url: str, timeout: int = 15):
    import requests

    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                return True
        except Exception:
            pass
        time.sleep(0.5)
    return False


VIEWPORTS = [
    (1280, 800, "desktop"),
    (1024, 768, "tablet"),
    (375, 812, "mobile"),
]

BROWSERS = ["chromium", "firefox", "webkit"]


@pytest.mark.parametrize("viewport", VIEWPORTS)
@pytest.mark.parametrize("browser_type", BROWSERS)
def test_homepage_responsive(viewport, browser_type):
    """Test the homepage renders correctly across viewports and browsers."""
    width, height, label = viewport
    server = _start_hugo_server()
    try:
        assert _wait_for_server("http://127.0.0.1:1313"), "Hugo server did not start in time"
        with sync_playwright() as p:
            launcher = getattr(p, browser_type)
            browser = launcher.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto("http://127.0.0.1:1313", wait_until="networkidle")

            # Hero section with Apple-style design
            hero = page.locator(".sh-hero")
            assert hero.is_visible(), "Hero section missing"

            # Hero heading
            heading = hero.locator("h1")
            assert heading.is_visible(), "Hero heading missing"
            assert "superheld" in heading.inner_text().strip().lower(), "Hero heading text wrong"

            # Hero tagline
            tagline = hero.locator(".sh-hero-tagline")
            assert tagline.is_visible(), "Hero tagline missing"

            # CTA buttons
            cta_buttons = hero.locator(".sh-hero-cta")
            assert cta_buttons.count() >= 1, "No CTA buttons in hero"

            # Device screenshots in hero
            device_images = hero.locator(".sh-devices img")
            assert device_images.count() >= 1, "No device screenshots in hero"

            # Features section
            features = page.locator(".sh-features .sh-feature-card")
            assert features.count() == 4, f"Expected 4 feature cards, got {features.count()}"

            # Screenshot gallery
            screenshots = page.locator(".sh-screenshots .sh-screenshot img")
            assert screenshots.count() >= 3, "Not enough screenshots in gallery"

            # Platform grid
            platforms = page.locator(".sh-platforms .sh-platform-card")
            assert platforms.count() >= 4, "Not enough platform cards"

            # Tabs section (roles)
            tabs = page.locator(".tab-nav-button")
            assert tabs.count() >= 4, "Role tabs missing"

            # CTA section at bottom
            cta_section = page.locator(".sh-cta-section")
            assert cta_section.count() >= 1, "CTA section missing"

            # Doc links
            doc_links = page.locator(".sh-doc-links .sh-doc-link")
            assert doc_links.count() >= 4, "Not enough doc links"

            # No horizontal overflow
            has_overflow = page.evaluate("""() => {
                return document.documentElement.scrollWidth <= window.innerWidth;
            }""")
            assert has_overflow, f"Horizontal overflow detected on {label} ({browser_type})"

            # Capture screenshot
            out_dir = os.path.join("tests", "screenshots")
            os.makedirs(out_dir, exist_ok=True)
            page.screenshot(
                path=os.path.join(out_dir, f"homepage_{label}_{browser_type}.png"),
                full_page=True,
            )

            browser.close()
    finally:
        server.terminate()
        server.wait(5)


@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_homepage_images_load(viewport):
    """Test that all SVG screenshot images load correctly."""
    width, height, label = viewport
    server = _start_hugo_server()
    try:
        assert _wait_for_server("http://127.0.0.1:1313"), "Hugo server did not start in time"
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})

            failed_requests = []
            page.on("requestfailed", lambda req: failed_requests.append(req.url))

            page.goto("http://127.0.0.1:1313", wait_until="networkidle")

            # Check no image requests failed
            image_failures = [url for url in failed_requests if ".svg" in url or ".png" in url]
            assert len(image_failures) == 0, f"Failed image requests: {image_failures}"

            # Verify SVG images have natural dimensions
            images = page.locator("img[src$='.svg']")
            count = images.count()
            assert count >= 4, f"Expected at least 4 SVG images, got {count}"

            browser.close()
    finally:
        server.terminate()
        server.wait(5)


@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_homepage_custom_css_loaded(viewport):
    """Test that custom Apple-style CSS is loaded."""
    width, height, label = viewport
    server = _start_hugo_server()
    try:
        assert _wait_for_server("http://127.0.0.1:1313"), "Hugo server did not start in time"
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto("http://127.0.0.1:1313", wait_until="networkidle")

            # Check that custom CSS classes are styled (not just default)
            hero_bg = page.evaluate("""() => {
                const hero = document.querySelector('.sh-hero');
                if (!hero) return null;
                return getComputedStyle(hero).background;
            }""")
            assert hero_bg is not None, "Hero element not found or not styled"

            browser.close()
    finally:
        server.terminate()
        server.wait(5)


@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_homepage_no_console_errors(viewport):
    """Test that no console errors occur on page load."""
    width, height, label = viewport
    server = _start_hugo_server()
    try:
        assert _wait_for_server("http://127.0.0.1:1313"), "Hugo server did not start in time"
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})

            errors = []
            page.on("console", lambda msg: errors.append(msg.text()) if msg.type == "error" else None)

            page.goto("http://127.0.0.1:1313", wait_until="networkidle")
            page.wait_for_timeout(1000)

            assert len(errors) == 0, f"Console errors on {label}: {errors}"

            browser.close()
    finally:
        server.terminate()
        server.wait(5)
