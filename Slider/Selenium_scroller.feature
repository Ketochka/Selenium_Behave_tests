Feature: moving scroller

  Scenario: user can move scroller to make number 17 visible
    Given page with scroller and 20 numbers on it
     When user scrolls to the right and makes number 17 visible
     Then ensure number 17 is visible