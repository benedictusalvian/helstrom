from numpy import apply_along_axis, linalg as LA
import numpy as np
from math import sqrt
from collections import OrderedDict
from numpy.lib.function_base import _append_dispatcher
from scipy.linalg import fractional_matrix_power

'''
    -define B_1 :  =  B  and  compute p_1 : =  maximum { p  |    p  | 1 ><  1  |  ≤  B_1 }
    Explicitly,  p_1  :  =  <1|  B_1  |1>

    -define B_2 :  = B_1 - p_1  |1><1|    and  compute p_2 : =  maximum { p  |    p  | 2 ><  2  |  ≤  B_2 }
    Explicitly,  p_2  :  =  <2|  B_2  |2>

    -iterate B_{k+1}  =  B_k  -  p_k |k><k|

    Finally, the probability of success is    sum_i  p_i  a_i

    Finally, you can compare the two solution.

    The above algorithm provides a lower bound to the optimal solution. It would be very cool if, actually, the lower bound were the exact solution.

'''


def heuristic(rho0, rho1):
    n = len(rho0)

    # A and B are positive semidefinite matrices. B is an invertible matrix.
    A = rho0
    B = rho0 + rho1
    x = fractional_matrix_power(B, -0.5)
    E = x @ A @ x

    w, v = LA.eig(E)

    d = {}
    for (index, eigenvalue) in enumerate(w):
        d[eigenvalue] = np.array(v[:, index]).reshape(n, 1)  # Column vectors.

    # Order eigenvalues descendingly.
    d_descending = OrderedDict(sorted(d.items(), reverse=True))

    # DEBUGGING.
    # print("Input rho_0 is:")
    # print(rho0)
    # print("Input rho_1 is:")
    # print(rho1)

    # print("E := B^-1/2 @ A @ B^-1/2 is:")
    # print(E)

    # print("Eigenvalues of E are:")
    # print(w)
    # print("Eigenvectors of E are:")
    # print(v)

    # print("d_descending is:")
    # print(d_descending)

    prevDensityMatrix, prevP, prevB = np.zeros((n, n)), 0, B
    p_i, ans = [], 0

    for index, (key, value) in enumerate(d_descending.items(), start=1):
        # Calculate B_{k+1} = B_k - p_k |k><k|
        newB = prevB - prevP * prevDensityMatrix
        newP = (value.T @ newB @ value).item()
        newP = min(newP, 1 - sum(p_i))  # Constraints to p.
        ans += newP * key
        p_i.append(newP)
        prevDensityMatrix = value @ value.T  # Calculate |k><k|.
        prevP, prevB = newP, newB

        # DEBUGGING.
        # print(f'B{index} is:')
        # print(newB)
        # print(f"p{index} is {newP}.")
        # print(f"|{index}><{index}| is:")
        # print(prevDensityMatrix)

    # print("p_i:", p_i)
    # print("The optimal value is", ans)

    return ans


if __name__ == "__main__":
    '''
    Change rho_0 and rho_1 here
    '''
    rho0 = np.array([[0.25, sqrt(3)/4], [sqrt(3)/4, 0.75]])
    # rho0 = np.array([[0.5625, 3 * sqrt(7)/16], [3 * sqrt(7)/16, 7/16]])    rho1 = np.array([[0.5, 0], [0, 0.5]])
    # rho0 = np.array([[1, 0], [0, 0]])
    rho1 = np.array([[0.5, 0], [0, 0.5]])
    # rho0 = np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    # rho1 = np.array([[0.25, 0, 0, 0], [0, 0.25, 0, 0],
    #                  [0, 0, 0.25, 0], [0, 0, 0, 0.25]])
    # rho0 = np.array([[1/9, 1/9, sqrt(7)/9], [1/9, 1/9, sqrt(7)/9],
    #                  [sqrt(7)/9, sqrt(7)/9, 7/9]])
    # rho1 = np.array([[1/4, 1/4, 1/(2 * sqrt(2))], [1/4, 1/4, 1/(2 * sqrt(2))],
    #                  [1/(2 * sqrt(2)), 1/(2 * sqrt(2)), 1/2]])
    heuristic(rho0, rho1)
