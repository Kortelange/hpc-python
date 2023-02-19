import numpy as np
from timeit import timeit
from cyt_multi import matrix_mult_cyt


def matrix_multiply(m1, m2):
    assert m1.shape[1] == m2.shape[0]
    n, m, l = m1.shape[0], m2.shape[1], m1.shape[1]
    product = np.empty((n, m))
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(l):
                s += m1[i, k] * m2[k, j]
            product[i, j] = s
    return product


runs = 1000


m1 = np.random.random((100, 100))
m2 = np.random.random((100, 10))

print(timeit('matrix_multiply(m1, m2)', globals=globals(), number=runs))
print(timeit('matrix_mult_cyt(m1, m2)', globals=globals(), number=runs))
print(timeit('m1.dot(m2)', globals=globals(), number=runs))
