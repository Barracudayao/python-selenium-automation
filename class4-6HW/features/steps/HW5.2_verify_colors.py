from behave import *
from selenium.webdriver.common.by import By

COLORS = (By.XPATH, "//img[@class='imgSwatch']")
CURRENT_COLOR = (By.XPATH, "//div[@id='variation_color_name']//span[@class='selection']")


@given('Open Amazon product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')


@then('Verify colors has been selected')
def verify_colors_selected(context):
   actual_colors = ['Black', 'Dark Vintage', 'Dark Wash', 'Indigo Wash', 'Light Vintage',
                     'Light Wash', 'Medium Vintage', 'Medium Wash', 'Rinse', 'Rinsed Vintage',
                     'Vintage Light Wash', 'Washed Black', 'Bright White', 'Dark Khaki',
                     'Light Khaki', 'Olive', 'Sage Green', 'Blue Overdyed']

   colors = context.driver.find_elements(*COLORS)

   for i in range(len(colors)):
       colors[i].click()
       current_color = context.driver.find_element(*CURRENT_COLOR).text
       assert actual_colors[i] == current_color, f'Error expected {actual_colors[i]} did not match {current_color}'



