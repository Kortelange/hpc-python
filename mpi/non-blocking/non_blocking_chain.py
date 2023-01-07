from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
myid = comm.Get_rank()
ntasks = comm.Get_size()

trgt = (myid + 1) % ntasks
src = (myid - 1) % ntasks

n = 100000

send_msg = ''
recv_msg = ''
if trgt:
    send_arr = np.full(n, myid, dtype=np.int32)
    send_req = comm.Isend(send_arr, dest=trgt)
if myid:
    recv_arr = np.empty(n, np.int32)
    rec_req = comm.Irecv(recv_arr, source=src)

if trgt:
    # send_req.wait()
    send_msg = f"process {myid} sent array of size {send_arr.size} containing all {send_arr[0]}'s"
if myid:
    rec_req.wait()
    recv_msg = f"process {myid} received an array of {recv_arr[0]}'s\n"

print(recv_msg + send_msg)

