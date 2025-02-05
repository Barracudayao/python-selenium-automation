'''
1. Find the most optimal locators for Create Account (Registration) pages elements:
'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(executable_path= "/Users/seashore/PycharmProjects/Careerist7/python-selenium-automation/chromedriver 2")
driver.maximize_window()
driver.implicitly_wait(30)

# open amazon creat account pages
driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to="
           "https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26gclid%3DCjwKCAjw-sqKBhBjEiwAVaQ9a1jPaTxnlbMD1T2ZELcSzxfbMaMQCXXhEwbQ9I1xwCK1tLvhuEC8oBoCsUcQAvD_"
           "BwE%26hvadid%3D381844282515%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9028321%26hvnetw%3Dg%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3De%26hvrand%3D3151513621281695843%26hvtargid%3Dkwd-"
           "319320701642%26hydadcr%3D15240_11283473%26ref%3Dpd_sl_1tp0wm2huj_e%26tag%3Damazusnavi-20%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_"
           "id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

sleep(1)

# amazon logo locator

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-icon.a-icon-logo"))).click()

driver.back()
sleep(1)

# creat account locator
element = driver.find_element(By.XPATH, "//div[@class='a-box-inner']/h1").text
print(element)
sleep(1)

# your name
element1 = driver.find_element(By.XPATH, "//label[@for='ap_email']").text
print(element1)
sleep(1)

#input your name locator

element2 = driver.find_element(By.ID, "ap_customer_name")
element2.clear()
element2.send_keys("barracudakun")
sleep(1)

#input Your email locator
driver.find_element(By.ID, "ap_email").send_keys("yingxukun@gmail.com")


# input password locator
driver.find_element(By.ID, "ap_password").send_keys("11111")
sleep(1)

#re-enter password locator
driver.find_element(By.ID, "ap_password_check").send_keys("11111")
sleep(1)

#Create your Amazon account locator
driver.find_element(By.ID, "continue")

#Conditions of Use locator
element3 = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_condition_of_use')]").text
print(element3)

#privacy_notice locator
element4 = driver.find_element(By.XPATH, "//a[contains(@href, 'ap_register_notification_privacy_notice')]").text
print(element4)

#Sing_in locator
element5 = driver.find_element(By.XPATH, "//a[contains(@href, 'signin')]").text
print(element5)

# Creat free account locator
element6 = driver.find_element(By.ID, "ab-registration-link").text
print(element6)

driver.close()