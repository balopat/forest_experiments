import pyquil.quil as pq
import pyquil.forest as forest
from pyquil.gates import *

## Bernstein Vazirani

qvm = forest.Connection()

p = pq.Program(CNOT(0,1), CNOT())

print p

print qvm.wavefunction(p)
