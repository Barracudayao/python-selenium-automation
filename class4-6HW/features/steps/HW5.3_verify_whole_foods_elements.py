from behave import *
from selenium.webdriver.common.by import By
from time import sleep
PRODUCT_FRAME = (By.XPATH, "//li[@class='s-result-item']")
PRODUCT_NAME = (By.CSS_SELECTOR, ".wfm-sales-item-card__product-name")


@given('Open Wholefoods deal page')
def open_wholefoods_deal_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')
    sleep(3)


@then("Verify Wholefoods deal page has a text ‘Regular’ and a product name")
def verify_text_Regular(context):
    product_elements = context.driver.find_elements(*PRODUCT_FRAME)

    for product_element in product_elements:
        assert 'Regular' in product_element.text, f'Error Regular text, but got {product_element.text}'

        product_name = product_element.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, f'Expected product_name'







