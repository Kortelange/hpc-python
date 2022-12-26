import numpy as np
import matplotlib.pyplot as plt
from collections.abc import Callable


def integral(f: Callable, start: float, stop: float, dx: float) -> float:
    x = np.arange(start, stop + dx, dx)
    return dx * np.sum(f((x[1:] + x[:-1]) / 2))


start = 0.0
stop = np.pi / 2

print('expected integral = 1')
for dx in (0.001, 0.01, 0.1, 0.5):
    print(f'dx = {dx}, numerical integral = '
          f'{integral(np.sin, start, stop, dx)}')