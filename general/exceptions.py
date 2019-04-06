from contextlib import suppress

try:
    # pass
    # print(idontexist)
    raise ValueError('ValueError message')
    # 5/0
except NameError as e:
    print(e)
except (AssertionError, ValueError) as e:
    print(e)
except:
    print("something unexpected happened. re-raising")
    raise
else:
    print("executes if no exception in try clause")
finally:
    print("always executes")


print('---')

# https://docs.python.org/3/library/contextlib.html#contextlib.suppress
with suppress(FileNotFoundError):
    print('before exception')
    raise FileNotFoundError
    print("after exception - won't execute")
print('after context')
