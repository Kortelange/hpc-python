from init_data import *

color = int(rank > 1)
local_comm = comm.Split(color)
local_rank = local_comm.Get_rank()

local_comm.Reduce(data, recv_buf, op=MPI.SUM, root=0)

comm.barrier()
print(f'process {rank} received {recv_buf}')