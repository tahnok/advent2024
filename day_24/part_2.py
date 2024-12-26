"""
Simulate logic gates

Given a list of wires named like x01, y01, z02 or abc
and a XOR, OR and AND gates, determine the output
(wires starting with z) based on the input wires

We have wires, which are either unset or have value.
A gate is 'ready' when all input wires are ready, otherwise
pending.

Track all unready gates, and loop over them looking for
ones where input wires are ready and then updating the
output wire.

When done, combine the output of the z wires (in order) into a decimal
number

Wires can be in a dict with a value of none, or 0 or 1.

gates are initially in a list that contain a struct of {in_a, in_b, op, out}

Loop over gate list (queue?)
When in_a and in_b are ready, set out according to op, then discard it.

---

Part 2: the wires SHOULD be configured as an adder

but FOUR gates are swapped. That is the gate a's output
and gate b's output are swapped.

x01 OR x02 -> z01
x03 OR x04 -> z02

Could instead be

x01 OR x02 -> z02
x03 OR x04 -> z01

Can we brute force this given the input is 45bits and we have 222 gates?

We need every combination of 4 gates from every pair of gates...

222 choose 2 = 24531

24531 choose 4 ~= 1.5e16 which is 10 quadrillion, seems to big
"""

import sys
from collections import deque, namedtuple

Gate = namedtuple('Gate', ['in_a', 'in_b', 'op', 'out'])

def main(path: str) -> None:
    with open(path) as f:
        raw = f.read().strip()

    inputs, raw_gates = raw.split("\n\n")

    wires = dict()
    for input in inputs.split("\n"):
        name, value = input.split(": ")
        wires[name] = int(value)

    gates = deque()
    for r_gate in raw_gates.split("\n"):
        in_a, op, in_b, _, out = r_gate.split(" ")
        gates.append(Gate(in_a, in_b, op, out))

    print(len(gates))
    while len(gates) > 0:
        gate = gates.popleft()
        in_a_val = wires.get(gate.in_a, None)
        in_b_val = wires.get(gate.in_b, None)
        if in_a_val is not None and in_b_val is not None:
            val = None
            if gate.op == "AND":
                val = in_a_val & in_b_val
            elif gate.op == "OR":
                val = in_a_val | in_b_val
            else:
                val = in_a_val ^ in_b_val
            wires[gate.out] = val
        else:
            gates.append(gate)

    z_outs = [w for w in wires.keys() if w.startswith("z")]
    x_ins = [w for w in wires.keys() if w.startswith("x")]
    y_ins = [w for w in wires.keys() if w.startswith("y")]
    print(len(z_outs))
    print(len(x_ins))
    print(len(y_ins))
    z_outs.sort(reverse=True)
    str_out = "".join([str(wires[v]) for v in z_outs])
    print(int(str_out, base=2))

if __name__ == "__main__":
    main(sys.argv[1])
