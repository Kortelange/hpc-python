import numpy as np

points = np.loadtxt('xy-coordinates.dat')
points[:,1] += 2.5

np.savetxt('new_points.dat', points, fmt='%.5f')