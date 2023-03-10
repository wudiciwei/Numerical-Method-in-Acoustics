import func_calc_dfdx as fc
import numpy as np

solver_term_order = 1
stencil = [-5/2,-3/2,-1/2,1/2,3/2,5/2]
N = len(stencil)

A = np.eye(6)
for row in range(N):
    dx = stencil[row]
    for col in range(N):
        A[col,row] = dx**(col)/np.math.factorial(col)

B = np.zeros([N,1])
B[solver_term_order][0] = 1

C = np.dot(np.linalg.inv(A),B)
order = len(B) - 1