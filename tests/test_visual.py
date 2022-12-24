import allure
import pytest

from pages.main_page import MainPage


@allure.title('Visual tests')
class TestVisualClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.main_page = MainPage(browser, url)
        self.main_page.open_page()

    @allure.testcase("Logo is present")
    def test_logo_is_present(self):
        self.main_page.check_logo_is_exist()

    @allure.testcase("User is able to click next and previous img in carousel")
    def test_carousel_next_prev(self):
        self.main_page.samsung_is_present()
        self.main_page.carousel_click_prev()
        self.main_page.laptop_is_present()
        self.main_page.carousel_click_next()
        self.main_page.carousel_click_next()
        self.main_page.nexus_is_present()

    @allure.testcase("Category displays valid items")
    def test_categories_phones(self):
        self.main_page.select_phone_category()
        self.main_page.check_qty_phones()

    @allure.testcase("Text in footer is present")
    def test_footer_is_present(self):
        self.main_page.check_footer_about()
