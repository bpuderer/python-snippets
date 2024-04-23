import time
from functools import lru_cache


# Memoization - https://en.wikipedia.org/wiki/Memoization
# avoid duplicate work

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def cache_fib(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    result = cache_fib(n - 1, cache) + cache_fib(n - 2, cache)
    cache[n] = result
    return result


@lru_cache
def lru_fib(n):
    if n < 2:
        return n
    return lru_fib(n - 1) + lru_fib(n - 2)


start = time.perf_counter()
fib(35)
end = time.perf_counter()
print(f'Regular recursive version: {end - start:.7f}s elapsed')

start = time.perf_counter()
lru_fib(35)
end = time.perf_counter()
print(f'With lru_cache: {end - start:.7f}s elapsed')

start = time.perf_counter()
cache_fib(35)
end = time.perf_counter()
print(f'With cache: {end - start:.7f}s elapsed')
