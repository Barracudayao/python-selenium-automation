# Created by seashore at 9/28/21
#Create a test case using BDD that opens amazon.com, clicks on the cart icon and verifies that Your Amazon Cart is empty.

Feature: Amazon Cart


  Scenario: Amazon Cart is empty while click on cart icon
    Given Open Amazon homepage
    When  Click on the cart icon
    Then  Verifies that Your Amazon Cart is empty

