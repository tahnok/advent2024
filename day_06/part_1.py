"""
doing a simulation

find the start position and move "forward"
based on direction until you encounter an
obstacle or leave the map (and exit)
keep track of visited locations in a set
return size of the set
"""

import sys

NORTH = (0,-1)
EAST = (1,0)
SOUTH = (0,1)
WEST = (-1,0)

def turn(current: tuple[int,int]) -> tuple[int,int]:
    if current == NORTH:
        return EAST
    elif current == EAST:
        return SOUTH
    elif current == SOUTH:
        return WEST
    elif current == WEST:
        return NORTH
    else:
        raise ValueError("invalid direction")

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    obstacles = set()
    curr_x = None
    curr_y = None
    width = None
    height = len(raw.strip().split("\n"))
    for y, line in enumerate(raw.strip().split("\n")):
        if width is None:
            width = len(line.strip())
        for x, char in enumerate(line.strip()):
            if char == "#":
                obstacles.add((x,y))
            elif char == "^":
                curr_x = x
                curr_y = y
    assert width
    assert curr_x
    assert curr_y

    direction = NORTH
    seen = set()
    seen.add((curr_x, curr_y))
    while True:
        curr_x += direction[0]
        curr_y += direction[1]
        if curr_x < 0 or curr_y < 0 or curr_x >= width or curr_y >= height:
            break
        if (curr_x, curr_y) in obstacles:
            curr_x -= direction[0]
            curr_y -= direction[1]
            direction = turn(direction)
        else:
            seen.add((curr_x, curr_y))

    print(len(seen))
         

if __name__ == "__main__":
    main(sys.argv[1])
