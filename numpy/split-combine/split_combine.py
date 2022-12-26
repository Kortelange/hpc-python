import numpy as np

# create 8x8 array
a = np.arange(8*8).reshape(8,8)
print(f'8x8 array:\n{a}\n')

# split into 2 4x8 arrays
a = np.split(a, 2)
print(f'array split into 2 4x8 arrays\n{a}\n')

# combine arrays
a = np.concatenate((a))
print(f'arrays combined again\n{a}\n')

# split into 2 8x4 arrays
a = np.split(a, 2, axis=1)
print(f'array split into 8x4 arrays\n{a}\n')

# combine again
a = np.concatenate((a), axis=1)
print(f'arrays combined again\n{a}')


