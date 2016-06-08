Feature: accordion panels can sorted

  Scenario: user can change the order of panels with drag and drop
    Given page with 4 accordion sortable sections on it
     When user selects panel 4 and moves it to the position of panel 1
     Then ensure panel 4 is placed on the top of all other panels