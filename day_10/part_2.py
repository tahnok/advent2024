"""
Given a "topographic map" which is a grid of numbers representing heights
find the number of paths from 0 that increase by one based on the heights of
4 'cells' around the current location.
Return the total number of paths

Parse the map into a dict[(x,y), height]
and collect the locations of 0s as trail heads
"""

import sys

def step(topo: dict[tuple[int,int], int], height: int, x: int, y: int) -> int:
    if height == 9:
        return 1
    next_height = height + 1
    total = 0
    if topo.get((x - 1, y), -1) == next_height:
        total += step(topo, next_height, x-1,y)
    if topo.get((x + 1, y), -1) == next_height:
        total += step(topo, next_height, x+1,y)
    if topo.get((x, y-1), -1) == next_height:
        total += step(topo, next_height, x,y-1)
    if topo.get((x, y+1), -1) == next_height:
        total += step(topo, next_height, x,y+1)

    return total


def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    topo = dict()
    trailheads = []
    for y, line in enumerate(raw.strip().split("\n")):
        for x, height in enumerate(line.strip()):
            if height == ".":
                continue
            height = int(height)
            topo[(x,y)] = height
            if height == 0:
                trailheads.append((x,y))
    
    total = 0
    for x,y in trailheads:
        total += step(topo, 0, x, y)


    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
