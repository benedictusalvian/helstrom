import cvxpy as cp
import numpy as np


def sdp(rho0, rho1):
    n = len(rho0)
    t = 0.5  # Since t is arbitrary, change to whatever you like.
    C = np.zeros((2 * n, 2 * n))
    try:
        C[0:n, 0:n] = (1 - t) * rho1.T
        C[n:2 * n, n:2 * n] = t * rho0.T
    except TypeError:
        print("TypeError: can't multiply sequence by non-int of type 'float'.\nTry checking input states. Input states must be square matrices!")
        return False
    A = []
    b = []

    A0 = np.zeros((2 * n, 2 * n))
    A0[0:n, 0:n] = rho1.T
    A0[n:2 * n, n:2 * n] = -1 * (rho0.T)
    A.append(A0)
    b.append(0)
    for i in range(n):
        for j in range(n):
            E = np.zeros((2 * n, 2 * n))
            E[i][j] = 1
            E[n + i][n + j] = 1
            A.append(E.T)
            b.append(1 if i == j else 0)

    # Define and solve the CVXPY problem.
    # Create a symmetric matrix variable.
    X = cp.Variable((2 * n, 2 * n), symmetric=True)
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
    '''
    Change desired decimal places for solution here
    '''
    value = round(prob.value, ndigits=5)
    solution = np.around(X.value, decimals=3)
    print("The optimal value (min_pwc) is", value)
    print("A solution X (composed of P0 and P1) is")
    print(solution)
    print("P0 is:")
    print(solution[0:n, 0:n])
    print("P1 is:")
    print(solution[n:2 * n, n:2 * n])


if __name__ == "__main__":
    '''
    Change rho_0 and rho_1 here
    '''
    rho0 = np.array([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    rho1 = np.array([[0.25, 0, 0, 0], [0, 0.25, 0, 0],
                     [0, 0, 0.25, 0], [0, 0, 0, 0.25]])
    sdp(rho0, rho1)
