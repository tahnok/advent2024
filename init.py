from datetime import datetime
from pathlib import Path
import sys

def main():
    if len(sys.argv) > 1:
        raw = int(sys.argv[1])
        day = f"{raw:02}"
    else:
        now = datetime.now()
        day = now.strftime('%d')

    dir = Path.cwd() / f"day_{day}"
    print(f"created {dir}")
    dir.mkdir(exist_ok=True)
    (dir / "part_1.py").touch()
    (dir / "part_2.py").touch()

if __name__ == '__main__':
    main()
