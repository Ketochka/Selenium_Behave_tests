Feature: accordion panels can be expanded on hover

  Scenario: user can expand an accordion panel on hover
    Given page with 4 accordion collapsive sections on it
     When user hovers on second panel it becomes expanded and all the other become collapsed
     Then ensure the third panel is expanded on hover