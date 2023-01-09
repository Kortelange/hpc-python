import numpy as np
from timeit import timeit
# from cyt_sum import cyt_sum
from mpi4py import MPI

comm = MPI.COMM_WORLD
ntasks = comm.Get_size()
rank = comm.Get_rank()


def naive_sum(array):
    s = 0
    for v in array:
        s += v
    return s


def mp_sum(array):
    # Try and distribute data equally
    to_each = array.size // ntasks
    remainder = array.size % ntasks
    print(f'hello from {rank}')
    # if remainder:
    #     if rank == 0:
    #         s = np.zeros(ntasks, dtype='f')
    #         for i in range(1, remainder):
    #             comm.Send(array[i * (to_each + 1): (i + 1) * (to_each + 1)], i)
    #         for i in range(remainder, ntasks):
    #             start = remainder * (to_each + 1)
    #             comm.Send(array[start + (i % remainder) * to_each: start + ((i + 1) % remainder) * to_each], i)
    #         s[0] = array[: to_each + 1].sum()
    #         for i in range(1, ntasks):
    #             s[i] = comm.recv(source=i)
    #         return s.sum()
    #
    #     if (0 < rank) and (rank <= remainder):
    #         recv_buf = np.empty(to_each + 1, dtype='f')
    #         comm.Recv(recv_buf, 0)
    #         comm.send(recv_buf.sum(), 0)
    #     elif rank > remainder:
    #         recv_buf = np.empty(to_each, dtype='f')
    #         comm.Recv(recv_buf, 0)
    #         comm.send(recv_buf.sum(), 0)







a = np.random.random(100000)
runs = 1000

# print(timeit('naive_sum(a)', globals=globals(), number=runs))
# print(timeit('a.sum()', globals=globals(), number=runs))
# print(timeit('cyt_sum(a)', globals=globals(), number=runs))
print(a.sum())
print(mp_sum(a))


