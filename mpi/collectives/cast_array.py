from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
ntasks = comm.Get_size()

# communicate array to all threads
if rank == 0:
    a = np.arange(8, dtype='i')
else:
    a = np.empty(8, dtype='i')

comm.Bcast(a, root=0)
for i in range(8):
    assert i == a[i], f'{a[i]} != {i} in process {rank}'

print('Arrays were cast succesfully')

