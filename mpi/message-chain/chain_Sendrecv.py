from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
ntasks = comm.Get_size()
myid = comm.Get_rank()
trgt = (myid + 1) % ntasks
src = (myid - 1) % ntasks

n = 100000
if not myid:
    send_arr = np.full(n, myid, dtype=np.int32)
    comm.Send([send_arr, n, MPI.INT], dest=trgt)
elif not trgt:
    recv_arr = np.empty(n, dtype=np.int32)
    comm.Recv([recv_arr, n, MPI.INT], source=src)
else:
    send_arr = np.full(n, myid, dtype=np.int32)
    recv_arr = np.empty(n, dtype=np.int32)
    comm.Sendrecv(sendbuf=send_arr, dest=trgt, recvbuf=recv_arr, source=src)

send_msg = ''
recv_msg = ''

if myid:
    recv_msg = f'process {myid} received array with first element = {recv_arr[0]}\n'
if trgt:
    send_msg = f'process {myid} sent array of size {send_arr.size}' \
               f' with first element = {send_arr[0]}'
print(recv_msg + send_msg)

