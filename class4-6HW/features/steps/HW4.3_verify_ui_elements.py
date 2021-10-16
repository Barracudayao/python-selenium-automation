from behave import *
from selenium.webdriver.common.by import By


ELEMENTS1 = (By.XPATH, "//div[@class='a-box-inner']")
ELEMENTS2 = (By.CSS_SELECTOR, "#category-section li")


@given('Open Customer Service’s pages')
def open_customer_service_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify these UI elements1 are present of the pages')
def verify_ui_elements1_present(context):
    actual_elements1 = context.driver.find_elements(*ELEMENTS1)
    expected_elements1 = 9
    assert len(actual_elements1) == int(expected_elements1), f'Error int(expected_elements), but got {actual_elements1}'


@then('Verify these UI elements2 are present of the pages')
def verify_ui_elements1_present(context):
    actual_elements2 = context.driver.find_elements(*ELEMENTS2)
    expected_element2 = 12
    assert len(actual_elements2) == int(expected_element2), f'Error int(expected_elements2), but got {actual_elements2}'