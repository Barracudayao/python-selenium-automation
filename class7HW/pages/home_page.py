from selenium.webdriver.common.by import By

from class7HW.pages.base_page import BasePage


class HomePage(BasePage):
    ORDER_LinkS = (By.XPATH, "//a[@id='nav-orders']")
    CART = (By.ID, "nav-cart-count-container")

    def open_amazon_home_page(self):
        self.open_page()

    def click_order_links(self):
        self.click(*self.ORDER_LinkS)

    def click_cart(self):
        self.click(*self.CART)






