from math import sqrt
from numericalSolver1 import sdp
from numericalSolver2 import heuristic
import random
import numpy as np


def makeMatrix(step):
    alpha = step
    beta = sqrt(1 - alpha**2)
    vector = np.array([[alpha], [beta]])
    return alpha, beta, vector @ vector.T


step = 0
while (step <= 1):
    alpha0, beta0, rho0 = makeMatrix(step)
    alpha1, beta1, rho1 = makeMatrix(random.uniform(0, 1))
    sdpResult = sdp(rho0, rho1)
    heuristicResult = heuristic(rho0, rho1)
    step += 0.05
    step = round(step, 3)
    print(
        f'Vector rho0 is: {str([alpha0, beta0]):<43}, rho1 is {str([alpha1, beta1]):<43}, sdp result: {sdpResult}, heuristic result: {heuristicResult}')
