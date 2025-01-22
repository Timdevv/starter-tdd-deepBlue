import pytest
from hello import Position, Rover

@pytest.mark.parametrize("initial_direction,expected_direction", [
    ("North", "West"),
    ("West", "South"),
    ("South", "East"),
    ("East", "North"),
])
def test_rover_turns_left(initial_direction, expected_direction):
    rover = Rover(Position(0, 0), initial_direction)
    
    rover.turn_left()
    
    assert rover.direction == expected_direction 


@pytest.mark.parametrize("initial_direction,expected_direction", [
    ("North", "East"),
    ("East", "South"),
    ("South", "West"),
    ("West", "North"),
])
def test_rover_turns_right(initial_direction, expected_direction):
    rover = Rover(Position(0, 0), initial_direction)
    
    rover.turn_right()
    
    assert rover.direction == expected_direction    
