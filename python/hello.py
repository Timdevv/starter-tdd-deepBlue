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

