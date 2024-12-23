"""
Using up/down/left/right/enter movements,
control a numeric, controlled by a movement keypad,
controlled by another movement keypad, finally a
movement keypad controlled by you

Figure out the sequence to enter on your keypad,
that's translated all the way to the final keypad.

Return the sum of multiplying the length of the keypad sequence
(shortest) by the number to enter (ie: 023 or 123)


Keeping track of our location in each keypad?,
figure out the move we want to make on the first one,
then how to make it on the second, then how to do it on the third,
finally how you would enter it. Repeat for each digit

We can map numbers to a grid location, so 0 is at 1,3
and we are at 2,4. That means we need to enter <,^,^ 
(which is the x delta, then y delta, mapped to left/right
based on positive/negative).

Then we need to figure out how to enter < (and the rest)
which is at 0,1 from 2,0, which is v<<

Then figure out v on the third,

then the final one (so this middle bit is recursive)

We need to hit A between the middle ones when recursing?

stopping point: the problem we're running into is that
we want to repeat keys were possible if we are on them,
so if we went up before, we should go up again, instead
of moving to left and then going up again.
"""

import sys

numpad_map = {
        '7': (0,0),
        '8': (1,0),
        '9': (2,0),
        '4': (0,1),
        '5': (1,1),
        '6': (2,1),
        '1': (0,2),
        '2': (1,2),
        '3': (2,2),
        '0': (1,3),
        'A': (2,3),
        }

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

POINT = tuple[int,int]

def numpad_moves(sequence: str, start: POINT) -> tuple[str, POINT]:
    loc = start
    moves = ""
    for s in sequence:
        dest = numpad_map[s]
        x = dest[0] - loc[0]
        y = dest[1] - loc[1]
        if x > 0:
            moves += RIGHT * x
        if y < 0:
            moves += UP * abs(y)
        if y > 0:
            moves += DOWN * y
        if x < 0:
            moves += LEFT * abs(x)
        moves += "A"
        loc = dest
    return moves, loc


directional_map = {
        UP: (1,0),
        "A": (2,0),
        LEFT: (0,1),
        DOWN: (1,1),
        RIGHT: (2,1),
    }

def directional_moves(sequence: str, start: POINT) -> tuple[str, POINT]:
    loc = start
    moves = ""
    for s in sequence:
        dest = directional_map[s]
        x = dest[0] - loc[0]
        y = dest[1] - loc[1]
        if x > 0:
            moves += RIGHT * x
        if y > 0:
            moves += DOWN * y
        if y < 0:
            moves += UP * abs(y)
        if x < 0:
            moves += LEFT * abs(x)
        moves += "A"
        loc = dest
    return (moves, loc)

def recursed_moves(sequence: str, loc_n: POINT, loc_d_1: POINT, loc_d_2: POINT) -> tuple[str, POINT,POINT,POINT]:
    moves, n_n = numpad_moves(sequence, loc_n)
    print(moves)
    moves, n_d_1 = directional_moves(moves, loc_d_1)
    print(moves)
    moves, n_d_2 = directional_moves(moves, loc_d_2)
    return moves, n_n, n_d_1, n_d_2



def main(path: str) -> None:
    with open(path) as f:
        codes = [x.strip() for x in f.readlines()]

    score = 0
    loc_n = numpad_map["A"]
    loc_d_1 = directional_map["A"]
    loc_d_2 = directional_map["A"]
    for c in codes:
        moves, n_n, n_d_1, n_d_2 = recursed_moves(c, loc_n, loc_d_1, loc_d_2)
        loc_n = n_n
        loc_d_1 = n_d_1
        loc_d_2 = n_d_2
        n_code = int(c[0:3])
        print(c,len(moves),n_code, moves)
        score += len(moves) * n_code

    print(score)

if __name__ == "__main__":
    main(sys.argv[1])
