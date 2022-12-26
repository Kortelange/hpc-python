import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('points_circle.dat')

v = np.array([2.1, 1.1])
translated_points = points + v

plt.plot(points[:,0], points[:,1], 'o')
plt.plot(translated_points[:, 0], translated_points[:, 1], 'o')
plt.legend(['original points', 'translated points'])
plt.show()