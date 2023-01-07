from init_data import *

comm.Scatter(data, recv_buf[:2], root=0)
print(f'process {rank} received {recv_buf}')
