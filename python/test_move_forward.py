from hello import Position, Rover

def test_rover_moves_forward_when_facing_north():
    
    initial_position = Position(4, 2)
    rover = Rover(initial_position, "North")
    
    rover.move_forward()
    
    assert rover.position.x == 4
    assert rover.position.y == 3
    assert rover.direction == "North"

def test_rover_moves_forward_when_facing_south():
    initial_position = Position(4, 2)
    rover = Rover(initial_position, "South")
    
    rover.move_forward()
    
    assert rover.position.x == 4
    assert rover.position.y == 1
    assert rover.direction == "South"

def test_rover_moves_forward_when_facing_east():
    initial_position = Position(4, 2)
    rover = Rover(initial_position, "East")
    
    rover.move_forward()
    
    assert rover.position.x == 5
    assert rover.position.y == 2
    assert rover.direction == "East"

def test_rover_moves_forward_when_facing_west():
    initial_position = Position(4, 2)
    rover = Rover(initial_position, "West")
    
    rover.move_forward()
    
    assert rover.position.x == 3
    assert rover.position.y == 2
    assert rover.direction == "West"
    













