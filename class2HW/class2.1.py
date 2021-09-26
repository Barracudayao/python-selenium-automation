

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").click()
driver.back()
# Email field
email = driver.find_element(By.ID, "ap_email")
email.clear()
email.send_keys("yingxukun@gmail.com")
sleep(2)

# Continue button
driver.find_element(By.ID, "continue").click()
sleep(1)
driver.back()
sleep(1)


# Need help link
# use explicit wait

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".a-expander-prompt")))
element.click()

# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom").click()
sleep(1)
driver.back()

# Other issues with Sign-In link
driver.find_element(By.CSS_SELECTOR, ".a-expander-prompt").click()
sleep(1)
driver.find_element(By.ID, "ap-other-signin-issues-link").click()
sleep(1)
driver.back()

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit").click()
sleep(1)
driver.back()


# *Conditions of use link
driver.find_element(By.XPATH, "//a[contains(@href,'ref=ap_signin_notification_condition_of_use')]").click()
driver.back()

# *Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href, 'ref=ap_signin_notification_privacy_notice')]").click()


driver.close()