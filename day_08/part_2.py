"""
Given a "map" which is a grid
look for "antennas" that are identified with a letter or number
and add it's location to a dict of id to location list

for each pair of locations for a given antenna calculate their
distance in x,y.
Then "normalize" this distance so that the delta x and delta y
don't share any common factors.
Then expand out along the entire line to each coordinate is
"on the map" (aka greater zero and less than the max
max size in x and y). If so, add to a set

return the size of the set
"""

import sys
from collections import defaultdict
from itertools import combinations
from math import gcd

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    antenna_map = defaultdict(list)
    height = len(raw.strip().split("\n"))
    width = None
    for y, line in enumerate(raw.strip().split("\n")):
        if width is None:
            width = len(line)
        for x, antenna in enumerate(line.strip()):
            if antenna == ".":
                continue
            antenna_map[antenna].append((x,y))
    assert width is not None

    def in_of_bounds(x: int, y: int) -> bool:
        return x >= 0 and y >= 0 and x < width and y < height

    antinodes = set()
    for antenna, coords in antenna_map.items():
        for l,r in combinations(coords, 2):
            delta_x = l[0] - r[0]
            delta_y = l[1] - r[1]
            d = gcd(delta_y, delta_x)
            delta_y //= d
            delta_x //= d

            new_x = l[0]
            new_y = l[1]
            while True:
                antinodes.add((new_x, new_y))
                new_x += delta_x
                new_y += delta_y
                if not in_of_bounds(new_x, new_y):
                    break
            new_x = l[0]
            new_y = l[1]
            while True:
                antinodes.add((new_x, new_y))
                new_x -= delta_x
                new_y -= delta_y
                if not in_of_bounds(new_x, new_y):
                    break
    print(len(antinodes))


if __name__ == "__main__":
    main(sys.argv[1])
