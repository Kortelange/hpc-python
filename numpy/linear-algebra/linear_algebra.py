import numpy as np

# construct 2 2x2 symmetric matrices A and B
A = np.random.random((2,2))
A += A.T
B = np.random.random((2,2))
B += B.T

print(f'A = {A}\nB = {B}')

# compute C = AB
C = A.dot(B)
print(f'AB = {C}')

print(f'Eigenvalues of AB = {np.linalg.eigvals(C)}')