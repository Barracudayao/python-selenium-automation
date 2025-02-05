from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
2. Practice with locators. 
Create locators + search strategy for these pages elements of Amazon Sign in pages:
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

'''
HW5.1. Go over your code and remove sleep() wherever possible. 
Replace sleep() with wait.until if needed.
'''



driver = webdriver.Chrome("/Users/seashore/PycharmProjects/Careerist7/python-selenium-automation/chromedriver 2")
driver.maximize_window()
driver.implicitly_wait(10)


# Open Amazon home pages
driver.get('https://www.amazon.com')
# redirect to sign in pages
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "nav-link-accountList-nav-line-1"))).click()


# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']").click()
driver.back()
# Email field
email = driver.find_element(By.ID, "ap_email")
email.clear()
email.send_keys("yingxukun@gmail.com")


# Continue button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "continue"))).click()

driver.back()



# Need help link
# use explicit wait

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-expander-prompt")))
element.click()

# Forgot your password link
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "auth-fpp-link-bottom"))).click()

driver.back()

# Other issues with Sign-In link
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-expander-prompt"))).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ap-other-signin-issues-link"))).click()

driver.back()

# Create your Amazon account button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "createAccountSubmit"))).click()

driver.back()


# *Conditions of use link
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                        "//a[contains(@href,'ref=ap_signin_notification_condition_of_use')]"))).click()
driver.back()

# *Privacy Notice link
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                        "//a[contains(@href, 'ref=ap_signin_notification_privacy_notice')]"))).click()

driver.quit()