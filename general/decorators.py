# https://www.python.org/dev/peps/pep-0318/
# https://github.com/GrahamDumpleton/wrapt
# Colton Myers PyCon 2014: https://www.youtube.com/watch?v=9oyr0mocZTg

# decorators are a callable object which takes in a callable object and returns a callable object
# replace, enhance, or modify existing functions

import time
import operator
import functools


def log_args(f):
    @functools.wraps(f)  # needed to keep decorated object's __doc__ and __name__ intact
    def wrapper(*args, **kwargs):  # acts as proxy for original function - CM
        print(f'arguments: {args} {kwargs}')
        return f(*args, **kwargs)
    return wrapper


def timer(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = f(*args, **kwargs)
        total_time = int((time.time() - start_time) * 1000)
        print(f'execution time: {total_time} ms')
        return ret
    return wrapper


def count(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.counter += 1
        return f(*args, **kwargs)
    wrapper.counter = 0
    return wrapper


def fancy_print(txt='*', n=3):
    def dec(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f'{args} {kwargs}')
            return f'{txt*n} {f(*args, **kwargs)} {txt*n}'
        return wrapper
    return dec


@count
@timer
@log_args
def snooze(num_sec=1):
    """snooze demo function"""
    time.sleep(num_sec)

snooze(0.3)
snooze()
print(f'snooze called {snooze.counter} times')



@fancy_print('-**-', 2)
def multiply_these(*args):
    return functools.reduce(operator.mul, args)

print(multiply_these(3, 6, 10))
