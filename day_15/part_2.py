"""
Simulate the movement of a robot in a warehouse

The input is a "map" consistiting of walls (#), boxes (O) and the robot (@)
Walls cannot move, but the robot can push boxes around.

Walls and boxes are now "wide" in that they take up 2 tiles in the x direction.

As the robot moves, it pushes any box in front of it (and all boxes touching it)
If the robot runs into a wall, or tries to push a box into a wall nothing happens
or moves.

The second part of the input is multiple lines of moves that should all be executed,
with <>^v being left,right,up,down.

After all the moves calculate the "GPS" coordinate of each box which is the left x * 100 + y.

Return the sum of all box GPS coordinates.

For simulating the movement, we can keep the walls in a set to check for colisions.
The boxes can exist in dictionary where the keys are coordinates and the values are either
L or R depending on which half of the box they are.
When moving, we check if there's a box in the direction of the move, and if so we 'walk'
in that direction looking for all the boxes that are touching. If at the end of the robot
or boxes is empty space, we can move the whole stack (which may be just the bot or several
boxes). If the end is a wall, move to the next movement.

When moving left and right, the rules are simple, we just move both box coordinates.

Moving up/down is much harder.
Now we also have to consider the other half of any box

Consider

##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############

Move ^:

We can iteratively look for the boxes we need to move AND the "edges" of the boxes.
First we see if the move up hits a box. If so we iteratively check to see if the spot
above the left and right halves of the box contains another box or a wall. If wall,
we can't move. If box, check on the left/right halves again until we are sure all boxes
have empty space.

During this box exploration phase, keep track of all boxes. When we move, iterate over all
of the touching boxes and move them in the approriate direction
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
    
def left(p: tuple[int, int]) -> tuple[int,int]:
    return (p[0] - 1, p[1])

def right(p: tuple[int, int]) -> tuple[int,int]:
    return (p[0] + 1, p[1])

WIDTH = 1
HEIGHT = 1
def print_board(walls: set[tuple[int,int]], boxes: dict[tuple[int,int], str], robot: tuple[int,int]) -> None:
    print(" ", end="")
    for x in range(WIDTH):
        print(x, end="")
    print("")
    for y in range(HEIGHT):
        print(y, end="")
        for x in range(WIDTH):
            z = (x,y)
            p = "."
            if z in walls:
                p = "#"
            if z in boxes:
                p = boxes[z]
            if z == robot:
                p = "@"

            print(p, end="")
        print("")


def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    warehouse_map, moves = raw.split("\n\n")

    walls = set()
    robot = (0,0)
    boxes: dict[tuple[int,int], str] = dict()
    for y, line in enumerate(warehouse_map.strip().split("\n")):
        for x, tile in enumerate(line.strip()):
            x = 2 * x
            if tile == "@":
                robot = (x,y)
            elif tile == "#":
                walls.add((x,y))
                walls.add((x+1,y))
            elif tile == "O":
                boxes[(x,y)] = "["
                boxes[(x+1,y)] = "]"

    for m in moves.replace("\n",""):
        one_step = step(m, robot)

        # this might be paranoia...
        if one_step in walls:
            continue
        elif not one_step in boxes:
            robot = one_step
            continue

        if m in [LEFT, RIGHT]:
            box_tip = step(m,robot)
            seen = set()
            while box_tip in boxes:
                seen.add(box_tip)
                box_tip = step(m, box_tip)
            if box_tip in walls:
                continue
            # move box
            if one_step in boxes:
                side = boxes[one_step]
                del boxes[one_step]
                seen.remove(one_step)
                for k in seen:
                    s = boxes[k]
                    boxes[k] = "[" if s == "]" else "]"

                boxes[box_tip] = "[" if side == "]" else "]"
            # move robot
            robot = one_step
        else:
            box_side = boxes.get(one_step, None)
            assert box_side is not None

            seen = set()
            seen.add(one_step)

            to_check = set()
            to_check.add(step(m, one_step))

            other = left if box_side == "]" else right
            x = other(one_step)
            seen.add(x)
            to_check.add(step(m, x))

            wall_found = False
            while len(to_check) > 0:
                x = to_check.pop()
                if x in walls:
                    wall_found = True
                    break
                if x in boxes:
                    seen.add(x)
                    to_check.add(step(m,x))

                    box_side = boxes[x]
                    other = left if box_side == "]" else right
                    y = other(x)
                    
                    if not y in seen:
                        seen.add(y)
                        to_check.add(step(m, y))

            if wall_found:
                continue

            # move all seen boxes
            new_boxes = dict()
            for coord in seen:
                side = boxes[coord]
                del boxes[coord]
                new_boxes[step(m, coord)] = side
            for coord, side in new_boxes.items():
                boxes[coord] = side
            # move robot
            robot = one_step
            

    gps_sum = sum(k[1] * 100 + k[0] for k,v in boxes.items() if v == "[")
    print(gps_sum)

if __name__ == "__main__":
    main(sys.argv[1])
