import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.get("https://www.browserstack.com/users/sign_in")    # in real project it shouldn't be hardcoded
    browser.maximize_window()
    yield browser
    browser.quit()
