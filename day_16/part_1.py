"""
Given a maze with a start (S) and end (E) with walls as (#)
determine the lowest 'score' possible for a path.
Moving forward adds 1 to the score, turning adds 1000 to the score
There are multiple lowest score paths.

The 'reindeer' starts facing East

This is a graph traversal problem where the edges between nodes
are either 1 or 1001

ie from
####
#C #
#>A#
#B #
####

The 'cost' to A is 1, the cost to B and C is 1001

There are always at most 3 edges out from a given spot,
although some might be into walls and thus not exist.


I think I want to implement A* or a similar 'min cost' graph algorithm
that uses a BFS.

We can keep a set of 'paths' that we build up with scores, direction and seen nodes
We copy the path for all possible options and build up the list to check as a queue?
If we reach the end that's the shortest path?

Dijkstra's algorithm might be good here.
We add each location in the maze to the unvisited set
We assign the distance of each location from the start to infinity (or None?)
We assign the distance from the origin to itself as 0
While the unvisited set is not empty:
    pick the node with the shortest distance (looping over unvisited nodes?)
    for all neighbours of current node:
        see if 
"""

import sys

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

if __name__ == "__main__":
    main(sys.argv[1])
