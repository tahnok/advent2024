"""
Given a "map" made of of plants on a grid, where each plot has one plant identified by letter
divide them into 'regions' where of the same letter.

Calculate the size of each region multiplied by the perimeter

We can calculate perimeter by keeping track of the number of 'neighbours' for each plot.
The perimeter is just the sum of each plot's neighbour count.

We need to track the number of regions somehow too.
"""

import sys

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

if __name__ == "__main__":
    main(sys.argv[1])
