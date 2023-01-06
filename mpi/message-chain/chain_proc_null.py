import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
ntasks = comm.Get_size()
myid = comm.Get_rank()
trgt = (myid + 1) % ntasks
src = (myid - 1) % ntasks

n = 100000
if trgt:
    send_arr = np.full(n, myid, dtype=np.int32)
    send_msg = f'process {myid} sent array of size {send_arr.size} ' \
               f'with first element = {send_arr[0]}'
else:
    send_arr = np.empty(1)
    send_msg = ''
    trgt = MPI.PROC_NULL

if myid:
    recv_arr = np.empty(n, dtype=np.int32)
else:
    recv_msg = ''
    src = MPI.PROC_NULL
    recv_arr = np.empty(1)

comm.Sendrecv(sendbuf=send_arr, dest=trgt, recvbuf=recv_arr, source=src)
if recv_arr.size > 1:
    recv_msg = f'process {myid} received array with first value = {recv_arr[0]}\n'

print(recv_msg + send_msg)

