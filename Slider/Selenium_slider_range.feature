Feature: selecting price range on slider

  Scenario: user can select price range on slider
    Given page with horizontal slider with two markers on it
     When user moves left slider and selects value $14
     And  user moves right slider and selects value $85
     Then ensure marker positions on slider are correct