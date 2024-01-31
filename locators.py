from selenium.webdriver.common.by import By


class Locators:
    USER_EMAIL_LOGIN = (By.ID, "user_email_login")
    USER_PASSWORD = (By.ID, "user_password")
    SIGN_IN_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Sign me in']")
    ERROR_MSG_INVALID_EMAIL = (
        By.XPATH,
        "//*[@id='user_email_login']/following-sibling::div[@class='error-msg show']//span[@aria-live='polite']"
    )
