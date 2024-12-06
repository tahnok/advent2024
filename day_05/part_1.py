"""
Input is in two parts

first part is a list of page ordering rules
each line is a number, then a | then a number

For each line, we will build up a set of "exclusions"
to produce a dict[int, set[int]]

The second part is an "update". For each page in an update
check to see if any of the previous pages are in the exclusion
for the current page number. If we get to the end, add the middle page
to the total so far.
"""

import sys

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
        so_far = set()
        valid = True
        for p in pages:
            exc = rules.get(p, None)
            if exc is not None and not exc.isdisjoint(so_far):
                valid = False
                break
            so_far.add(p)

        if valid:
            mid = pages[len(pages) // 2]
            total += mid


    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
