from selenium.webdriver.common.by import By
from class7HW.pages.base_page import BasePage


SIGNIN_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

class SignInPage(BasePage):

    def verify_signin_page(self):
        self.verify_text("Sign-In", *SIGNIN_TEXT)
