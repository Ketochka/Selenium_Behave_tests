Feature: accordion set of panels width can be adjusted with help of dragging point

  Scenario: user can change the width of accordion panel set
    Given page with 4 accordion collapsive sections on it and a dragging point
     When user checks current panels width and decreases it with a dragging point
     And  user makes the panel set to be much wider and a bit higher
     Then ensure new width and height are set correctly