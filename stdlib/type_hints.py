from typing import List, Dict, Tuple, Iterable, Optional, Union
from datetime import date

# https://www.youtube.com/watch?v=2wDvzy6Hgxg&t=31m37s
# PEP-484 https://www.python.org/dev/peps/pep-0484/
# NOTE: status is **Provisional** as of Python 3.7

# https://github.com/python/mypy
# http://mypy-lang.org/
# pip install mypy


def hello(name: str) -> str:
    return 'Hello ' + name


def double(arg: Union[int, str]) -> Union[int, str]:
    return arg * 2


# Optional[str] is "str or None"
def todays_date_str(format_str: Optional[str] = None) -> str:
    if format_str is None:
        return date.today().isoformat()
    return date.today().strftime(format_str)


def sum_dict_vals(d: Dict[str, int]) -> int:
    return sum(d.values())


# type alias
IntList = List[int]
def sum_list_ints(lst: IntList) -> int:
    return sum(lst)


# "variable-length tuple of homogeneous type, use literal ellipsis" PSF
def sum_tuple_ints(tup: Tuple[int, ...]) -> int:
    return sum(tup)


def print_items(items: Iterable) -> None:
    for item in items:
        print(item)
    return


if __name__ == "__main__":

    print(hello('Guido'))

    print(double(14))
    print(double('abc'))
    print('Causes error in mypy:', double([2]))

    print(todays_date_str())
    print(todays_date_str('%m-%d-%Y'))

    print(sum_dict_vals({'a': 4, 'b': 5, 'c': 6}))
    print(sum_list_ints([1, 2, 3]))

    print(sum_tuple_ints((7, 8, 9)))
    print('Causes error in mypy:', sum_tuple_ints((7, 8, 9.0)))

    print_items((1, 2, 3))
    print_items('abc')
