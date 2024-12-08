"""
Given a list of equations with missing operators and a value
Check to see if the number on the right can add or multiply to get the
value on the left
Operations are evaluated from left to right, not acording to BEDMAS

For each line
split on :
on the right side, split on space
[1,2,3]
1+2+3
1+2*3
1*2+3
1*2*3

starting with the first element, call operate with remaining elements
then see if adding or multiplying equal the calibration

f([3]) = 3 1
f([3,2]) = [6, 5] 2 
f([4,3,2]) = [10, 24, 20, 9] 4
f([5, 4,3,2]) = [15, 50, 29, 120, 100, 25, 14, 45] 8
2^n
"""

import sys

def operate(incoming: list[int]) -> list[int]:
    if len(incoming) == 1:
        return incoming
    else:
        n = operate(incoming[1:])
        return [incoming[0] * x for x in n] + [incoming[0] + x for x in n] + [int(str(x) + str(incoming[0])) for x in n]

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    total = 0
    for l in raw.strip().split("\n"):
        calibrate, rest = l.strip().split(": ")
        calibrate = int(calibrate)
        values = list(reversed(list(map(int, rest.split(" ")))))
        possible = operate(values)
        if calibrate in possible:
            total += calibrate

    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
