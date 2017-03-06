import pyquil.forest as forest
import pyquil.quil as pq
from pyquil.gates import *
from math import *

qvm = forest.Connection()


def throw_polyhedral_die(num_sides):
    reject = True
    roll = -1
    num_qbits = int(ceil(log(num_sides, 2)))
    while reject:
        p = pq.Program()
        for i in range(num_qbits):
            p.inst(H(i))
        for i in range(num_qbits):
            p.inst(MEASURE(i, i))
        reg = range(num_qbits)
        roll = int(''.join(str(x) for x in qvm.run(p, reg)[0]), 2) + 1
        reject = roll > num_sides
    return roll


for i in range(1, 10):
    print "DICE:", throw_polyhedral_die(11)
