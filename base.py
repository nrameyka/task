from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    BasePage class serves as a foundation for creating Page Object classes.
    """

    def __init__(self, browser):
        self.browser = browser

    def find_an_element(self, locator):
        """
        Waits for the specified element identified by the locator to be visible.
        :param locator: Tuple (locator strategy, the value)
        :return: WebElement
        """
        wait = WebDriverWait(self.browser, 10)
        return wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        """
        Scroll the page to make the specified element visible.
        :param element: WebElement to scroll to
        """
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
