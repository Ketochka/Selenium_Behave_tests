Feature: custom icons can be shown/hidden by click on "Toggle icons" button

  Scenario: user can show/hide custom icons
    Given page with 4 accordion collapsive sections on it and Toggle icons button
     When user clicks on Toggle icons button and icons disappear
     And  user clicks on Toggle icons button again
     Then ensure custom icons are visible