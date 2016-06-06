Feature: setting the best color

  Scenario: user can move marker points on red, green and blue channels and set a desired color
    Given page with colorpicker on it
     When user sets 216 on red channel
     And  user sets 81 on green channel
     And  user sets 41 on blue channel
     Then ensure RGB value is set correctly