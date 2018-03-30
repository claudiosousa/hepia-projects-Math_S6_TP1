from itertools import combinations

def solve_brut_force(m):
    n = len(m)
    tests = 0
    clique_found = None
    for k in range(2, n+1):
        clique_found = False
        for v_set in combinations(range(n), k):
            for v1, v2 in combinations(v_set, 2):
                tests += 1
                if not m[v1][v2]:
                    break
            else:
                clique_found = True
        if not clique_found:
            return k - 1, tests
    return n, tests
