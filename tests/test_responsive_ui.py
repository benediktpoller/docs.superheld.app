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


@pytest.fixture(scope="session")
def hugo_server():
    """Start Hugo server once for the entire test session."""
    server = _start_hugo_server()
    assert _wait_for_server("http://127.0.0.1:1313"), "Hugo server did not start in time"
    yield server
    server.terminate()
    server.wait(5)


@pytest.mark.parametrize("viewport", VIEWPORTS)
@pytest.mark.parametrize("browser_type", BROWSERS)
def test_homepage_responsive(viewport, browser_type, hugo_server):
    """Test the homepage renders correctly across viewports and browsers."""
    width, height, label = viewport
    with sync_playwright() as p:
        launcher = getattr(p, browser_type)
        browser = launcher.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto("http://127.0.0.1:1313", wait_until="networkidle")

        # Hextra hero headline
        headline = page.locator("h1")
        assert headline.count() >= 1, "No h1 headline found"

        # Hero subtitle area
        subtitle = page.locator("p")
        assert subtitle.count() >= 1, "No paragraph text found"

        # Navigation bar
        navbar = page.locator(".hextra-nav-container")
        assert navbar.is_visible(), "Navigation bar missing"

        # Feature cards (Hextra card components)
        cards = page.locator(".hextra-card")
        assert cards.count() >= 4, f"Expected at least 4 cards, got {cards.count()}"

        # SVG device screenshots
        device_images = page.locator("img[src$='.svg']")
        assert device_images.count() >= 3, f"Expected at least 3 SVG images, got {device_images.count()}"

        # Footer
        footer = page.locator(".hextra-footer")
        assert footer.count() >= 1, "Footer missing"

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


@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_homepage_images_load(viewport, hugo_server):
    """Test that all SVG screenshot images load correctly."""
    width, height, label = viewport
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})

        failed_requests = []
        page.on("requestfailed", lambda req: failed_requests.append(req.url))

        page.goto("http://127.0.0.1:1313", wait_until="networkidle")

        # Check no image requests failed
        image_failures = [url for url in failed_requests if ".svg" in url or ".png" in url]
        assert len(image_failures) == 0, f"Failed image requests: {image_failures}"

        # Verify SVG images exist
        images = page.locator("img[src$='.svg']")
        count = images.count()
        assert count >= 4, f"Expected at least 4 SVG images, got {count}"

        browser.close()


@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_docs_page_renders(viewport, hugo_server):
    """Test that documentation pages render correctly with Hextra theme."""
    width, height, label = viewport
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto("http://127.0.0.1:1313/docs/", wait_until="networkidle")

        # Page title
        title = page.locator("h1")
        assert title.count() >= 1, "No h1 on docs page"

        # Navigation
        navbar = page.locator(".hextra-nav-container")
        assert navbar.is_visible(), "Navigation bar missing on docs page"

        # Sidebar (visible on desktop)
        if width >= 768:
            sidebar = page.locator(".hextra-sidebar-container")
            assert sidebar.count() >= 1, "Sidebar missing on docs page"

        browser.close()


@pytest.mark.parametrize("viewport", VIEWPORTS)
def test_homepage_no_console_errors(viewport, hugo_server):
    """Test that no console errors occur on page load."""
    width, height, label = viewport
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": width, "height": height})

        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

        page.goto("http://127.0.0.1:1313", wait_until="networkidle")
        page.wait_for_timeout(1000)

        assert len(errors) == 0, f"Console errors on {label}: {errors}"

        browser.close()
