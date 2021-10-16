from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

SearchHelp = (By.ID, "helpsearch")
Cancel = (By.CSS_SELECTOR, ".help-content h1")


@given('Open Amazon Help pages https://www.amazon.com/gp/help/customer/display.html')
def open_amazon_help_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when('Use “Search Help Library” field, search for "Cancel order" and hit enter')
def cancel_order(context):
    Search = context.driver.find_element(*SearchHelp)
    Search.clear()
    Search.send_keys("Cancel order")
    Search.send_keys(Keys.RETURN)


@then('Verify that ‘Cancel Items or Orders’ text is present')
# method 1
def verify_text(context):
    expect_text = context.driver.find_element(*Cancel).text
    print(expect_text)
    assert expect_text in "Cancel Items or Orders", f'expected "Cancel Items or Orders", but get {expect_text}'


