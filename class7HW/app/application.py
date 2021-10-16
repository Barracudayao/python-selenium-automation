from class7HW.pages.home_page import HomePage
from class7HW.pages.signin_page import SignInPage
from class7HW.pages.cart_page import CartPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.home_page = HomePage(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)