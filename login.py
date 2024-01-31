from locators import Locators
from base import BasePage


class LoginPage(BasePage):
    """
    Page Object class for interacting with the login page.
    """

    def enter_email(self, email):
        """
        Enter the specified email into the email input field.
        :param email: an email address
        """
        email_field = self.find_an_element(Locators.USER_EMAIL_LOGIN)
        email_field.send_keys(email)

    def enter_password(self, password):
        """
        Enters the specified password into the password input field.
        :param password: a password
        """
        password_field = self.find_an_element(Locators.USER_PASSWORD)
        password_field.send_keys(password)

    def click_sign_in_button(self):
        """
        Click the "Sign me in" button
        """
        sign_in_button = self.find_an_element(Locators.SIGN_IN_BUTTON)
        self.scroll_to_element(sign_in_button)
        sign_in_button.click()

    def get_error_message(self, error_locator):
        """
        Get the text of the error message on the page.
        :return: text of the error message
        """
        error_msg = self.find_an_element(error_locator)
        return error_msg.text

    def get_current_url(self):
        """
        Get the current URL of the page.
        :return: current URL
        """
        return self.browser.current_url
