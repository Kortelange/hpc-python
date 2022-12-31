import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

points = np.loadtxt('faulty_data.dat')
# after investigating, it looks like point 3 is wrong
valid = np.zeros_like(points)
valid[2, :] = 1
mask = ma.array(points, mask=valid)

masked_poly = ma.polyfit(mask[:, 0], mask[:, 1], 2)
poly = np.polyfit(points[:, 0], points[:, 1], 2)

x = np.linspace(points[0, 0], points[-1, 0])
tempx = np.array([x**2, x, np.ones_like(x)])
y_mask = masked_poly.dot(tempx)
y_nomask = poly.dot(tempx)
plt.plot(x, y_mask, label='mask')
plt.plot(points[:, 0], points[:, 1], 'o', label='points')
plt.plot(x, y_nomask, label='nomask')
plt.legend()
plt.show()