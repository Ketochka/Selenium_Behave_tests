Feature: setting the volume on vertical slider

  Scenario: user can set the volume on vertical slider
    Given page with vertical slider on it
     When user sets the value on vertical slider
     Then ensure marker position is correct