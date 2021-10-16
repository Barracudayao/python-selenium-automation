from selenium.webdriver.common.by import By
from class7HW.pages.base_page import BasePage

EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']/h2")


class CartPage(BasePage):

    def verity_empty_cart(self):
        self.verify_text("Your Amazon Cart is empty", *EMPTY_CART)
