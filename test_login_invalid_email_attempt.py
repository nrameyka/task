from login import LoginPage
from helpers import get_creds
from locators import Locators


def test_invalid_email(browser):
    """
    Login attempt with invalid e-mail format
    """
    creds = get_creds("credentials.yaml")

    login_page = LoginPage(browser)

    login_page.enter_email(creds["invalid_email"])
    login_page.enter_password(creds["password"])
    login_page.click_sign_in_button()

    error_msg_text = login_page.get_error_message(Locators.ERROR_MSG_INVALID_EMAIL)
    assert "Invalid Email" in error_msg_text

    assert login_page.get_current_url().endswith("/users/sign_in")
