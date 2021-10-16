from behave import *


@given('Open Amazon page')
def open_amazon_page(context):
    context.app.home_page.open_amazon_home_page()


@when('Click Amazon Orders link')
def click_amazon_orders_link(context):
    context.app.home_page.click_order_links()


@then('Verify Sign In page is opened')
def verify_signin_page(context):
    context.app.signin_page.verify_signin_page()

