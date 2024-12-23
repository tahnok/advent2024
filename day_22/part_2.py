"""
Calculate the 2000 "secret number" for 
each of the seed values in the input

Calculation is as follows for each round:
    - multiply by 64 / left shift by 6
    - dividing by 32 / right shift by 5
    - multiply by 2048 / left shift by 11
between each operation, xor with input and take
result mod 16777216, which is the same as doing
AND (2^24 - 1)

Take the digit in the 1s position as the actual price
for each buyer's secret numbers.

Calculate the changes between each price and record
the 4 previous changes, along with the current price in a dict
eg: (-2,1,-1,3) -> 7

Also record each quad in a set

For each seen quad, take the sum of the price associated
and determine the max

return the max
"""

import sys

PRUNE_MASK = 2**24 - 1

def pseudorandom(seed: int) -> int:
    result = seed
    result = ((result << 6) ^ result) & PRUNE_MASK
    result = ((result >> 5) ^ result) & PRUNE_MASK
    result = ((result << 11) ^ result) & PRUNE_MASK

    return result

QUAD = tuple[int,int,int,int]

def prices(seed: int, changes: set[QUAD]) -> dict[QUAD, int]:
    r = seed
    prices = dict()
    last_price = seed % 10
    last_3_changes = []
    for _ in range(2000):
        r = pseudorandom(r)
        price = r % 10
        change = price - last_price
        last_3_changes.append(change)
        if len(last_3_changes) == 4:
            quad = tuple(last_3_changes)
            if quad not in prices:
                prices[quad] = price
            changes.add(quad)
            del last_3_changes[0]
        last_price = price
    return prices 

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()
    
    seeds = map(int, raw.strip().split("\n"))

    buyers = []
    quads = set()
    for s in seeds:
        buyers.append(prices(s, quads))
    
    m = 0
    for q in quads:
        n = 0
        for b in buyers:
            n += b.get(q, 0)

        if n > m:
            m = n

    print(m)

if __name__ == "__main__":
    main(sys.argv[1])
