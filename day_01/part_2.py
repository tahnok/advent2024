"""
We're given a list of pairs of numbers.
We want to count the number of times an item on the left
appears on the right. We then multiply the left number by the
number of occurances to make a list.
Then we take the sum of those
"""

import sys

def main(input: str):
    with open(input, "r") as f:
        raw = f.readlines()
    left = []
    right = dict()
    for line in raw:
        l, r = map(lambda x: int(x), line.strip().split("   "))
        left.append(l)
        if r in right:
            right[r] += 1
        else:
            right[r] = 1


    result = []
    for l in left:
        if l in right:
            result.append(l * right[l])
        else:
            result.append(0)

    print(sum(result))

if __name__ == "__main__":
    main(sys.argv[1])
