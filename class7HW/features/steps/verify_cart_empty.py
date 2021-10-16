from behave import *


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.home_page.click_cart()


@then("Verify 'Your Amazon Cart is empty' text present")
def verify_text_present(context):
    context.app.cart_page.verity_empty_cart()



