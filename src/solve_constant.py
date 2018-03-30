from math import *

def solve_constant(m):
    n = len(m)
    E = max(1, sum(sum(l) for l in m)-n)
    return ceil(sqrt(E)), n**2
