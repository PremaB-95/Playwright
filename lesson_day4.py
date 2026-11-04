from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # Login > Checkout
    page = browser.new_page()
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.get_by_role("button", name = "Login").click()
    page.wait_for_selector(".inventory_item")
    product_count = page.locator(".inventory_item").count()
    print(product_count)
    products = page.locator(".inventory_item_name").all_text_contents()
    print(products)
    expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
    item = page.locator(".inventory_item", has_text="Sauce Labs Backpack")
    item.get_by_role("button", name="Add to cart").click()
    cart = page.locator(".shopping_cart_badge")
    quantity =int(cart.inner_text())
    assert quantity ==1
    cart.click()
    page.wait_for_selector(".header_secondary_container")
    assert page.locator(
        ".header_secondary_container"
    ).inner_text() == "Your Cart"
    cart_item = page.locator(".inventory_item_name").inner_text()
    assert cart_item == "Sauce Labs Backpack"
    print(cart_item)
    page.get_by_role("button", name="Checkout").click()
    page.wait_for_selector(".header_secondary_container").is_visible()
    page.locator("#first-name").fill("John")
    page.locator("#last-name").fill("doe")
    page.locator("#postal-code").fill("123456")
    page.get_by_role("button", name="Continue").click()
    assert page.locator(".inventory_item_name").inner_text() == "Sauce Labs Backpack"
    page.get_by_role("button", name="Finish").click()
    success = page.locator(".complete-header")
    expect (success).to_have_text("Thank you for your order!")
    browser.close()
