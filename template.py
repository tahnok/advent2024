"""
"""

import sys

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read()

if __name__ == "__main__":
    main(sys.argv[1])
