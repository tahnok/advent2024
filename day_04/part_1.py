"""
Given a grid of letters look for XMAS written
 - forward
 - up
 - down
 - all 4 diagonals

 and consider it written backwards for all of the above

 Return the number of times it is written.

AAAX catch with down left
AAMA
AAAA
SAAA


given a coordinate x,y, check if it's X, otherwise continue
if it's x, then we look in all 8 directions for MAS
"""

import sys

def check(word_search: list[list[str]], x: int, y: int) -> int:
    if word_search[x][y] != "X":
        return 0

    matches = 0
    # 0 degrees / aka flat straight
    if y + 3 < len(word_search[x]):
        if word_search[x][y+1] == "M" and word_search[x][y+2] == "A" and word_search[x][y+3] == "S":
            matches += 1

    # down right
    if y + 3 < len(word_search[x]) and x + 3 < len(word_search):
        if word_search[x+1][y+1] == "M" and word_search[x+2][y+2] == "A" and word_search[x+3][y+3] == "S":
            matches += 1

    # down
    if x + 3 < len(word_search):
        if word_search[x+1][y] == "M" and word_search[x+2][y] == "A" and word_search[x+3][y] == "S":
            matches += 1

    # down left
    if y - 3 >= 0 and x + 3 < len(word_search):
        if word_search[x+1][y-1] == "M" and word_search[x+2][y-2] == "A" and word_search[x+3][y-3] == "S":
            matches += 1


    # left (or backwards)
    if y - 3 >= 0:
        if word_search[x][y-1] == "M" and word_search[x][y-2] == "A" and word_search[x][y-3] == "S":
            matches += 1


    # up left
    if y - 3 >= 0 and x - 3 >= 0:
        if word_search[x-1][y-1] == "M" and word_search[x-2][y-2] == "A" and word_search[x-3][y-3] == "S":
            matches += 1

    # up
    if x - 3 >= 0:
        if word_search[x-1][y] == "M" and word_search[x-2][y] == "A" and word_search[x-3][y] == "S":
            matches += 1

    # up right
    if y + 3 < len(word_search[x]) and x - 3 >= 0:
        if word_search[x-1][y+1] == "M" and word_search[x-2][y+2] == "A" and word_search[x-3][y+3] == "S":
            matches += 1

    return matches

def main(path: str) -> None:
    with open(path) as f:
        raw = f.readlines()

    word_search = [list(l.strip()) for l in raw]

    count = 0
    for x in range(len(word_search)):
        for y in range(len(word_search[0])):
            count += check(word_search, x, y)

    print(count)

if __name__ == "__main__":
    main(sys.argv[1])
