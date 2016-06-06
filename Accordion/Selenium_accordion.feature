Feature: clicking on collapsive panels to display section information

  Scenario: user can click on a desired section on accordion to display section information
    Given page with 4 accordion sections on it
     When user clicks on section 2
     Then ensure information of section 2 is displayed and section 1 is collapsed