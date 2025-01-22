from hello import Position, Rover

def test_rover_turns_left_when_facing_north():
    rover = Rover(Position(0, 0), "North")
    
    rover.turn_left()
    
    assert rover.direction == "West"

def test_rover_turns_left_when_facing_west():
    rover = Rover(Position(0, 0), "West")
    
    rover.turn_left()
    
    assert rover.direction == "South"

def test_rover_turns_left_when_facing_south():
    rover = Rover(Position(0, 0), "South")
    
    rover.turn_left()
    
    assert rover.direction == "East"

def test_rover_turns_left_when_facing_east():
    rover = Rover(Position(0, 0), "East")
    
    rover.turn_left()
    
    assert rover.direction == "North" 