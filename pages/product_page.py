from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    B_ADD_TO_CART = (
        By.XPATH, "//a[contains(text(),'Add to cart')]")

    def add_to_cart(self):
        self.wait_until_clickable(self.B_ADD_TO_CART).click()
