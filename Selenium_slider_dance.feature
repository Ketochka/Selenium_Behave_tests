Feature: playing with multiple sliders

  Scenario: user can increase and decrease the volume and make EQ sliders to get different shapes
    Given page with multiple sliders on it
     When user increases the volume and makes EQ shape to be concave
     And  user continues making EQ shape to be concave
     And  user lowers the volume and makes EQ shape to be convex
     And  user continues making EQ shape to be convex
     Then ensure there is actual mute