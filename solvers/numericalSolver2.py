from numpy import linalg as LA
import numpy as np

w, v = LA.eig(np.array([[1, -1], [2, 4]]))
print(w)
print(v)
