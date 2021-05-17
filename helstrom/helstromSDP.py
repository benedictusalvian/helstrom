import cvxpy as cp
import numpy as np


def sdp(rho0, rho1):
    n = 2
    t = 0.5  # Since t is arbitrary, change to whatever you like.
    C = np.zeros((4, 4))
    C[0:2, 0:2] = (1 - t) * rho1.T
    C[2:4, 2:4] = t * rho0.T
    A = []
    b = []

    A0 = np.zeros((4, 4))
    A0[0:2, 0:2] = rho1.T
    A0[2:4, 2:4] = -1 * (rho0.T)
    A.append(A0)
    b.append(0)
    for i in range(n):
        for j in range(n):
            E = np.zeros((4, 4))
            E[i][j] = 1
            E[n + i][n + j] = 1
            A.append(E.T)
            b.append(1 if i == j else 0)

    # Define and solve the CVXPY problem.
    # Create a symmetric matrix variable.
    X = cp.Variable((4, 4), symmetric=True)
    # The operator >> denotes matrix inequality.
    constraints = [X >> 0]
    constraints += [
        cp.trace(A[i] @ X) == b[i] for i in range(n**2 + 1)
    ]
    prob = cp.Problem(cp.Minimize(cp.trace(C @ X)),
                      constraints)
    prob.solve()

    # DEBUGGING.
    # print(A)
    # print(b)

    # Print result.
    print("Input rho_0 is:")
    print(rho0)
    print("Input rho_1 is:")
    print(rho1)
    print("The optimal value (min_pwc) is", prob.value)
    print("A solution X (composed of P0 and P1) is")
    '''
    Change desired decimal places for solution here
    '''
    solution = np.around(X.value, decimals=3)
    print(solution)
    print("P0 is:")
    print(solution[0:2, 0:2])
    print("P1 is:")
    print(solution[2:4, 2:4])


if __name__ == "__main__":
    '''
    Change rho_0 and rho_1 here
    '''
    rho0 = np.array([[1, 0], [0, 0]])
    rho1 = np.array([[0.5, 0], [0, 0.5]])
    sdp(rho0, rho1)
