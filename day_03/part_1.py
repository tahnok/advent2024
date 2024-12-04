"""
Given a list of memory sections that contain garbage mixed with
some valid mul(digit,digit) instructions
Compute the product of digits and sum them up for each memory section
"""

import re
import sys

MUL = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

def main(input: str) -> None:
    with open(input, "r") as f:
        raw = f.readlines()

    # consider using multi match to avoid double loops
    total = 0
    for line in raw:
        for l, r in MUL.findall(line):
            total += int(l) * int(r)
    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
