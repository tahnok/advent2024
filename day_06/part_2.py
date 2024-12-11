"""
doing a simulation

find the start position and move "forward"
based on direction until you encounter an
obstacle or leave the map (and exit)
keep track of visited locations in a set

for each visited location place an obstacle
and try moving around again. Count the number
of modified maps that result in a loop

We can detect loops by keeping track of the
location AND direction of every spot we've visited.
(location is not enough, as we cross over spots)
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
    orig_x = None
    orig_y = None
    width = None
    height = len(raw.strip().split("\n"))
    for y, line in enumerate(raw.strip().split("\n")):
        if width is None:
            width = len(line.strip())
        for x, char in enumerate(line.strip()):
            if char == "#":
                obstacles.add((x,y))
            elif char == "^":
                orig_x = x
                orig_y = y
    assert width
    assert orig_x
    assert orig_y

    curr_x = orig_x
    curr_y = orig_y
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

    cycles = 0
    for x,y in seen:
        new_obstacles = obstacles.copy()
        new_obstacles.add((x,y))

        curr_x = orig_x
        curr_y = orig_y
        direction = NORTH
        seen = set()
        seen.add((direction, curr_x, curr_y))
        while True:
            curr_x += direction[0]
            curr_y += direction[1]
            if curr_x < 0 or curr_y < 0 or curr_x >= width or curr_y >= height:
                break
            if (curr_x, curr_y) in new_obstacles:
                curr_x -= direction[0]
                curr_y -= direction[1]
                direction = turn(direction)
            loc = (direction, curr_x, curr_y)
            if loc in seen:
                cycles += 1
                break
            seen.add(loc)
         
    print(cycles)

if __name__ == "__main__":
    main(sys.argv[1])
