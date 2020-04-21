from functools import partial


def some_func(a, b=28, **kwargs):
    print(f'a: {a}    b: {b}    kwargs: {kwargs}')
    return


wrapper = partial(some_func, default_kwarg=9)

wrapper(44)
wrapper(44, 45)
