import numpy as np
cimport numpy as cnp
import cython


@cython.boundscheck(False)
cpdef cyt_sum(cnp.ndarray[cnp.double_t, ndim=1] array):
	cdef int i
	cdef int m = array.size
	cdef double s = 0
	for i in range(m):
		s += array[i]
	return s
