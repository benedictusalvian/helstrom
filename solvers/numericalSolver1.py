import cvxpy as cp
from cvxpy.expressions.cvxtypes import power
import numpy as np
from math import sqrt
import numpy as np
from scipy.linalg import fractional_matrix_power


def sdp(rho0, rho1):
    n = len(rho0)

    # A and B are positive semidefinite matrices. B is an invertible matrix.
    A = rho0
    B = rho0 + rho1
    # Define and solve the CVXPY problem.
    # Create a symmetric matrix variable.
    P = cp.Variable((n, n), symmetric=True)
    x = fractional_matrix_power(B, -0.5)
    y = fractional_matrix_power(B, 0.5)
    gamma = y @ P @ y
    # The operator << denotes matrix inequality.
    # constraints = [cp.trace(B @ P) <= 1]
    # constraints += [P >> 0]
    # constraints += [P << np.eye(2)]
    constraints = [gamma << B]
    constraints += [P >> 0]
    constraints += [cp.trace(gamma) <= 1]
    prob = cp.Problem(cp.Maximize(cp.trace(x @ A @ x @ gamma)),
                      constraints)
    prob.solve()

    # Print result.
    # print("Input rho_0 is:")
    # print(rho0)
    # print("Input rho_1 is:")
    # print(rho1)
    '''
    Change desired decimal places for solution here
    '''
    value = round(prob.value, ndigits=5)
    # solution = np.around(P.value, decimals=3)
    # gammaResult = np.around(y @ P.value @ y, decimals=3)
    # print("The optimal value is", value)
    # print("A solution P is")
    # print(solution)
    # print("Gamma result is")
    # print(gammaResult)

    return value


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
    sdp(rho0, rho1)
