from math import *

from M_gen import M_gen
from solve_brut_force import solve_brut_force
from solve_constant import solve_constant
import matplotlib.pyplot as plt

k_values = [0.2, 0.5, 0.8]
n_values = range(2, 23)
measures = 10

solvers = [solve_brut_force, solve_constant]

complexity_p = []
error_p = []
for n in n_values:
    complexity_p.append([])
    error_p.append([])
    for d in k_values:
        C = [0] * len(solvers)
        err = [0] * (len(solvers) - 1)
        for _ in range(measures):
            k_min = None
            m = M_gen(n, d)
            for isolver, solver in enumerate(solvers):
                k, c = solver(m)
                if not k_min:
                    k_min = k
                else:
                    err[isolver - 1] += abs(k - k_min) / k_min / measures
                C[isolver] += c / measures

        error_p[-1] += err
        complexity_p[-1] += C


plt.subplot(211)
plt.title("Compléxité en fonction de n,k")
plt.semilogy(n_values, complexity_p)
plt.legend([f'$n^k, d={k}$' for k in k_values])
plt.grid(True)
plt.xlabel("n")
plt.ylabel("Complexité")

plt.subplot(212)
plt.title("Erreur en fonction de n,k")
plt.plot(n_values, error_p)
plt.legend([f'$n^k, d={k}$' for k in k_values])
plt.grid(True)
plt.xlabel("n")
plt.ylabel("Error %")

plt.show()
