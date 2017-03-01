Feature: A sample test framework

  Scenario: open a website
    Given I visit the website www.bbc.co.uk
    When I click on the news link
    Then the bbc news page is opened
