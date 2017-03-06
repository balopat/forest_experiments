import pyquil.quil as pq
import pyquil.forest as forest
from pyquil.gates import *

qvm = forest.Connection()
coin_flip = pq.Program().inst(H(0)).measure(0, 0)
num_flips = 2
print coin_flip
print qvm.wavefunction(coin_flip)
print qvm.run(coin_flip, [0], num_flips)