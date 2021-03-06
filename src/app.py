from math import *

from M_gen import M_gen
from solve_brut_force import solve_brut_force
from solve_constant import solve_constant
from solve_heuristique import solve_heuristique
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

k_values = [0, 0.5, 1]
n_values = range(2, 7)
measures = 10

solvers = [solve_brut_force, solve_constant, solve_heuristique]

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
                    err[isolver - 1] += abs(k) / k_min / measures
                C[isolver] += c / measures

        error_p[-1] += err
        complexity_p[-1] += C


mpl.rcParams['axes.prop_cycle'] = cycler(color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
plt.subplot(211)
plt.title("Compléxité en fonction de n,k")
plt.semilogy(n_values, complexity_p)
plt.legend(sum([(f'$n^k, d={k}$', f'$sqrt(|E|), d={k}$', f'$n^2, d={k}$') for k in k_values],()), loc='upper left', ncol=3)
plt.grid(True)
plt.xlabel("n")
plt.ylabel("Complexité")

mpl.rcParams['axes.prop_cycle'] = cycler(color=['#ff7f0e', '#2ca02c', '#9467bd', '#8c564b', '#7f7f7f', '#bcbd22', '#17becf'])
plt.subplot(212)
plt.title("Erreur en fonction de n,k")
plt.plot(n_values, error_p)
plt.legend(sum([(f'$sqrt(|E|), d={k}$', f'$n^2, d={k}$') for k in k_values],()), loc='upper left', ncol=3)
plt.grid(True)
plt.xlabel("n")
plt.ylabel("Error ratio")

plt.show()
