# Created by seashore at 10/9/21

#HW5.3.*[Not required]. Make a test case to verify that every product on the Wholefoods page has a text ‘Regular’
# and a product name: https://www.amazon.com/wholefoodsdeals
#NOTE: ONLY USE BOTTOM SECTION:


Feature: Wholefoods page


  Scenario: Wholefoods page has a text ‘Regular’
    Given Open Wholefoods deal page
    Then Verify Wholefoods deal page has a text ‘Regular’ and a product name