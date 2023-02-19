import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
ntasks = comm.Get_size()
rank = comm.Get_rank()

n = 10000 * 4
to_each = n // ntasks
remainder = n % ntasks

if rank == 0:
    print(remainder, flush=True)
    a = np.random.random(n)
    for i in range(1, ntasks - remainder):
        comm.Send(a[to_each * i: to_each * (i + 1)], i)
    start_val = to_each * (ntasks - remainder)
    for i in range(remainder):
        comm.Send(a[start_val + i * (to_each + 1): start_val + (i + 1) * (to_each + 1)], i + ntasks - remainder)
    s = a[:to_each].sum()
    for i in range(1, ntasks):
        s += comm.recv(source=i)
    print((abs(a.sum() - s) < 10 ** -6))
else:
    if rank < ntasks - remainder:
        recv_buf = np.empty(to_each, dtype=float)
    else:
        recv_buf = np.empty(to_each + 1, dtype=float)
    comm.Recv(recv_buf, 0)
    comm.send(recv_buf.sum(), 0)