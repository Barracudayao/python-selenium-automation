from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

'''
2. Practice with locators. 
Create locators + search strategy for these page elements of Amazon Sign in page:
Amazon logo
Email field
Continue button
Need help link
Forgot your password link
Other issues with Sign-In link
Create your Amazon account button
*Conditions of use link
*Privacy Notice link
'''

driver = webdriver.Chrome("/Users/seashore/PycharmProjects/Careerist7/python-selenium-automation/chromedriver 2")
driver.maximize_window()
driver.implicitly_wait(10)


# Open Amazon home page
driver.get('https://www.amazon.com')
# redirect to sign in page
driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
sleep(1)
# Amazon logo
driver.find_element(By.ID, "//i[@class='a-icon a-icon-logo']").click()
driver.back()
# Email field

# Continue button
# Need help link
# Forgot your password link
# Other issues with Sign-In link
# Create your Amazon account button
# *Conditions of use link
# *Privacy Notice link
