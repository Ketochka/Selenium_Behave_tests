Feature: selecting the maximum price

  Scenario: user can select the maximum price of something
    Given page with horizontal slider with fixed minimum 
     When user selects the maximum price equal to $170
     Then marker on slider has the correct position