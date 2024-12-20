"""
Given a list of available towels with colour given by w,u,b,r,g 
in any combination or repeat (eg: r, rr, wubrg)

and a list of patterns made up of towels

Return the number of patterns that can be made with those towels

Approach

Construct one big regex that is
(towel1|towel2|...)+

aka, any combination of at least one towel

This doesn't work because once towel1 is matched, but the rest fails, regex
won't go back to try towel2, so we need to do it ourselves

A recursive search is also taking too long on the third option.
I don't quite understand why, I think it's taking too long to parse?

But what if looked at this as a parsing problem. We can parse
brb with b,r,br in 2 ways b,r,b and br,b. But u is impossible.

Another thought: we can prune the towels we consider. br is always the same
as b and r so we don't need to look for br. But to check this we need to
do a lot of combinations...

What if we just delete all occurances of each pattern and if the result
is empty, we can make it, otherwise fail.

No, consider aa, aaa, ab and the pattern aaab. If we delete in order
then we fail.

What about memoization? if we have aa and a vs aaaaaaaab
once we do one pass to get aaaab as impossible, if we get there
again via aa or a,a we can abort immediately
"""

from tqdm import tqdm
from functools import cache
import sys

DEADENDS = set()

@cache
def recurse_match(pattern: str, towels: tuple[str]) -> int:
    """
    options is a possible towels
    for each possible towel match,
    check if recurse_match on the remainder of the pattern
    return true pattern is empty and if any of the recursive
    calls return true

    also track deadends, if we see a pattern we know we can't
    get to we can abort immediately
    """

    if pattern == "":
        return 1
    if pattern in DEADENDS:
        return 0
    total = 0
    for t in towels:
        if pattern.startswith(t):
            total += recurse_match(pattern[len(t):], towels)
    if total == 0:
        DEADENDS.add(pattern)
    return total


def main(path: str) -> None:
    with open(path) as f:
        raw = list(map(lambda l: l.strip(), f.readlines()))

    towels = tuple(raw[0].split(", "))
    patterns = raw[2:]

    total = 0
    for p in tqdm(patterns):
        DEADENDS = set()
        total += recurse_match(p, towels)

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
