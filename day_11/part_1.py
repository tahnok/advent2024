"""
Given a set of "stones" with numbers on them, simulate
the process of "blinking" that changes the stones according to the rules

We take as input a list of numbers seperated by a space on a single line.
Parse those and store them in a deque.

Each "blink" changes the stones according to these rules in order:

    1. 0 is replaced by 1
    2. Numbers with an even number of digits (aka str(n) % 2 == 0) are split
    in half with no leading zeros (1000 -> 10, 0)
    3. number is multiplied by 2024

We will iterate over the items of the deque and make a new deque 25 times.

Return the number of stones after 25 "blinks"
"""

import sys
from collections import deque

def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        half = len(str_stone) // 2
        return [int(str_stone[0:half]), int(str_stone[half:])]

    return [stone * 2024]

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    stones = deque()
    for stone in map(int, raw.strip().split(" ")):
        stones.append(stone)

    for i in range(25):
        new_stones = deque()
        for stone in stones:
            for n in blink(stone):
                new_stones.append(n)

        stones = new_stones

    print(len(stones))

if __name__ == "__main__":
    main(sys.argv[1])
