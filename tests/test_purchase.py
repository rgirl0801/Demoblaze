import time

import allure
import pytest

from constants import PURCHASE_DATA
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


@allure.story('Purchase')
class TestPurchaseClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.product_page = ProductPage(browser, url)
        self.cart_page = CartPage(browser, url)

    @pytest.mark.e2e
    @allure.feature('Successful purchase')
    def test_purchase_success(self, url):
        self.main_page.open_page()
        self.main_page.open_samsung_galaxy_s6()
        self.product_page.add_to_cart()
        self.product_page.accept_alert()
        self.product_page.go_to_cart()
        self.cart_page.place_order()
        self.cart_page.fill_form(*PURCHASE_DATA)
        self.cart_page.press_confirm_purchase()
        self.cart_page.click_ok_purchase()
        assert self.main_page.page_is_open(url)

    @pytest.mark.e2e
    @allure.feature('Purchase without name impossible')
    def test_purchase_wo_name(self):
        self.main_page.open_page()
        self.main_page.open_samsung_galaxy_s6()
        self.product_page.add_to_cart()
        self.product_page.accept_alert()
        self.product_page.go_to_cart()
        self.cart_page.place_order()
        self.cart_page.fill_form('', '', PURCHASE_DATA['card'], '', '', '')
        self.cart_page.press_confirm_purchase()
        assert self.cart_page.get_alert_text() == 'Please fill out Name and Creditcard.'

    @pytest.mark.e2e
    @allure.feature('Purchase without card number impossible')
    def test_purchase_wo_card(self):
        self.main_page.open_page()
        self.main_page.open_samsung_galaxy_s6()
        self.product_page.add_to_cart()
        self.product_page.accept_alert()
        self.product_page.go_to_cart()
        self.cart_page.place_order()
        self.cart_page.fill_form(PURCHASE_DATA['name'], '', '', '', '', '')
        self.cart_page.press_confirm_purchase()
        assert self.cart_page.get_alert_text() == 'Please fill out Name and Creditcard.'
