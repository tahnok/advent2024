
"""
Given a 70x70 grid
and a list of "fallen bytes" that block your path
find the coordinates of the first byte that would
prevent you from finishing the maze.

I think this is just A* where we have some walls
that prevent us from going to that spot.

We'll loop, adding 1 byte at a time until the maze isn't
solved
"""

import sys
from tqdm import trange

#SIZE = 6
SIZE = 70
GOAL = (SIZE, SIZE)

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

    corrupt = []
    for line in raw.strip().split("\n"):
        x,y = map(int, line.split(","))
        corrupt.append((x,y))

    corrupt.reverse()
    corrupt_so_far = set()

    found = None
    for _ in trange(len(corrupt)):
        new_corrupt = corrupt.pop()
        corrupt_so_far.add(new_corrupt)
        distance = dict()
        distance[(0,0)] = 0
        to_visit = set()
        to_visit.add((0,0))

        escape = False
        while len(to_visit) > 0:
            cheapest = smallest(to_visit, distance)
            if cheapest == GOAL:
                escape = True
                break
            to_visit.remove(cheapest)

            for delta_x, delta_y in [(0,1), (0,-1), (-1,0), (1,0)]:
                neighbour = (cheapest[0] + delta_x, cheapest[1] + delta_y)
                if neighbour[0] < 0 or neighbour[0] > SIZE or neighbour[1] < 0 or neighbour[1] > SIZE:
                    continue
                if neighbour in corrupt_so_far:
                    continue
                d = distance[cheapest] + 1
                if neighbour not in distance or distance[neighbour] > d:
                    distance[neighbour] = d
                    to_visit.add(neighbour)

        if not escape:
            found = new_corrupt
            break

    
    assert found is not None
    print(f"{found[0]},{found[1]}")

if __name__ == "__main__":
    main(sys.argv[1])
