"""
Given a list of memory sections that contain garbage mixed with
some valid mul(digit,digit) instructions
Compute the product of digits and sum them up for each memory section
BUT
Also look for do() and don't() instructions. If we're enabled (aka there's been a do)
then do collect multiplications, otherwise, ignore them.
We start enabled.
"""

import re
import sys

MUL = re.compile(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", re.MULTILINE)

def main(input: str) -> None:
    with open(input, "r") as f:
        raw = f.read()

    total = 0
    enabled = True
    for token, l, r in MUL.findall(raw):
        match token:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                total += int(l) * int(r)
    print(total)

if __name__ == "__main__":
    main(sys.argv[1])
