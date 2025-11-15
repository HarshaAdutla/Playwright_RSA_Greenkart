from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

    def checkout_page(self, country_name):
        self.page.get_by_role('combobox').select_option(country_name)
        self.page.locator('.chkAgree').check()
        expect(self.page.locator('.chkAgree')).to_be_checked()


    def purchase(self):
        self.page.get_by_role('button', name='Proceed').click()

    def success_message(self):
        expect(self.page.locator('.wrapperTwo')).to_contain_text('successfully')


