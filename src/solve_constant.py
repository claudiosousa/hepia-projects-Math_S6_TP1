from math import *

def solve_constant(m):
    n = len(m)
    E = sum(sum(l) for l in m)-n
    return ceil(sqrt(E)), n**2
