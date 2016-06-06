Feature: selecting the minimum number of bedrooms

  Scenario: user can select the minimum number of bedrooms they can live with
    Given page with horizontal slider with fixed maximum 
     When user selects the minimum number of bedrooms equal to one
     Then number 1 is displayed