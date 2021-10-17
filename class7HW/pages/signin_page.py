from selenium.webdriver.common.by import By
from class7HW.pages.base_page import BasePage


class SignInPage(BasePage):

    SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

    def verify_signin_page(self):
        self.verify_text("Sign-In", *self.SIGNIN_TEXT)
