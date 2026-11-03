from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

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
    assert page.get_by_text("Sauce Labs Backpack").is_visible()
    item = page.locator(".inventory_item", has_text="Sauce Labs Backpack")
    item.get_by_role("button", name="Add to cart").click()
    cart = page.locator(".shopping_cart_badge")
    quantity =int(cart.inner_text())
    assert quantity ==1
    cart.click()
    assert page.wait_for_selector(
        ".header_secondary_container"
    ).is_visible() == "Your Cart"
    cart_item = page.locator(".inventory_item_name").inner_text()
    assert cart_item == "Sauce Labs Backpack"
    print(cart_item)
    print(page.title())
    remove_button = page.get_by_role(
        "button", name="Remove"
    )
    remove_button.click()
    assert cart.is_hidden()
    browser.close()