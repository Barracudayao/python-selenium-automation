
#Create a test case for Help search using python & selenium script
#Test Case:
#User can search for solutions of Cancelling an order on Amazon
#1. Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
#2. Use “Search Help Library” field and search for Cancel order:
#3. Emulate hitting keyboard ENTER btn with send_keys command (here’s how)
#4. Verify that ‘Cancel Items or Orders’ text is present


# Created by seashore at 9/28/21
Feature:  Help search


  Scenario: User can search for solutions of Cancelling an order on Amazon
    Given  Open Amazon Help page https://www.amazon.com/gp/help/customer/display.html
    When   Use “Search Help Library” field, search for "Cancel order" and hit enter
    Then   Verify that ‘Cancel Items or Orders’ text is present