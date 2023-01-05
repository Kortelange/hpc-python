#BASH

if [[ $1 ]];
  then
    processes=$1
  else
    processes=1
fi

mpirun -np "$processes" python hello_world.py