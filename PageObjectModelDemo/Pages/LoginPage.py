from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class LoginPage(BasePage):

    """By locators or Object Repositories"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "radius")
    SIGNUP_LINK = (By.ID, "Sign up")

    """Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """Used to get login page title"""
    def get_login_page_title(self, title):
        self.get_title(title)

    """Used to validate if sign_up link exits"""
    def is_sign_up_link_exits(self):
        return self.is_visible(self.SIGNUP_LINK)

    """Used to login to App"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)