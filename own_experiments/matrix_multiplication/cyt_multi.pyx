import numpy as np
cimport numpy as np
import cython


@cython.boundscheck(False)
cpdef matrix_mult_cyt(np.ndarray[np.double_t, ndim=2] m1, np.ndarray[np.double_t, ndim=2] m2):
	assert m1.shape[1] == m2.shape[0]
	cdef int n, m, i, j
	n = m1.shape[0]
	m = m2.shape[1]

	cdef np.ndarray product = np.zeros([n, m], dtype=np.float64)

	for i in range(n):
		for j in range(m):
			product[i, j] = (m1[i, :] * m2[:, j]).sum()
	return product
