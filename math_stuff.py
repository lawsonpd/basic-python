# Working with math in Python and the `math` built-in library.

def factorial(n:int) -> int:
    '''
        Returns product n * (n-1) * ... * 1
    '''
    if n == 1:
       return 1
    else:
       return n * factorial(n-1)


def fib(n:int, cache:dict={}):
    '''
        Return nth Fibonacci number.
    '''
    print(f'Current fib: {n}')
    if n == 1 or n == 2:
        return 1
    elif n in cache:
        return cache[n]
    else:
        fib_n = fib(n-1) + fib(n-2)
        cache[n] = fib_n
        return fib_n

