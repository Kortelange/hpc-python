import numpy as np

def derivative(f_x, dx):
    df = np.empty_like(f_x)
    df[1:-1] = (f_x[2:] - f_x[:-2]) / (2 * dx)
    df[0] = (f_x[1] - f_x[0]) / dx
    df[-1] = (f_x[-1] - f_x[-2]) / dx
    return df

x = np.arange(0, np.pi / 2 + 0.1, 0.1)

print('Diff between numerical and cos(x)')
print(derivative(np.sin(x), 0.1) - np.cos(x))
