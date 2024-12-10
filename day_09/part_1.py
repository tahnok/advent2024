"""
Given an input string that is a single line long
expand it out to the full 'disk layout'
This is done by alternating adding blocks to a 'disk' array
each number represents the number of blocks. We track the 
current file id when it's a file and increment every time
[0, None, None, 1, 1, 1, None, ...]
None is free space and the integer represents the file.

Next we find the first free block and save the index
then we start from the right and swap the free block
with the one on the end. Then find the next free block,
and decrement the right side until we find the next used
block and repeat until the two indexes are equal (or off by 1?)

Finally, we calculate the score by multiplying the index
in the disk with the file id and sum them up.
"""

import sys

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

    disk = []
    free = False
    file_id = 0
    for size in raw.strip():
        size = int(size)
        if free:
            disk.extend([None] * size)
        else:
            disk.extend([file_id] * size)
            file_id += 1
        free = not free

    free_idx = disk.index(None)
    move_idx = len(disk) - 1
    while disk[move_idx] == None:
        move_idx -= 1


    while move_idx > free_idx:
        disk[free_idx] = disk[move_idx]
        disk[move_idx] = None
        while disk[free_idx] != None:
            free_idx += 1

        while disk[move_idx] == None:
            move_idx -= 1

    total = 0
    for i, block in enumerate(disk):
        if block == None:
            break
        total += i * block
    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
