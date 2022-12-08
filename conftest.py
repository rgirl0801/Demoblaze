import pytest
import Links
from selenium import webdriver


@pytest.fixture(autouse=True)
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def url():
    url = Links.base_url
    if not url:
        raise Exception("Wrong environment")
    return url
