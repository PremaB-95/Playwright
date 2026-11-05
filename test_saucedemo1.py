import pytest
from playwright.sync_api import sync_playwright
# from playwright.sync_api import expect

@pytest.fixture(scope="function")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()
    playwright.stop()
def test_saucedemo(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    assert page.title() == "Swag Labs"

def test_login_page(browser):
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name = "Login").click()