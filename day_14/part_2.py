"""
Given a list of "robot" posisitions and velocities,
Print the number of robots at each grid location or a
. and the number of iterations that have elapsed.

Find the "christmas tree"
"""

import re
import sys
from collections import defaultdict

WIDTH = 101
HEIGHT = 103
# WIDTH = 11 
# HEIGHT = 7 

ROBOT = re.compile(r'[\d-]+')

def print_grid(grid: dict[tuple[int,int], int]) -> None:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            c = grid[(x,y)]
            if c == 0:
                c = "."
            print(c, end="")
        print("")

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    robots = []
    for l in raw.strip().split("\n"):
        xloc, yloc, xvel, yvel = [int(m[0]) for m in ROBOT.finditer(l)]
        loc = (xloc, yloc)
        vel = (xvel, yvel)
        robots.append((loc, vel))

    for i in range(WIDTH * HEIGHT):
        grid = defaultdict(int)
        for r_i, (loc, vel) in enumerate(robots):
            x = (loc[0] + vel[0]) % WIDTH
            y = (loc[1] + vel[1]) % HEIGHT
            robots[r_i] = ((x,y), vel)
            grid[(x, y)] += 1

        if ((i - 21) % 103 == 0) and ((i-78) % 101 == 0) :
            print_grid(grid)
            print(i + 1)
            print("=" * WIDTH)

if __name__ == "__main__":
    main(sys.argv[1])
