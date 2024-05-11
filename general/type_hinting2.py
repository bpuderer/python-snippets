from typing import Any, Callable, Sequence, TypeVar
# Callable and Sequence are deprecated aliases to collections.abc.Callable and collections.abc.Sequence
# https://docs.python.org/3/library/typing.html#deprecated-aliases

def doubler(val: Any) -> Any:
    # every type compatible with Any
    return val * 2

def print_seq(val: Sequence) -> None:
    for i, element in enumerate(val):
        print(f'{i}: {element}')

def run_ftn(ftn: Callable):
    ftn()

# generics.  reusable tpe variables
# https://docs.python.org/3/library/typing.html#typing.TypeVar
K = TypeVar('K')
V = TypeVar('V')

def find_in_dict(d: dict[K, V], val: V) -> bool:
    return val in d.values()


print(doubler(1))
print(doubler('1'))

print_seq((1, 2))
print_seq([1, 2])
# print_seq({'a': 0})  # arg-type error from mypy
# print_seq({1, 2, 3})  # arg-type error from mypy

run_ftn(lambda: print('hey'))

my_dict1 = {'a': 0, 'b': 1}
my_dict2 = {0: 'a', 1: 'b'}
print(find_in_dict(my_dict1, 1))
# print(find_in_dict(my_dict1, '1')) # misc error from mypy. cannot infer type argument 2
print(find_in_dict(my_dict2, 'z'))
