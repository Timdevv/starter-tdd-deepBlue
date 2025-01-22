Feature: Moving forward
Scenario: Facing North
  Given The rover has position (x=4, y=2) and facing North
  When Rover moves forward
  Then The rover has position (x=4, y=3) and facing North

Scenario: Facing South
  Given The rover has position (x=4, y=2) and facing South
  When Rover moves forward
  Then The rover has position (x=4, y=1) and facing South

Scenario: Facing East
  Given The rover has position (x=4, y=2) and facing East
  When Rover moves forward
  Then The rover has position (x=5, y=2) and facing East

Scenario: Facing West
  Given The rover has position (x=4, y=2) and facing West
  When Rover moves forward
  Then The rover has position (x=3, y=2) and facing West

Feature: Moving backward
Scenario: Facing North
  Given The rover has position (x=4, y=2) and facing North
  When Rover moves backward
  Then The rover has position (x=4, y=1) and facing North

Scenario: Facing South
  Given The rover has position (x=4, y=2) and facing South
  When Rover moves backward
  Then The rover has position (x=4, y=3) and facing South

Scenario: Facing East
  Given The rover has position (x=4, y=2) and facing East
  When Rover moves backward
  Then The rover has position (x=3, y=2) and facing East

Scenario: Facing West
  Given The rover has position (x=4, y=2) and facing West
  When Rover moves backward
  Then The rover has position (x=5, y=2) and facing West

Feature: Turning
Scenario: Turn right from North
  Given The rover is facing North
  When Rover turns right
  Then The rover is facing East

Scenario: Turn right from East
  Given The rover is facing East
  When Rover turns right
  Then The rover is facing South

Scenario: Turn right from South
  Given The rover is facing South
  When Rover turns right
  Then The rover is facing West

Scenario: Turn right from West
  Given The rover is facing West
  When Rover turns right
  Then The rover is facing North

Scenario: Turn left from North
  Given The rover is facing North
  When Rover turns left
  Then The rover is facing West

Scenario: Turn left from West
  Given The rover is facing West
  When Rover turns left
  Then The rover is facing South

Scenario: Turn left from South
  Given The rover is facing South
  When Rover turns left
  Then The rover is facing East

Scenario: Turn left from East
  Given The rover is facing East
  When Rover turns left
  Then The rover is facing North

Feature: Execute multiple commands
Scenario: Execute array of commands
  Given The rover has position (x=0, y=0) and facing North
  When Rover executes commands "FFRFF"
  Then The rover has position (x=2, y=2) and facing East

Scenario: Execute array with invalid commands
  Given The rover has position (x=0, y=0) and facing North
  When Rover executes commands "FFX1FF"
  Then The rover has position (x=0, y=4) and facing North

Feature: Grid bound
Scenario: Move beyond right grid boundary
  Given The rover has position (x=49, y=0) and facing East
  When Rover moves forward
  Then The rover has position (x=-50, y=0) and facing East

Scenario: Move beyond left grid boundary  
  Given The rover has position (x=-50, y=0) and facing West
  When Rover moves forward
  Then The rover has position (x=49, y=0) and facing West

Scenario: Move beyond top grid boundary
  Given The rover has position (x=0, y=49) and facing North  
  When Rover moves forward
  Then The rover has position (x=0, y=-50) and facing North

Scenario: Move beyond bottom grid boundary
  Given The rover has position (x=0, y=-50) and facing South
  When Rover moves forward
  Then The rover has position (x=0, y=49) and facing South




