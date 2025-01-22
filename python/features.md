# Mars Rover Test Cases

## Movement Tests

### Forward Movement
| Initial Position | Direction | Final Position | Direction (unchanged) |
|-----------------|-----------|----------------|---------------------|
| (4, 2)         | North     | (4, 3)        | North              |
| (4, 2)         | South     | (4, 1)        | South              |
| (4, 2)         | East      | (5, 2)        | East               |
| (4, 2)         | West      | (3, 2)        | West               |

### Backward Movement
| Initial Position | Direction | Final Position | Direction (unchanged) |
|-----------------|-----------|----------------|---------------------|
| (4, 2)         | North     | (4, 1)        | North              |
| (4, 2)         | South     | (4, 3)        | South              |
| (4, 2)         | East      | (3, 2)        | East               |
| (4, 2)         | West      | (5, 2)        | West               |

## Rotation Tests

### Turn Left
| Initial Direction | Final Direction |
|------------------|-----------------|
| North            | West            |
| West             | South           |
| South            | East            |
| East             | North           |

### Turn Right
| Initial Direction | Final Direction |
|------------------|-----------------|
| North            | East            |
| East             | South           |
| South            | West            |
| West             | North           |

## Grid Boundary Tests
| Initial Position | Direction | Final Position | Direction (unchanged) |
|-----------------|-----------|----------------|---------------------|
| (49, 0)        | East      | (-50, 0)      | East               |
| (-50, 0)       | West      | (49, 0)       | West               |
| (0, 49)        | North     | (0, -50)      | North              |
| (0, -50)       | South     | (0, 49)       | South              |

## Command Sequence Tests

### Multiple Valid Commands
| Initial State           | Commands | Final State            |
|------------------------|----------|------------------------|
| (0, 0), facing North   | "FFRFF"  | (2, 2), facing East   |

### Commands with Invalid Characters
| Initial State           | Commands | Final State            | Notes |
|------------------------|----------|------------------------|-------|
| (0, 0), facing North   | "FFX1FF" | (0, 4), facing North  | Invalid characters 'X' and '1' are ignored |




