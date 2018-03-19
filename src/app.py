from math import *

from M_gen import M_gen
from solve_brut_force import solve_brut_force
import matplotlib.pyplot as plt

k_values = [0.2, 0.5, 0.8]
n_values = range(2, 21)
measures = 20

data = []
for n in n_values:
    data.append([])
    for d in k_values:
        C = 0
        for _ in range(measures):
            m = M_gen(n, d)
            _, c = solve_brut_force(m)
            C += c
        data[-1].append(C / measures)

plt.title("Compléxité en fonction de n,k")
plt.semilogy(n_values, data)
plt.legend([f'$n^k, d={k}$' for k in k_values])
plt.grid(True)
plt.xlabel("n")
plt.ylabel("Complexité")
plt.show()
