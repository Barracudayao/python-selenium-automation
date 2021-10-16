# Created by seashore at 10/9/21
#HW 6.1. Create a window handling test case from the class and verify that user can open amazon applications from Terms of Conditions
#https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088


Feature: Amazon privacy page window handle switch
  # Enter feature description here

  Scenario: User can open and close Amazon Privacy Notice
   Given Open Amazon T&C page
   When Store original windows
   And Click on Amazon Privacy Notice link
   And Switch to the newly opened window
   Then Verify Amazon Privacy Notice page is opened
   And User can close new window and switch back to original