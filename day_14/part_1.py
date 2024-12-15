"""
Given a list of "robot" posisitions and velocities,
calculate the final location of each robot after 100 seconds / ticks.
Given a grid size to simulate.
Count the number of robots in each quadrant, ignoring robots
on the "axis" lines created by spliting up the quadrants
Return the product of the quadrant counts

The grid "wraps" around, so we can simualte the final position
of the robots by multiplying velocity by the number of ticks and
adding to the start position, and then taking that mod width/height.

Iterate over the final list of posistions, counting robots in each
quadrant.
"""

import re
import sys

WIDTH = 101
HEIGHT = 103

ROBOT = re.compile(r'[\d-]+')

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    robots = []
    for l in raw.strip().split("\n"):
        xloc, yloc, xvel, yvel = [int(m[0]) for m in ROBOT.finditer(l)]
        loc = (xloc, yloc)
        vel = (xvel, yvel)
        robots.append((loc, vel))

    final_robots = []
    for loc, vel in robots:
        x = (loc[0] + vel[0] * 100) % WIDTH
        y = (loc[1] + vel[1] * 100) % HEIGHT
        final_robots.append((x,y))

    ul = 0
    ur = 0
    ll = 0
    lr = 0
    for x,y in final_robots:
        if x < WIDTH // 2 and y < HEIGHT // 2:
            ul += 1
        if x > WIDTH // 2 and y > HEIGHT // 2:
            lr += 1
        if x < WIDTH // 2 and y > HEIGHT // 2:
            ll += 1
        if x > WIDTH // 2 and y < HEIGHT // 2:
            ur += 1


    print(ul * ur * ll * lr)
if __name__ == "__main__":
    main(sys.argv[1])
