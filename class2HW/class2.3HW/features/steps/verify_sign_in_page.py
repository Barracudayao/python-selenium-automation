from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver



@given("Open Amazon homepage")
def open_amazon_homepage(context):
    context.driver = webdriver.Chrome("/Users/seashore/PycharmProjects/Careerist7/python-selenium-automation/chromedriver 2")
    context.driver.get("https://www.amazon.com")


@when("Click Orders")
def click_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, "#nav-orders .nav-line-2").click()

@then("Verify Sign in page opened")
def verify_sign_in_page_open(context):
    assert 'signin' in context.driver.current_url, f"Expected query not in {context.driver.current_url.lower()}"
    print('Test Passed')