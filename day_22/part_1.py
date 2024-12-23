"""
Calculate the 2000th "Secret number" for 
each of the seed values in the input

Calculation is as follows for each round:
    - multiply by 64 / left shift by 6
    - dividing by 32 / right shift by 5
    - multiply by 2048 / left shift by 11
between each operation, xor with input and take
result mod 16777216, which is the same as doing
AND (2^24 - 1)


return the sum of the 2000th numbers
"""

import sys

PRUNE_MASK = 2**24 - 1

def pseudorandom(seed: int) -> int:
    result = seed
    result = ((result << 6) ^ result) & PRUNE_MASK
    result = ((result >> 5) ^ result) & PRUNE_MASK
    result = ((result << 11) ^ result) & PRUNE_MASK

    return result

def iterated(seed: int) -> int:
    r = seed
    for _ in range(2000):
        r = pseudorandom(r)
    return r

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()
    
    seeds = map(int, raw.strip().split("\n"))

    result = 0
    for s in seeds:
        result += iterated(s)

    print(result)

if __name__ == "__main__":
    main(sys.argv[1])
