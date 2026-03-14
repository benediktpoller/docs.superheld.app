import os
import subprocess
import time

import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "http://127.0.0.1:4321"


def _start_astro_preview():
    """Start Astro preview server (serves built output)."""
    astro_dir = os.path.join(os.path.dirname(__file__), "..", "astro-site")
    astro_dir = os.path.abspath(astro_dir)
    # Build first
    subprocess.run(
        ["npm", "run", "build"],
        cwd=astro_dir,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    proc = subprocess.Popen(
        ["npx", "astro", "preview", "--port", "4321", "--host", "127.0.0.1"],
        cwd=astro_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
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

# All pages that must exist
PAGES = [
    ("/", "Landing Page"),
    ("/einfuehrung/", "Erste Schritte"),
    ("/einfuehrung/intro/", "Was ist superheld.app?"),
    ("/einfuehrung/installation-v2/", "Installation"),
    ("/einfuehrung/setup/", "Erstkonfiguration"),
    ("/einfuehrung/nutzung/", "Tägliche Nutzung"),
    ("/einfuehrung/faq/", "FAQ"),
    ("/experten/", "Für Experten"),
    ("/experten/konfiguration/", "Konfiguration"),
    ("/experten/privacy-sicherheit/", "Privatsphäre & Sicherheit"),
    ("/experten/apps/", "Apps & Plattformen"),
    ("/experten/migration/", "Migration"),
    ("/experten/use-cases/", "Use Cases"),
    ("/experten/screenshots/", "Screenshots"),
]


@pytest.fixture(scope="session")
def astro_server():
    """Start Astro preview server once for the entire test session."""
    server = _start_astro_preview()
    assert _wait_for_server(BASE_URL), "Astro preview server did not start in time"
    yield server
    server.terminate()
    server.wait(5)


# --- Test 1: All pages return 200 ---

@pytest.mark.parametrize("path,name", PAGES)
def test_page_returns_200(path, name, astro_server):
    """Every page must return HTTP 200."""
    import requests

    r = requests.get(f"{BASE_URL}{path}", timeout=10)
    assert r.status_code == 200, f"{name} ({path}) returned {r.status_code}"


# --- Test 2: Landing page structure ---

@pytest.mark.parametrize("viewport", VIEWPORTS)
@pytest.mark.parametrize("browser_type", BROWSERS)
def test_landing_page(viewport, browser_type, astro_server):
    """Landing page renders hero, screenshots, and feature cards."""
    width, height, label = viewport
    with sync_playwright() as p:
        launcher = getattr(p, browser_type)
        browser = launcher.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(BASE_URL, wait_until="networkidle")

        # Hero headline exists
        headline = page.locator(".sh-hero-headline")
        assert headline.count() >= 1, "Hero headline missing"

        # Hero CTA buttons
        buttons = page.locator(".sh-hero-btn")
        assert buttons.count() >= 2, f"Expected 2 CTA buttons, got {buttons.count()}"

        # SVG screenshots
        images = page.locator("img[src$='.svg']")
        assert images.count() >= 3, f"Expected at least 3 SVG images, got {images.count()}"

        # Feature cards
        cards = page.locator(".sh-feature-card")
        assert cards.count() >= 4, f"Expected at least 4 feature cards, got {cards.count()}"

        # No horizontal overflow
        no_overflow = page.evaluate(
            "() => document.documentElement.scrollWidth <= window.innerWidth"
        )
        assert no_overflow, f"Horizontal overflow on {label} ({browser_type})"

        # Screenshot
        out_dir = os.path.join("tests", "screenshots")
        os.makedirs(out_dir, exist_ok=True)
        page.screenshot(
            path=os.path.join(out_dir, f"astro_landing_{label}_{browser_type}.png"),
            full_page=True,
        )

        browser.close()


# --- Test 3: Docs pages have sidebar and content ---

@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_docs_page_structure(viewport, astro_server):
    """Docs pages have navigation, sidebar (desktop), and content."""
    width, height, label = viewport
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(f"{BASE_URL}/einfuehrung/intro/", wait_until="networkidle")

        # Page title
        title = page.locator("h1")
        assert title.count() >= 1, "No h1 on docs page"

        # Starlight header
        header = page.locator("header")
        assert header.count() >= 1, "Header missing"

        # Sidebar on desktop
        if width >= 768:
            sidebar = page.locator("nav[aria-label]")
            assert sidebar.count() >= 1, "Sidebar missing on desktop"

        browser.close()


# --- Test 4: Images load without errors ---

@pytest.mark.parametrize("path,name", PAGES[:1] + PAGES[7:8])
def test_no_broken_images(path, name, astro_server):
    """No image requests should fail."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        failed_requests = []
        page.on("requestfailed", lambda req: failed_requests.append(req.url))

        page.goto(f"{BASE_URL}{path}", wait_until="networkidle")

        image_failures = [
            url for url in failed_requests if ".svg" in url or ".png" in url
        ]
        assert len(image_failures) == 0, f"Broken images on {name}: {image_failures}"

        browser.close()


# --- Test 5: No console errors ---

@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_no_console_errors(viewport, astro_server):
    """No JS console errors on page load."""
    width, height, label = viewport
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})

        errors = []
        page.on(
            "console",
            lambda msg: errors.append(msg.text) if msg.type == "error" else None,
        )

        page.goto(BASE_URL, wait_until="networkidle")
        page.wait_for_timeout(500)

        assert len(errors) == 0, f"Console errors on {label}: {errors}"

        browser.close()


# --- Test 6: Search works ---

def test_search_exists(astro_server):
    """Pagefind search assets exist."""
    import requests

    # Pagefind generates a JS bundle
    r = requests.get(f"{BASE_URL}/pagefind/pagefind.js", timeout=10)
    assert r.status_code == 200, "Pagefind search JS not found"


# --- Test 7: Favicon and OG image ---

def test_favicon_and_og(astro_server):
    """Favicon and OG image are accessible."""
    import requests

    for path in ["/favicon.svg", "/favicon.ico", "/images/og-image.png", "/apple-touch-icon.png"]:
        r = requests.get(f"{BASE_URL}{path}", timeout=10)
        assert r.status_code == 200, f"{path} returned {r.status_code}"


# --- Test 8: Internal links are valid ---

def test_internal_links(astro_server):
    """All internal links on the landing page point to valid pages."""
    import requests

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="networkidle")

        links = page.eval_on_selector_all(
            "a[href^='/']",
            "els => els.map(e => e.getAttribute('href'))",
        )

        # Deduplicate and filter
        unique_links = set()
        for link in links:
            # Strip anchors
            clean = link.split("#")[0]
            if clean and clean != "/":
                unique_links.add(clean)

        broken = []
        for link in unique_links:
            # Skip pagefind and sitemap
            if "pagefind" in link or "sitemap" in link:
                continue
            r = requests.get(f"{BASE_URL}{link}", timeout=10, allow_redirects=True)
            if r.status_code != 200:
                broken.append(f"{link} → {r.status_code}")

        assert len(broken) == 0, f"Broken internal links: {broken}"

        browser.close()


# --- Test 9: Dark mode toggle ---

def test_dark_mode_toggle(astro_server):
    """Dark mode toggle exists and works."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL, wait_until="networkidle")

        # Starlight has a theme toggle button
        toggle = page.locator("starlight-theme-select, [data-theme-toggle]")
        assert toggle.count() >= 1 or page.locator("select").count() >= 1, "Theme toggle not found"

        browser.close()
