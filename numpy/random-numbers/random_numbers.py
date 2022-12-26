import numpy as np
import matplotlib.pyplot as plt

uniform_array = np.random.random(1000)

print(f'mean of uniform array = {uniform_array.mean()}\n'
      f'std of uniform array = {uniform_array.std()}')

normal_array = np.random.normal(size=1000)
print(f'mean of normal dist = {normal_array.mean()}\n'
      f'std of normal dist = {normal_array.std()}')
