"""
It's time to implement a weird computer (or maybe a turing machine?)

Computer operates on 3 bit data/instructions (part of the input)
like 0,1,5,4,3,0

The computer has 3 registers (A,B,C) that can store any number (not just 3 bit)

There's an instruction pointer (IP) that points to the current instruction.
Except for one instruction (JNZ), IP increase by 2 after each execution.

We look at 2 numbers per instruction. The first is the opcode,
the second is the operand. 

I think the program halts if the IP is out of bounds, either by incrementing
past the end or jumping out of bounds. I don't think we should ever read an 
operand out of bounds, but maybe...

Operands are either 'literal' or 'combo', as specified in the instruction.
Literals are the value of the operand (ie: 0 is 0)

Combo operands follow these rules:
    - 0,1,2,3 are literals
    - 4 is register A
    - 5 is register B
    - 6 is register C
    - 7 is RESERVED and shouldn't occur

Operators are as follows:

    0: ADV is DIVISION
    numerator is A register, denominator is 2^(combo operand)
    division is TRUNCATED and stored in A

    1: BXL is BITWISE XOR
    B register and literal operand, stored in B

    2: BST is combo operand mod 8 and stored in B

    3: JNZ is jump not zero
    if A is zero, do nothing
    else set IP to literal operand

    4: BXC is bitwise XOR of B and C stored in B
    (ignore operand)

    5: OUT calculate value of combo operator mod 8 and then
    output the value. Multiple output values are printed seperated by ,

    6: BDV is DIVISION but with B

    7: CDV is DIVISION but with C


This will be implemented as a class that has a registers A, B, C, an IP...

I want a function I can call that returns the new state as a new object without
mutation (for debugging) but maybe we can just have step() called until we raise/return
a stop execution flag.

First thing, let's try to brute force finding a value for A such that
the output is the same as the program
"""

import sys

ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]):
        self.ip: int = 0
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.out: list[int] = []

    def step(self) -> bool:
        try:
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
        except IndexError:
            return True

        if opcode == ADV:
            self.a = self.div(operand, self.a)
            self.ip += 2
        elif opcode == BDV:
            self.b = self.div(operand, self.a)
            self.ip += 2
        elif opcode == CDV:
            self.c = self.div(operand, self.a)
            self.ip += 2
        elif opcode == BXL:
            self.b = self.b ^ operand
            self.ip += 2
        elif opcode == BST:
            self.b = self.combo(operand) % 8
            self.ip += 2
        elif opcode == JNZ:
            if self.a == 0:
                self.ip += 2
            else:
                self.ip = operand
        elif opcode == BXC:
            self.b = self.b ^ self.c
            self.ip += 2
        elif opcode == OUT:
            out = self.combo(operand) % 8
            if self.program[len(self.out)] != out:
                return True
            self.out.append(out)
            self.ip += 2
        else:
            raise ValueError(f"Invalid {opcode=}")

        return False

    def div(self, operand: int, register: int) -> int:
        return register // 2**self.combo(operand)

    def combo(self, operand: int) -> int:
        if operand in [0,1,2,3]:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        elif operand == 7:
            raise ValueError("Got 7 as combo operand!")
        else:
            raise ValueError(f"Invalid {operand=}")

    def run(self) -> None:
        while True:
            halted = self.step()
            if halted:
                break

    def is_quine(self) -> bool:
        return self.out == self.program

from tqdm import tqdm

def main(path: str) -> None:
    with open(path) as f:
        raw = f.readlines()

    a = 0
    b = int(raw[1].split(":")[1])
    c = int(raw[2].split(":")[1])

    program = list(map(int, raw[4].split(":")[1].strip().split(",")))

    pbar = tqdm()
    while True:
        comp = Computer(a,b,c,program)
        comp.run()
        pbar.update(1)
        if comp.is_quine():
            pbar.close()
            print(",".join(map(str,comp.out)))
            print(a)
            break
        a += 1

if __name__ == "__main__":
    main(sys.argv[1])
