from math import *

def solve_constant(m):
    E = sum(sum(l) for l in m) / 2
    n = len(m)
    return 1 + ceil(sqrt(E)), n**2
