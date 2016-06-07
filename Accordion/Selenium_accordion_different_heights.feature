Feature: every accordion panel height can be different 

  Scenario: user can assure that panel height can be dependent on text in it
    Given page with 4 accordion collapsive sections of different height
     When user checks the height of first expanded panel and clicks on the second panel
     Then ensure the height of the third and second panels are not the same