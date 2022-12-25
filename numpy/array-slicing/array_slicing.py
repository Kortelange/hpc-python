import numpy as np

ar = np.random.random((4,4))
print('random 4x4 array')
print(ar)

# extract 2nd row
print('2nd row')
print(ar[1, :])

# extract 3rd column
print('3rd column')
print(ar[:, 2])

# assign .21 to upper left corner
print('assign .21 to upper left')
ar[:2, :2] = np.ones((2,2)) * 0.21
print(ar)

# 8x8 checkerboard
row_1 = np.array([(i+1) % 2 for i in range(8)])
row_2 = (row_1 + 1) % 2
checkerboard = np.array([(row_1, row_2)[i % 2] for i in range(8)])
print(checkerboard)

# alternative
checkerboard = np.zeros((8,8))
checkerboard[::2,::2] = 1
checkerboard[1::2, 1::2] = 1
print(checkerboard)