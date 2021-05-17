
import helstrom
import numpy as np
import sys

if __name__ == "__main__":
    '''
    Change rho_0 and rho_1 here
    '''

    rho0 = np.array([[1, 0], [0, 0]])
    rho1 = np.array([[0.5, 0], [0, 0.5]])
    if len(sys.argv) == 3:
        rho0 = np.matrix(sys.argv[1])
        rho1 = np.matrix(sys.argv[2])
        rho0 = np.asarray(rho0)
        rho1 = np.asarray(rho1)
    helstrom.sdp(rho0, rho1)
