import time
import pytest

from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


class TestVisualClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.product_page = ProductPage(browser,url)
        self.cart_page = CartPage(browser, url)

    def test_carousel_next_prev(self):
        self.main_page.open_page()
        self.main_page.samsung_is_present()
        self.main_page.carousel_click_prev()
        self.main_page.nexus_is_present()
        self.main_page.laptop_is_present()

    def test_purchase(self):
        self.main_page.open_page()
        self.main_page.open_samsung_galaxy_s6()
        self.product_page.add_to_cart()
        self.product_page.accept_alert()
        self.product_page.go_to_cart()
        self.cart_page.place_order()
        time.sleep(2)

