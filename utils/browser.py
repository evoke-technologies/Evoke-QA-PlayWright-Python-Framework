from playwright.sync_api import sync_playwright

def get_browser():
    """Initialize and return the browser instance."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True to run headless
        return browser
