import pyquil.quil as pq
import pyquil.forest as forest
from pyquil.gates import *
qvm = forest.Connection()
p = pq.Program(H(0), CNOT(0,1))
print p

print qvm.wavefunction(p)[0]
