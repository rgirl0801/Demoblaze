from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class MainPage(BasePage):
    B_CAROUSEL_NEXT = (
        By.XPATH, "//*[@id='carouselExampleIndicators']/a[2]/span[1]")
    B_CAROUSEL_PREV = (
        By.XPATH, '//*[@id="carouselExampleIndicators"]/a[1]/span[1]')
    IMG_SAMSUNG = (By.CSS_SELECTOR, 'img[src*="Samsung1.jpg"]')
    IMG_NEXUS = (By.CSS_SELECTOR, 'img[src*="nexus1.jpg"]')
    IMG_LAPTOP = (By.CSS_SELECTOR, 'img[src*="iphone1.jpg"]')
    B_CATEGORY_PHONES = (By.XPATH, "//a[contains(text(),'Phones')]")
    B_CATEGORY_LAPTOPS = (By.XPATH, "//a[contains(text(),'Laptops')]")
    B_CATEGORY_MONITORS = (By.XPATH, "//a[contains(text(),'Monitors')]")

    def carousel_click_next(self):
        self.wait_until_clickable(self.B_CAROUSEL_NEXT).click()

    def carousel_click_prev(self):
        self.wait_until_clickable(self.B_CAROUSEL_PREV).click()

    def samsung_is_present(self):
        assert self.element_is_present(self.IMG_SAMSUNG)

    def nexus_is_present(self):
        assert self.element_is_present(self.IMG_NEXUS)

    def laptop_is_present(self):
        assert self.element_is_present(self.IMG_LAPTOP)

    def select_phone_category(self):
        self.wait_until_clickable(self.B_CATEGORY_PHONES)

    def select_phone_laptops(self):
        self.wait_until_clickable(self.B_CATEGORY_LAPTOPS)

    def select_phone_monitors(self):
        self.wait_until_clickable(self.B_CATEGORY_MONITORS)