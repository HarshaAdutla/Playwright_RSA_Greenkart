import time

from playwright.sync_api import Page, expect

from pageObjects.checkout_page import CheckoutPage


class CartPage:

    def __init__(self, page: Page):
        self.page = page

    def promo_code(self, promo_code):
        expect(self.page.locator('.products')).to_be_visible()
        self.page.locator('.promoCode').fill(promo_code)
        self.page.get_by_role('button', name='Apply').click(timeout=8000)
        time.sleep(5)

    def verify_promo_info(self):
        expect(self.page.locator('.promoInfo')).to_have_text("Code applied ..!")

    def order_placing(self):
        self.page.get_by_role('button', name='Place Order').click()
        checkout_page = CheckoutPage(self.page)
        return checkout_page
