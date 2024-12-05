"""
Given a grid of letters look for MAS written
- as an x, with MAS in either direction

M.M
.A.
S.S

 Return the number of times it is written.
"""

import sys

def check(word_search: list[list[str]], x: int, y: int) -> int:
    if word_search[x][y] != "A":
        return 0

    if (
            (
                (word_search[x+1][y+1] == "M" and word_search[x-1][y-1] == "S") or
                (word_search[x+1][y+1] == "S" and word_search[x-1][y-1] == "M")
            ) and
            (
                (word_search[x-1][y+1] == "M" and word_search[x+1][y-1] == "S") or
                (word_search[x-1][y+1] == "S" and word_search[x+1][y-1] == "M")
            )
        ):
        return 1

    return 0

def main(path: str) -> None:
    with open(path) as f:
        raw = f.readlines()

    word_search = [list(l.strip()) for l in raw]

    count = 0
    for x in range(len(word_search) - 2):
        for y in range(len(word_search[0]) - 2):
            count += check(word_search, x + 1, y + 1)

    print(count)

if __name__ == "__main__":
    main(sys.argv[1])
