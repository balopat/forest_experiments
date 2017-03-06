import pyquil.forest as forest
import pyquil.quil as pq
from pyquil.gates import *

# return the result of throwing an 8 sided die, an int between 1 and 8, by running a quantum program
qvm = forest.Connection()
p = pq.Program(H(0), H(1), H(2), MEASURE(0, 0), MEASURE(1, 1), MEASURE(2, 2))
print p
print qvm.wavefunction(p)
res = [0, 1, 2]
print int(''.join(str(x) for x in qvm.run(p, res)[0]), 2)
