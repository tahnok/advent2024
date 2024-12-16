"""
Simulate the movement of a robot in a warehouse

The input is a "map" consistiting of walls (#), boxes (O) and the robot (@)
Walls cannot move, but the robot can push boxes around.
As the robot moves, it pushes any box in front of it (and all boxes touching it)
If the robot runs into a wall, or tries to push a box into a wall nothing happens
or moves.

The second part of the input is multiple lines of moves that should all be executed,
with <>^v being left,right,up,down.

After all the moves calculate the "GPS" coordinate of each box which is x * 100 + y.

Return the sum of all box GPS coordinates.

For simulating the movement, we can keep the walls in a set to check for colisions.
The box locations are stored in a set as well.
When moving, we check if there's a box in the direction of the move, and if so we 'walk'
in that direction looking for all the boxes that are touching. If at the end of the robot
or boxes is empty space, we can move the whole stack (which may be just the bot or several
boxes). If the end is a wall, move to the next movement.
When moving boxes we can just delete the first box in a row and replace it with empty space.
"""

import sys

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

def step(dir: str, pos: tuple[int,int]) -> tuple[int,int]:
    x = pos[0]
    y = pos[1]
    if dir == UP:
        return (x,y-1)
    elif dir == DOWN:
        return (x,y+1)
    elif dir == LEFT:
        return (x-1,y)
    elif dir == RIGHT:
        return (x+1,y)
    else:
        raise ValueError(f"{dir=} is invalid")

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    warehouse_map, moves = raw.split("\n\n")

    walls = set()
    robot = (0,0)
    boxes = set()
    for y, line in enumerate(warehouse_map.strip().split("\n")):
        for x, tile in enumerate(line.strip()):
            if tile == "@":
                robot = (x,y)
            elif tile == "#":
                walls.add((x,y))
            elif tile == "O":
                boxes.add((x,y))

    for m in moves.replace("\n",""):
        one_step = step(m, robot)

        box_tip = step(m,robot)
        while box_tip in boxes:
            box_tip = step(m, box_tip)
        if box_tip in walls:
            continue
        # move box
        if one_step in boxes:
            boxes.remove(one_step)
            boxes.add(box_tip)
        # move robot
        robot = one_step

    gps_sum = sum(b[1] * 100 + b[0] for b in boxes)
    print(gps_sum)

if __name__ == "__main__":
    main(sys.argv[1])
