import pytest
from hello import Rover, Position, Grid

@pytest.mark.parametrize("start_x, start_y, direction, expected_x, expected_y", [
    (49, 0, "East", -50, 0),    
    (-50, 0, "West", 49, 0),    
    (0, 49, "North", 0, -50),  
    (0, -50, "South", 0, 49),   
])
def test_move_beyond_boundary(start_x, start_y, direction, expected_x, expected_y):
    grid = Grid()
    position = Position(start_x, start_y)
    rover = Rover(position, direction, grid)
    
    rover.move_forward()
    
    assert rover.position.x == expected_x
    assert rover.position.y == expected_y
    assert rover.direction == direction
