Feature: selecting the number of beds

  Scenario: user can select the number of beds with the help of dropdown and slider
    Given page with horizontal slider with dropdown
     When user selects the desired number of beds equal to 5
     And  user selects the desired number of beds equal to 1
     Then 1 bed is a selected option