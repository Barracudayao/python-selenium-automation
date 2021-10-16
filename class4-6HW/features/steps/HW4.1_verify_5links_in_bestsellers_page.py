from behave import *
from selenium.webdriver.common.by import By
from time import sleep

LINKS = (By.XPATH, "//a[contains(@href, 'zg_bs_tab')]")
# LINKS = (By.CSS_SELECTOR, '#CardInstanceUBACYSfZVZQrTkibUrDPnA a')
BESTSELLER = (By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")


@given('Open amazon Bestsellers page')
def open_bestsellers_page(context):
    # can't open bestsellers pages, instead get homepage redirect to bestseller pages
    context.driver.get("https://www.amazon.com")
    sleep(2)
    context.driver.find_element(*BESTSELLER).click()
    sleep(3)


@then('Verify there are 5 links')
def verify_5links(context):
    actual_links = context.driver.find_elements(*LINKS)
    assert len(actual_links) == int(5), f'Expected 5 links, but got {actual_links}'
















