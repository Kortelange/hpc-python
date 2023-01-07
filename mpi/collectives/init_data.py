from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ntasks = comm.Get_size()

n = ntasks * 2

# initialise data
data = np.arange(rank * n, n * (rank + 1), dtype='i')
recv_buf = np.full(n, -1, dtype='i')


comm.barrier()