from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
PRIVACY_NOTICE = (By.XPATH, "//a[contains(@href, 'amazon.com/privacy')]")


@given('Open Amazon T&C page')
def open_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html'
                       '/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store_original_windows(context):
    context.driver.original_window = context.driver.current_window_handle
    print(context.driver.original_window)

@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
    context.driver.find_element(*PRIVACY_NOTICE).click()
    sleep(3)


@when('Switch to the newly opened window')
def switch_newly_opened_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice_page_open(context):
    expected_url = context.driver.current_url
    actual_url = "https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ"
    assert expected_url == actual_url, f'Error {actual_url}, but got {expected_url}'



@then('User can close new window and switch back to original')
def close_new_window_switch_back_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.driver.original_window)
    current_url1 = context.driver.current_window_handle
    print(current_url1)
    assert current_url1 == context.driver.original_window, f'Error {context.driver.original_window}, but got {current_url1}'