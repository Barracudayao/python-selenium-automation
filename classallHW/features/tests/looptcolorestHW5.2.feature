# Created by seashore at 10/7/21

#HW5.2. Make a test case with a loop. You can use color selection for any product page you like.
#Create 1 test case that will loop through colors: it should click on each color and verify that color has been selected.
#Product examples with multiple colors:
#https://www.amazon.com/gp/product/B07BJKRR25/
#https://www.amazon.com/dp/B081YS2F7N



Feature: Color selection


  Scenario: Loop through colors, it should click on each color
    Given Open Amazon product B07BJKRR25 page
    Then  Verify colors has been selected