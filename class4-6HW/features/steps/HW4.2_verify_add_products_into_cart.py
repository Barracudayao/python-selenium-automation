from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

INPUT = (By.ID, "twotabsearchtextbox")
MUG = (By.XPATH, "//div[@class='a-section aok-relative s-image-square-aspect']")
ADDCART = (By. ID, "add-to-cart-button")
NUM = (By.ID, "nav-cart-count")

@given('Open Amazon homepage')
def open_homepage(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {product} in the searchbar and enter')
def search_product(context, product):
    searchbar = context.driver.find_element(*INPUT)
    searchbar.send_keys('mug')
    searchbar.send_keys(Keys.ENTER)


@when('Pick first {product} from the list and click')
def first_mug(context, product):
    first_mug = context.driver.find_elements(*MUG)
    first_mug[0].click()


@when('Click "Add to Cart" button')
def click_add_cart(context):
    context.driver.find_element(*ADDCART).click()


@Then('Verify number of items in the cart')
def verify_number_items_in_cart(context):
    expected_number = context.driver.find_element(*NUM).text
    # test = expected_number.get_attribute('class') #
    # print(test)
    assert int(expected_number) == int(1), f' get 1 product number, but got {expected_number}'


