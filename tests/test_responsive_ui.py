import os
import subprocess
import time

import pytest
from playwright.sync_api import sync_playwright


def _start_hugo_server():
    # Start Hugo in a subprocess; ensure it uses a fixed port to avoid clashes.
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


@pytest.mark.parametrize(
    "viewport",
    [
        (1280, 800, "desktop"),
        (1024, 768, "tablet"),
        (375, 812, "mobile"),
    ],
)
def test_homepage_responsive(viewport):
    width, height, label = viewport
    server = _start_hugo_server()
    try:
        assert _wait_for_server("http://127.0.0.1:1313"), "Hugo server did not start in time"
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(viewport={"width": width, "height": height})
            page.goto("http://127.0.0.1:1313", wait_until="networkidle")

            # Basic UI checks
            heading = page.locator("h1").inner_text().strip().upper()
            assert "DOKUMENTATION" in heading, "Homepage heading missing"
            assert page.locator("text=Installation").first.is_visible(), "Installation link missing"
            assert page.locator("text=Apps & Plattformen").first.is_visible(), "Apps & Plattformen link missing"
            assert page.locator("text=Installationsanleitung starten").first.is_visible(), "CTA button missing"

            # Capture snapshot for regression / visual sanity
            out_dir = os.path.join("tests", "screenshots")
            os.makedirs(out_dir, exist_ok=True)
            page.screenshot(path=os.path.join(out_dir, f"homepage_{label}.png"), full_page=True)

            browser.close()
    finally:
        server.terminate()
        server.wait(5)
