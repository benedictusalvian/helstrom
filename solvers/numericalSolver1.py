import cvxpy as cp
import numpy as np
from math import sqrt


def sdp(rho0, rho1):
    n = len(rho0)

    # A and B are positive semidefinite matrices. B is an invertible matrix.
    A = rho0
    B = rho0 + rho1
    # Define and solve the CVXPY problem.
    # Create a symmetric matrix variable.
    P = cp.Variable((n, n), symmetric=True)
    # The operator << denotes matrix inequality.
    constraints = [cp.trace(B @ P) <= 1]
    constraints += [P >> 0]
    constraints += [P << np.eye(2)]
    prob = cp.Problem(cp.Maximize(cp.trace(A @ P)),
                      constraints)
    prob.solve()

    # Print result.
    print("Input rho_0 is:")
    print(rho0)
    print("Input rho_1 is:")
    print(rho1)
    '''
    Change desired decimal places for solution here
    '''
    value = round(prob.value, ndigits=5)
    solution = np.around(P.value, decimals=3)
    print("The optimal value is", value)
    print("A solution P is")
    print(solution)


if __name__ == "__main__":
    '''
    Change rho_0 and rho_1 here
    '''
    # rho0 = np.array([[0.25, sqrt(3)/8], [sqrt(3)/8, 3/16]])
    rho0 = np.array([[0.5625, 3 * sqrt(7)/16], [3 * sqrt(7)/16, 7/16]])
    rho1 = np.array([[0.5, 0.5], [0.5, 0.5]])
    sdp(rho0, rho1)
