import time
import pytest

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestPurchaseClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.product_page = ProductPage(browser,url)
        self.cart_page = CartPage(browser, url)

    def test_purchase(self):
        self.main_page.open_page()
        self.main_page.open_samsung_galaxy_s6()
        self.product_page.add_to_cart()
        self.product_page.accept_alert()
        self.product_page.go_to_cart()
        self.cart_page.place_order()

