
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/seashore/PycharmProjects/Careerist7/"
                                          "python-selenium-automation/chromedriver 2")
driver.maximize_window()
driver.implicitly_wait(10)


# 3. Create a test case for Help search using python & selenium script

# Test Case:
# User can search for solutions of Cancelling an order on Amazon
# 1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
driver.get("https://www.amazon.com/gp/help/customer/display.html")
sleep(1)
# 2. Use “Search Help Library” field and search for Cancel order:
element = driver.find_element(By.ID, "helpsearch")
element.clear()
element.send_keys("Cancel order")
sleep(2)
# 3. Emulate hitting keyboard ENTER btn with send_keys command (here’s how)
element.send_keys(Keys.RETURN)
sleep(1)

# 4. Verify that ‘Cancel Items or Orders’ text is present
actual_text = "Cancel Items or Orders"
expected_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
assert expected_text == actual_text, f'Expect "Cancel Items or Orders" , but get {expected_text}'


driver.close()