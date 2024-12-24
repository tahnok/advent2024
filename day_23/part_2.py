"""
Given (as input) a set of connections between computers like
tb-ub

Find the largest interconnected set of computers

Return the sorted list of computer names, joined with a ","

Build up a dictionary of computer to neighbour set.

Build a 
For each computer, 
"""

import sys
from collections import defaultdict

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    computer_connections = defaultdict(set)
    for pair in raw.strip().split("\n"):
        a,b = pair.split("-")
        computer_connections[a].add(b)

        computer_connections[b].add(a)

    triples = set()
    for c in computer_connections.keys():
        for other in computer_connections[c]:
            other_others = computer_connections[c].copy()
            other_others.remove(other)
            for o in other_others:
                if o in computer_connections[other]:
                    triples.add(tuple(sorted([c,o,other])))

    largest = set()
    possible = triples
    while len(possible) > 0:
        p = possible.pop()
        for computer in p:
            for neighbour in computer_connections[computer]:
                if neighbour in p:
                    continue
                new = tuple(sorted([*p, neighbour]))
                if largest == new:
                    continue
                connected = True
                for other in p:
                    if other == computer:
                        continue
                    if neighbour not in computer_connections[other]:
                        connected = False
                        break
                if connected:
                    possible.add(new)
                    if len(new) > len(largest):
                        largest = new
            



    print(",".join(sorted(list(largest))))


if __name__ == "__main__":
    main(sys.argv[1])
