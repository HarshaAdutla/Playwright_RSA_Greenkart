import pytest
from playwright.sync_api import Page
from pytest_bdd import given, scenarios, when, parsers, then

from pageObjects.home_page import HomePage

scenarios('../bdd/placing_order.feature')


@pytest.fixture(scope='session')
def shared_data():
    return {}


@given('Go to greenkart page')
def place_order(page: Page, shared_data):
    home_page = HomePage(page)
    home_page.goto_page()
    shared_data['homePage'] = home_page


@given('Verify the home page')
def verify_home_page(shared_data):
    home_page = shared_data['homePage']
    home_page.verify_home_page()


@when('All products visible')
def verify_products_visibility(shared_data):
    home_page = shared_data['homePage']
    home_page.verify_products()


@then(parsers.parse('Search one item {item_name}'))
def search_item(item_name, shared_data):
    home_page = shared_data['homePage']
    home_page.search_item(item_name)


@then(parsers.parse('Add {item_name} to cart'))
def add_item(item_name, shared_data):
    home_page = shared_data['homePage']
    home_page.add_to_cart(item_name)


@then('Go to cart page')
def goto_cart(shared_data):
    home_page = shared_data['homePage']
    cart_page = home_page.checkout()
    shared_data['cartPage'] = cart_page


@then(parsers.parse('Apply the {promo_code}'))
def apply_promo_code(promo_code, shared_data):
    cart_page = shared_data['cartPage']
    cart_page.promo_code(promo_code)


@then('Verify promo code message')
def promo_code_verification(shared_data):
    cart_page = shared_data['cartPage']
    cart_page.verify_promo_info()


@then('Place order')
def placing_order(shared_data):
    cart_page = shared_data['cartPage']
    checkout_page = cart_page.order_placing()
    shared_data['checkoutPage'] = checkout_page


@then(parsers.parse('Select the {country_name}'))
def address(country_name, shared_data):
    checkout_page = shared_data['checkoutPage']
    checkout_page.checkout_page(country_name)


@then('Complete the purchase')
def purchase(shared_data):
    checkout_page = shared_data['checkoutPage']
    checkout_page.purchase()


@then('Verify the message')
def verify_message(shared_data):
    checkout_page = shared_data['checkoutPage']
    checkout_page.success_message()
