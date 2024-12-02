"""
Given a list of reports (a line)
check to see if the levels are "safe" (a list of numbers)
a report is safe if
- all numbers are increasing or decreasing (aka it's sorted)
- the difference between each pair of levels is at least one and less than 4
Return the number of safe reports
"""

import sys

def main(file):
    with open(file, "r") as f:
        # can I loop over the file line by line instead?
        raw = f.readlines()

    reports = [list(map(int, line.strip().split(" "))) for line in raw]
    
    valid = 0
    for r in reports:
        if not(sorted(r) == r) and not(list(reversed(r)) == sorted(r)):
            continue

        # wish we had labeled break or something to break out of both loops
        line_valid = True
        for i in range(len(r) - 1):
            diff = abs(r[i] - r[i + 1])
            if not(1 < diff < 4):
                line_valid = False
                break

        if line_valid:
            valid += 1

    print(valid)

if __name__ == "__main__":
    main(sys.argv[1])
