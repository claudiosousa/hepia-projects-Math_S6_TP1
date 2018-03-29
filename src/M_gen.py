from random import random

def M_gen(n, density):
    m = [[0] * n for _ in range(n)]
    left_todo = n * (n - 1) / 2
    e_left = left_todo * density
    for i in range(n):
        m[i][i] = 1
        for j in range(i + 1, n):
            e = random() < e_left / left_todo
            if e:
                e_left -= 1
                m[i][j] = m[j][i] = int(e)
            left_todo -= 1
    return m