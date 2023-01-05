from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
other_rank = (rank + 1) % 2

# have 2 processes communicate a dictionary with their ranks
msg = {'rank': rank}

comm.send(msg, dest=other_rank)
received_msg = comm.recv(source=other_rank)

print(f'process with rank {rank} received message {received_msg}')

# send numpy arrays we switch orders to avoid deadlock
send_arr = np.full(100000, rank, np.int32)
recv_arr = np.empty_like(send_arr, np.int32)
if rank == 0:
    comm.Send([send_arr, 100000, MPI.INT], dest=other_rank)
    comm.Recv([recv_arr, 100000, MPI.INT], source=other_rank)
else:
    comm.Recv([recv_arr, 100000, MPI.INT], source=other_rank)
    comm.Send([send_arr, 100000, MPI.INT], dest=other_rank)


# send_arr = rank * np.ones(100000, dtype=np.int32)
# recv_arr = np.empty(100000, dtype=np.int32)
# comm.Sendrecv(send_arr, dest=other_rank, recvbuf=recv_arr, source=other_rank)
#
print(f'process with rank {rank} received array of size {recv_arr.shape} with first value {recv_arr[0]}')
