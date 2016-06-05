Feature: moving marker on incremental slider

  Scenario: user can move marker on incremental slider
    Given page with incremental slider on it
     When user mover marker to the right to set $150 as a value
     Then ensure marker has the correct position