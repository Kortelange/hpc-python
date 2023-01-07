from init_data import *

comm.Gather(data[:2], recv_buf, root=1)

print(f'process {rank} received {recv_buf}')