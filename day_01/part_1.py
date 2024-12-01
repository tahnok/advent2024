"""
We're given a list of pairs of numbers.
We want to sort them and then take the difference between each pair
once both lists are sorted.
Then we take the sum of those
"""

import sys

def main(input: str):
    with open(input, "r") as f:
        raw = f.readlines()
    left = []
    right = []
    for line in raw:
        l, r = line.strip().split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    result = []
    for i in range(len(left)):
        result.append(abs(left[i] - right[i]))

    print(sum(result))

if __name__ == "__main__":
    main(sys.argv[1])
