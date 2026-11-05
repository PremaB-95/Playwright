import pytest
from playwright.sync_api import sync_playwright, expect

# 1. Browser Fixture
@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(
        headless=False
    )
    try:
        yield browser
    finally:
        browser.close()
        playwright.stop()

# 2. Context Fixture
@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

# 3. Page Fixture
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()

def test_saucedemo(page):
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"

def test_login_page(page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name = "Login").click()