Feature: moving marker point on slider

  Scenario: user can move marker point on slider
    Given page with horizontal slider on it
     When user moves slider by 410 points to the right
     Then ensure slider position is changed correctly