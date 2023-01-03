def fibonacci(int n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def cyfib(int n) -> int:
    if n < 2:
        return n
    return cyfib_int(n)

cdef int cyfib_int(int n):
    if n < 2:
        return n
    return cyfib_int(n - 1) + cyfib_int(n - 2)

