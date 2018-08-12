# https://www.python.org/dev/peps/pep-0318/
# https://github.com/GrahamDumpleton/wrapt
# Colton Myers PyCon 2014: https://www.youtube.com/watch?v=9oyr0mocZTg

import time
import operator
from functools import reduce


def log_args(wrapped):
    def inner(*args, **kwargs):  # acts as proxy for original function - CM
        print(f'arguments: {args} {kwargs}')
        return wrapped(*args, **kwargs)
    return inner


def timer(wrapped):
    def inner(*args, **kwargs):
        start_time = time.time()
        ret = wrapped(*args, **kwargs)
        total_time = int((time.time() - start_time) * 1000)
        print(f'total time executing {wrapped.__name__} (ms): {total_time}')
        return ret
    return inner


def count(wrapped):
    def inner(*args, **kwargs):
        inner.counter += 1
        return wrapped(*args, **kwargs)
    inner.counter = 0
    return inner


def fancy_print(txt='*', n=3):
    def dec(wrapped):
        def inner(*args, **kwargs):
            return f'{txt*n} {wrapped(*args, **kwargs)} {txt*n}'
        return inner
    return dec


@count
@timer
@log_args
def snooze(num_sec=1):
    time.sleep(num_sec)

snooze(2)
snooze()
print(f'snooze called {snooze.counter} times')



@fancy_print('-*-', 2)
def multiply_these(*args):
    return reduce(operator.mul, args)

print(multiply_these(3, 6, 10))
