from behave import *
from selenium.webdriver.common.by import By
from time import sleep

CART = (By.CSS_SELECTOR, ".nav-cart-icon.nav-sprite")
TEXT = (By.XPATH, "//div[@id='sc-empty-cart-message']/h2")

@given('Open Amazon homepage')
def open_amazon_homepage(context):
    context.driver.get("https://www.amazon.com")

@when('Click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART).click()

@then('Verifies that Your Amazon Cart is empty')
def verify_cart_empty(context):
    expect_text = context.driver.find_element(*TEXT).text
    print(expect_text)
    sleep(1)
    assert expect_text in "Your Amazon Cart is empty", f' actual text "Your Amazon Cart is empty", but get {expect_text}'


