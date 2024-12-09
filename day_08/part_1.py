"""
Given a "map" which is a grid
look for "antennas" that are identified with a letter or number
and add it's location to a dict of id to location list

for each pair of locations for a given antenna calculate their
distance in x,y. Then see if adding and subtracting the offset
to each pair is "on the map" (aka greater zero and less than the max
max size in x and y). If so, add to a set

return the size of the set
"""

import sys
from collections import defaultdict
from itertools import combinations

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

    def valid(new: tuple[int,int], l: tuple[int, int], r: tuple[int,int]) -> bool:
        return new != l and new != r and new[0] >= 0 and new[1] >= 0 and new[0] < width and new[1] < height

    antinodes = set()
    for antenna, coords in antenna_map.items():
        for l,r in combinations(coords, 2):
            delta_x = l[0] - r[0]
            delta_y = l[1] - r[1]
            new = l[0] + delta_x, l[1] + delta_y
            if valid(new, l, r):
                antinodes.add(new)
            new = l[0] - delta_x, l[1] - delta_y
            if valid(new, l, r):
                antinodes.add(new)
            new = r[0] + delta_x, r[1] + delta_y
            if valid(new, l, r):
                antinodes.add(new)
            new = r[0] - delta_x, r[1] - delta_y
            if valid(new, l, r):
                antinodes.add(new)
    print(len(antinodes))


if __name__ == "__main__":
    main(sys.argv[1])
