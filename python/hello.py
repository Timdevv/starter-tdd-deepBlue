
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rover:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
    
    def move_forward(self):
        if self.direction == "North":
            self.position.y += 1
        elif self.direction == "South":
            self.position.y -= 1
        elif self.direction == "East":
            self.position.x += 1
        elif self.direction == "West":
            self.position.x -= 1
    
    def move_backward(self):
        if self.direction == "North":
            self.position.y -= 1
        elif self.direction == "South":
            self.position.y += 1
        elif self.direction == "East":
            self.position.x -= 1
        elif self.direction == "West":
            self.position.x += 1

