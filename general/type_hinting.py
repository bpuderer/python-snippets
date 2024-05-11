# https://github.com/python/mypy
# https://peps.python.org/pep-0484/
# https://docs.python.org/3/library/typing.html

def my_function(my_parameter: int) -> str:
    print(my_parameter)
    return 'demo'

def my_function2(my_parameter: str) -> None:
    pass

def another_function(my_parameter: list[int]):
    pass

def mult_return_types(my_parameter: int) -> str | None:
    if my_parameter < 0:
        return 'negative'
    return None


#my_function("abc")  # arg-tye error from mypy
my_function(10)
my_function2(my_function(0))

#another_function(['1', 2, '3'])  # list-item error from mypy
another_function([1, 2, 3])
my_list: list[int] = [1, 2]
another_function(my_list)

#a: int = 'abc'  # assignment error from mypy
a: int = 5
print(mult_return_types(-1))
print(mult_return_types(a))

my_dict: dict[int, str] = {0: "zero", 1: "one"}

test_dict = dict[str, list[str]]
my_dict2: test_dict = {"abc": ["x", "y", "z"]}
