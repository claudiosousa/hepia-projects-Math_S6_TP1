def solve_heuristique(m):
    n = len(m)
    k = 0
    tests = 0
    line_sum = [sum(l) for l in m]
    tests += n**2
    line_sum_count = dict(zip(line_sum, [0] * len(line_sum)))
    tests += n

    for s in line_sum:
        for c in range(0, s+1):
            if c in line_sum_count:
                line_sum_count[c] += 1
                tests += 1

    for c in line_sum_count.items():
        if (c[1] >= c[0]) and (c[0] > k):
            k = c[0]
            tests += 1

    return k, tests
