"""
Simulate logic gates

Given a list of wires named like x01, y01, z02 or abc
and a XOR, OR and AND gates, determine the output
(wires starting with z) based on the input wires

These should be arranged in a dag, and I think
we can just simulate this.

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
    z_outs.sort(reverse=True)
    str_out = "".join([str(wires[v]) for v in z_outs])
    print(int(str_out, base=2))

if __name__ == "__main__":
    main(sys.argv[1])
