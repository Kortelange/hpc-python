import numpy as np
cimport numpy as cnp
import cython


@cython.boundscheck(False)
@cython.boundscheck(False)
@cython.cdivision(True)
cpdef evolve(
	cnp.ndarray[cnp.double_t, ndim=2] u,
	cnp.ndarray[cnp.double_t, ndim=2] u_previous,
	double a,
	double dt,
	double dx2,
	double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step
       dx2:          grid spacing squared, i.e. dx^2
       dy2:            -- "" --          , i.e. dy^2"""

    cdef int n = u.shape[0]
    cdef int m = u.shape[1]

    cdef double mdx2 = 1 / dx2
    cdef double mdy2 = 1 / dy2

    cdef int i,j

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
    		(u_previous[i + 1, j] + u_previous[i - 1, j] \
    		- 2 * u_previous[i, j]) * mdx2 + \
    		(u_previous[i, j + 1] + u_previous[i, j - 1] \
    		- 2 * u_previous[i, j] * mdy2))
    u_previous[:] = u[:]
