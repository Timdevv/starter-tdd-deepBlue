import pytest
from hello import Position, Rover

# =============== FORWARD TESTS ===============

@pytest.mark.parametrize("direction,expected_x,expected_y", [
    ("North", 4, 3),
    ("South", 4, 1),
    ("East", 5, 2),
    ("West", 3, 2),
])
def test_rover_moves_forward(direction, expected_x, expected_y):
    initial_position = Position(4, 2)
    rover = Rover(initial_position, direction)
    
    rover.move_forward()
    
    assert rover.position.x == expected_x
    assert rover.position.y == expected_y
    assert rover.direction == direction


# =============== BACKWARD TESTS ===============


@pytest.mark.parametrize("direction,expected_x,expected_y", [
    ("North", 4, 1),
    ("South", 4, 3),
    ("East", 3, 2),
    ("West", 5, 2),
])
def test_rover_moves_backward(direction, expected_x, expected_y):
    initial_position = Position(4, 2)
    rover = Rover(initial_position, direction)
    
    rover.move_backward()
    
    assert rover.position.x == expected_x
    assert rover.position.y == expected_y
    assert rover.direction == direction
