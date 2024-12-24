"""
Given (as input) a set of connections between computers like
tb-ub

Find 'sets of three' where all 3 computers are connected to each other

return how many sets of three contain a computer who's name starts with t

Looping over each connection, create a dictionary of computer to it's
connected neighbours as a set. Also add each computer name that starts
with t to a list.

For each computer in the t-list, check how many computers it's connected
to are connected to each other.
"""

import sys
from collections import defaultdict

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    computers = defaultdict(set)
    t_computers = set()
    for pair in raw.strip().split("\n"):
        a,b = pair.split("-")
        computers[a].add(b)
        computers[b].add(a)
        if a.startswith("t"):
            t_computers.add(a)
        if b.startswith("t"):
            t_computers.add(b)

    t_triples = set()
    for c in t_computers:
        for other in computers[c]:
            other_others = computers[c].copy()
            other_others.remove(other)
            for o in other_others:
                if o in computers[other]:
                    t_triples.add(tuple(sorted([c,o,other])))

    print(len(t_triples))

if __name__ == "__main__":
    main(sys.argv[1])
