"""
Given a list of reports (a line)
check to see if the levels are "safe" (a list of numbers)
a report is safe if
- all numbers are increasing or decreasing (aka it's sorted)
- the difference between each pair of levels is at least one and less than 4
If a report is unsafe and removing one element would make it safe, consider it safe

This means if our first safety check fails, we then try a loop where we drop each element
and check for safety. If that works then the report is safe

Return the number of safe reports
"""

import sys

def safe(r: list[int]) -> bool:
    if not(sorted(r) == r) and not(list(reversed(r)) == sorted(r)):
        return False

    for i in range(len(r) - 1):
        diff = abs(r[i] - r[i + 1])
        if not(0 < diff < 4):
            return False

    return True

def main(file):
    with open(file, "r") as f:
        raw = f.readlines()

    reports = [list(map(int, line.strip().split(" "))) for line in raw]
    
    valid = 0
    for r in reports:
        if safe(r):
            valid += 1
        else:
            for i in range(len(r)):
                x = r.copy()
                del x[i]
                if safe(x):
                    valid += 1
                    break

    print(valid)

if __name__ == "__main__":
    main(sys.argv[1])
