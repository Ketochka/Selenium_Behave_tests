Feature: double clicking on collapsive panels to display and hide section information

  Scenario: user can click on a desired section on accordion to display  and hide section information
    Given page with 4 accordion collapsive sections on it
     When user ensures section 1 is expanded and clicks to collapse
     And  user ensures all four sections are collapsed and clicks on section 1 to expand
     Then ensure information of section 1 is displayed
