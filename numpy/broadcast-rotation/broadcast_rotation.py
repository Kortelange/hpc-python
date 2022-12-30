import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('points_circle.dat')

theta = np.pi/2

# We flip the matrix and do the transposed multiplication
M = np.array([[np.cos(theta), np.sin(theta)],
              [-np.sin(theta), np.cos(theta)]])

plt.plot(points[:, 0], points[:, 1],  'o')
rotated_points = points.dot(M)
plt.plot(rotated_points[:, 0], rotated_points[:, 1], 'o')
plt.show()
