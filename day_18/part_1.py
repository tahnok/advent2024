"""
Given a 70x70 grid
and a list of "fallen bytes" that block your path
find the shortest path from 0,0 to 70,70

I think this is just A* where we have some walls
that prevent us from going to that spot.
"""

import sys

#SIZE = 6
SIZE = 70
GOAL = (SIZE, SIZE)

#OFFSET = 12
OFFSET = 1024

def smallest(candidates: set[tuple[int,int]], dist: dict[tuple[int,int], int]) -> tuple[int,int]:
    small = None
    for c in candidates:
        if small is None:
            small = c
        elif dist[c] < dist[small]:
            small = c

    assert small is not None
    return small

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    corrupt = set()
    for line in raw.strip().split("\n")[:OFFSET]:
        x,y = map(int, line.split(","))
        corrupt.add((x,y))

    for y in range(SIZE):
        for x in range(SIZE):
            coord = (x,y)
            if coord in corrupt:
                continue
    distance = dict()
    distance[(0,0)] = 0
    to_visit = set()
    to_visit.add((0,0))

    while len(to_visit) > 0:
        cheapest = smallest(to_visit, distance)
        if cheapest == GOAL:
            print(distance[cheapest])
            break
        to_visit.remove(cheapest)

        for delta_x, delta_y in [(0,1), (0,-1), (-1,0), (1,0)]:
            neighbour = (cheapest[0] + delta_x, cheapest[1] + delta_y)
            if neighbour[0] < 0 or neighbour[0] > SIZE or neighbour[1] < 0 or neighbour[1] > SIZE:
                continue
            if neighbour in corrupt:
                continue
            d = distance[cheapest] + 1
            if neighbour not in distance or distance[neighbour] > d:
                distance[neighbour] = d
                to_visit.add(neighbour)

    

if __name__ == "__main__":
    main(sys.argv[1])
