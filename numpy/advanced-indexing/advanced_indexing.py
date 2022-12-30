import numpy as np

uniform_grid = np.random.random((10,10))
mask = (uniform_grid >= 0.5)

# values >= 0.5
# print(uniform_grid[mask])

# indeices of values greater than 0.5 can be obtained by [:, i]
a = np.vstack(np.nonzero(mask))
print(a)
print(a[:, :5])