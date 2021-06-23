from math import sqrt
from numericalSolver1 import sdp
from numericalSolver2 import heuristic
import random
import numpy as np


def makeMatrix():
    alpha = random.uniform(0, 1)
    beta = sqrt(1 - alpha**2)
    vector = np.array([[alpha], [beta]])
    return alpha, beta, vector @ vector.T


for i in range(10):
    alpha0, beta0, rho0 = makeMatrix()
    alpha1, beta1, rho1 = makeMatrix()
    sdpResult = sdp(rho0, rho1)
    heuristicResult = heuristic(rho0, rho1)
    print(
        f'Vector rho0 is: {str([alpha0, beta0]):<43}, rho1 is {str([alpha1, beta1]):<43}, sdp result: {sdpResult}, heuristic result: {heuristicResult}')
