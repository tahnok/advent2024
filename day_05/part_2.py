"""
Input is in two parts

first part is a list of page ordering rules
each line is a number, then a | then a number

For each line, we will build up a set of "exclusions"
to produce a dict[int, set[int]]

The second part is an "update". For each page in an update
check to see if any of the previous pages are in the exclusion
for the current page number.

If it's in order, ignore it.

If it's out of order, build up a list of exlcusions for
each page for this update from the rules/exclusioins dict

Take the page with 0 exclusions and add it to the new order.
Remove that page from the exclusions of all other pages and
loop until we've gone through all the pages.

This page list will be backwards

Add them middle page of the valid ones to the list so far.
"""

import sys

def valid(rules: dict[int, set[int]], pages: list[int]) -> bool:
    so_far = set()
    for p in pages:
        exc = rules.get(p, None)
        if exc is not None and not exc.isdisjoint(so_far):
            return False
        so_far.add(p)

    return True

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    raw_rules, raw_updates = raw.split("\n\n")

    rules = dict()
    for raw_rule in raw_rules.split("\n"):
        page, exclusion = map(int, raw_rule.split("|"))
        if page not in rules:
            rules[page] = set()
        rules[page].add(exclusion)

    total = 0
    for update in raw_updates.strip().split("\n"):
        pages = list(map(int, update.split(",")))
        if valid(rules, pages):
            continue

        # build up page list backwards
        # starting with the page that has no
        # exclusions and working backwards
        new = []
        current_rules = [(p, (rules.get(p, set()) & set(pages))) for p in pages]
        while len(current_rules) > 0:
            free = min(current_rules, key=lambda x: len(x[1]))
            assert len(free[1]) == 0, f"{free=}, {new=}"
            new.append(free[0])
            current_rules.remove(free)
            current_rules = [(p, r - set(new)) for (p,r) in current_rules]

        # doesn't matter if backwards for middle
        mid = new[len(new) // 2]
        total += mid
        
    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
