from playwright.sync_api import expect, Page

from pageObjects.cart_page import CartPage


class HomePage:

    def __init__(self, page: Page):
        self.page = page

    def goto_page(self):
        self.page.goto("https://rahulshettyacademy.com/seleniumPractise/#/")

    def verify_home_page(self):
        expect(self.page.locator(".greenLogo")).to_be_visible()
        print("It is visible")

    def verify_products(self):
        expect(self.page.locator(".products")).to_be_visible()
        print("All Products Are Visible")

    def search_item(self, item_name):
        self.page.get_by_placeholder('Search for Vegetables and Fruits').fill(item_name)
        self.page.locator('.search-button').click()
        self.page.locator('.products')

    def add_to_cart(self, item_name):
        item = self.page.locator('.product').filter(has_text=item_name)
        item.get_by_role('button', name='ADD TO CART').click()

    def checkout(self):
        self.page.locator("img[alt='Cart']").click()
        self.page.get_by_role("button", name='PROCEED TO CHECKOUT').click()
        cart_page = CartPage(self.page)
        return cart_page
