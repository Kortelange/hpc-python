from mpi4py import MPI

comm = MPI.COMM_WORLD

print(f'I am rank {comm.rank} in a group of {comm.size} processes')