class Grid:
    def __init__(self, size=100):
        self.size = size
        self.half_size = size // 2

    def normalize_coordinate(self, coord):
        if coord >= self.half_size:
            return coord - self.size
        elif coord < -self.half_size:
            return coord + self.size
        return coord

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rover:
    def __init__(self, position, direction, grid=None):
        self.position = position
        self.direction = direction
        self.grid = grid if grid is not None else Grid()
    
    def move_forward(self):
        new_position = Position(self.position.x, self.position.y)
        if self.direction == "North":
            new_position.y += 1
        elif self.direction == "South":
            new_position.y -= 1
        elif self.direction == "East":
            new_position.x += 1
        elif self.direction == "West":
            new_position.x -= 1

        new_position.x = self.grid.normalize_coordinate(new_position.x)
        new_position.y = self.grid.normalize_coordinate(new_position.y)
        self.position = new_position
        
    def move_backward(self):
        new_position = Position(self.position.x, self.position.y)
        if self.direction == "North":
            new_position.y -= 1
        elif self.direction == "South":
            new_position.y += 1
        elif self.direction == "East":
            new_position.x -= 1
        elif self.direction == "West":
            new_position.x += 1

        new_position.x = self.grid.normalize_coordinate(new_position.x)
        new_position.y = self.grid.normalize_coordinate(new_position.y)
        self.position = new_position
    
    def turn_left(self):
        if self.direction == "North":
            self.direction = "West"
        elif self.direction == "West":
            self.direction = "South"
        elif self.direction == "South":
            self.direction = "East"
        elif self.direction == "East":
            self.direction = "North"
    
    def turn_right(self):
        if self.direction == "North":
            self.direction = "East"
        elif self.direction == "East":
            self.direction = "South"
        elif self.direction == "South":
            self.direction = "West"
        elif self.direction == "West":
            self.direction = "North"

    def execute_commands(self, commands):
        command_map = {
            'F': self.move_forward,
            'B': self.move_backward,
            'L': self.turn_left,
            'R': self.turn_right
        }
        
        for command in commands:
            if command in command_map:
                command_map[command]()
            else:
                print(f"Commande invalide et ignorée: {command}")

