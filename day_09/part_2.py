"""
Given an input string that is a single line long
expand it out to the full 'disk layout'
This is done by alternating adding blocks to a 'disk' array
each number represents the number of blocks. We track the 
current file id when it's a file and increment every time
[0, None, None, 1, 1, 1, None, ...]
None is free space and the integer represents the file.

Try move all of each file starting from the right and going
in decreasing order of file id to a free span of blocks
looking from the left. If no space is found, move on to the
next file

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
    file_idx = []
    free_idx = []
    for size in raw.strip():
        size = int(size)
        if free:
            free_idx.append((size, len(disk)))
            disk.extend([None] * size)
        else:
            file_idx.append((file_id, size, len(disk)))
            disk.extend([file_id] * size)
            file_id += 1
        free = not free
    
    # we want the length (or start and end) of
    # each file
    # we want the length and location of each
    # block of free space
    # and we need to be able to update the free space as we go
    # [[size, start], [size, start]]
    # 
    for file_id, file_size, file_start in reversed(file_idx):
        found = False
        found_size = None
        found_start = None
        found_idx = None
        for free_idx_idx, (free_size, free_start) in enumerate(free_idx):
            if free_size >= file_size:
                found = True
                found_size = free_size
                found_start = free_start
                found_idx = free_idx_idx
                break

        if not found:
            continue

        if found_start > file_start:
            continue

        assert found_size is not None
        assert found_start is not None
        assert found_idx is not None

        # move the file on disk
        disk[found_start:found_start+file_size] = [file_id] * file_size
        # remove the old file
        disk[file_start:file_start+file_size] = [None] * file_size
        if file_size == found_size:
            del free_idx[found_idx]
        else:
            free_idx[found_idx] = (found_size - file_size, found_start + file_size)

    total = 0
    for i, block in enumerate(disk):
        if block == None:
            continue
        total += i * block
    print(total)


if __name__ == "__main__":
    main(sys.argv[1])
