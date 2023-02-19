import numpy as np

M = np.zeros((6,6))
M[1:, : -1] += np.eye(5)
M[: -1, 1:] += np.eye(5)
print(M)