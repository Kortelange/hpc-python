from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
ntasks = comm.Get_size()
myid = comm.Get_rank()
trgt = (myid + 1) % ntasks
src = (myid - 1) % ntasks

n = 1000


if myid == 0:
    send_arr = np.full(n, myid, dtype=np.int32)
    comm.Send([send_arr, n, MPI.INT], dest=trgt)
elif myid < ntasks - 1:
    send_arr = np.full(n, myid, dtype=np.int32)
    recv_arr = np.empty_like(send_arr, dtype=np.int32)
    comm.Recv([recv_arr, n, MPI.INT], source=src)
    comm.Send([send_arr, n, MPI.INT], dest=trgt)
else:
    recv_arr = np.empty(n, dtype=np.int32)
    comm.Recv([recv_arr, n, MPI.INT], source=src)

send_msg = ''
recv_msg = ''

if myid:
    recv_msg = f'process {myid} received array with first element = {recv_arr[0]}\n'
if trgt:
    send_msg = f'process {myid} sent array of size {send_arr.size} with ' \
               f'first element = {send_arr[0]}'

print(recv_msg + send_msg)
