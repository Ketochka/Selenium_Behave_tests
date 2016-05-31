Feature: selecting date range

  Scenario: user can select from and to date
    Given page with two date select blocks
     When user selects from date
     And  user selects to date
     Then date range becomes determined