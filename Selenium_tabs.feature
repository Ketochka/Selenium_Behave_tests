Feature: navigating through tabs

  Scenario: user can navigate through tabs by clicking on them
    Given page with three tabs on it
     When user clicks on the second and then on the third tab
     Then second and third tab are displayed respectively