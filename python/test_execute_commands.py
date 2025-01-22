from hello import Position, Rover

def test_rover_executes_multiple_commands():
    initial_position = Position(0, 0)
    rover = Rover(initial_position, "North")
    
    rover.execute_commands("FFRFF")
    
    assert rover.position.x == 2
    assert rover.position.y == 2
    assert rover.direction == "East"

def test_rover_ignores_invalid_commands():
    initial_position = Position(0, 0)
    rover = Rover(initial_position, "North")
    
    rover.execute_commands("FFX1FF")
    
    assert rover.position.x == 0
    assert rover.position.y == 4
    assert rover.direction == "North" 