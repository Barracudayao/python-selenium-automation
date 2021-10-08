# Created by seashore at 9/29/21
# HW4.1 Create a test case that will open amazon BestSellers page: https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers
#And verify there are 5 links:


Feature: Bestseller page

  Scenario: Bestsellers page 5 links
    Given Open amazon Bestsellers page
    Then  Verify there are 5 links