import logging
from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from constants import TEXT_ABOUT


class BasePage:
    LOGGER = logging.getLogger(__name__)
    B_HOME = (By.XPATH, "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]")
    B_CONTACT = (By.XPATH, "//a[contains(text(),'Contact')]")
    B_ABOUT = (By.XPATH, "//a[contains(text(),'About us')]")
    B_CART = (By.XPATH, "//a[@id='cartur']")
    B_LOGIN = (By.XPATH, "//a[@id='login2']")
    B_LOGOUT = (By.XPATH, "//a[@id='logout2']")
    B_SIGN_UP = (By.XPATH, "//a[@id='signin2']")
    F_SIGNUP_USERNAME = (By.ID, "sign-username")
    F_SIGNUP_PASSWORD = (By.ID, "sign-password")
    F_LOGIN_USERNAME = (By.ID, "loginusername")
    F_LOGIN_PASSWORD = (By.ID, "loginpassword")
    T_ABOUT = (By.XPATH, '//*[@id="fotcont"]/div[1]/div/div/p')
    T_GET_IN_TOUCH = (By.XPATH, "//b[contains(text(),'Get in Touch')]")
    LOGO = (By.ID, 'nava')

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        try:
            self.browser.get(self.url)
        except Exception as e:
            self.LOGGER.error(f"tException: {e}")

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.element_to_be_clickable(locator))
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_visible(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.visibility_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_alert(self, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.alert_is_present()
            )

        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def wait_until_all_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        try:
            return WebDriverWait(self.browser, timeout).until(
                ec.presence_of_all_elements_located(locator)
            )
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        try:
            self.wait_until_present(locator, timeout)
            return True
        except TimeoutException as e:
            self.LOGGER.error(f"TimeoutException: {e}")

    # def elements_are_present(self, locator: Tuple, timeout: int = 5) -> bool:
    #     try:
    #         self.wait_until_all_present(locator, timeout)
    #         return True
    #     except TimeoutException as e:
    #         self.LOGGER.error(f"TimeoutException: {e}")

    def go_to_home(self):
        self.wait_until_clickable(self.B_HOME).click()

    def go_to_contact(self):
        self.wait_until_clickable(self.B_CONTACT).click()

    def go_to_cart(self):
        self.wait_until_clickable(self.B_CART).click()

    def go_to_login(self):
        self.wait_until_clickable(self.B_LOGIN).click()

    def go_to_signup(self):
        self.wait_until_clickable(self.B_SIGN_UP).click()

    def accept_alert(self):
        self.wait_until_alert()
        self.browser.switch_to_alert().accept()

    def get_alert_text(self):
        prompt = self.wait_until_alert()
        return prompt.text

    def check_footer_about(self):
        assert self.wait_until_present(self.T_ABOUT).text == TEXT_ABOUT, \
            f'Wrong text: {self.wait_until_present(self.T_ABOUT).text}'

    def check_logo_is_exist(self):
        assert self.wait_until_present(self.LOGO)
