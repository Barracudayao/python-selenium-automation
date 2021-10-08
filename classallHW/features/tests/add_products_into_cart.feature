# Created by seashore at 9/29/21
#HW 4.2 Create your own test case to add any product you want into the cart, and make sure it’s there
# (check for the number of items in the cart OR open the cart and verify it’s there, up to you!)



Feature: Add products into cart


  Scenario: Add any product into the cart, and make sure it’s there
    Given Open Amazon homepage
    When Input mug in the searchbar and enter
    And  Pick first mug from the list and click
    And  Click "Add to Cart" button
    Then Verify number of items in the cart

