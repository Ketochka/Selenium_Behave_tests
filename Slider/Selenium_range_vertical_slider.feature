Feature: deciding the price range on vertical slider

  Scenario: user can decide the range on vertical slider
    Given page with vertical slider and two markers on it
     When user prepares the bottom marker
     And  user moves top marker and determines the upper value
     And  user moves bottom marker and determines the lower value
     Then ensure price range is set correctly