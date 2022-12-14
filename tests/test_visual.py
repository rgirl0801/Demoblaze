import allure
import pytest

from pages.main_page import MainPage


class TestVisualClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.main_page.open_page()

    @allure.title("Carousel is clickable next and previous buttons are active")
    def test_carousel_next_prev(self):
        self.main_page.samsung_is_present()
        self.main_page.carousel_click_prev()
        self.main_page.laptop_is_present()
        self.main_page.carousel_click_next()
        self.main_page.carousel_click_next()
        self.main_page.nexus_is_present()

    @allure.title("Phone's category is available")
    def test_categories_phones(self):
        self.main_page.select_phone_category()
        self.main_page.check_qty_phones()

    @allure.title("Footer is present and text is valid")
    def test_footer_is_present(self):
        self.main_page.check_footer_about()
