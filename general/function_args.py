# args=tuple, kwargs=dict
def ftn(a, b=0, *args, **kwargs):
    print(f"a={a} b={b} args={args} kwargs:{kwargs}")


ftn(1)
ftn(1, 2)
ftn(1, 2, 3)
ftn(1, c=42)


# unpack list or tuple
# https://docs.python.org/3.7/tutorial/controlflow.html#unpacking-argument-lists
# PEP 448 added unbounded number of * and ** unpackings
lst = [1, 2, 3]
tup = (4, 5, 6)
ftn(*lst, *tup)

# unpack dict
d1 = {'a': 99, 'c': 42}
d2 = {'d': 43}
ftn(**d1, **d2)

# both
ftn(*lst, *tup, **d2)  # cannot unpack d1 because multiple vals for a: TypeError


# PEP 3102 keyword only args
def ftn2(a, *, b=None, c):
    print(f"a={a} b={b} c={c}")

# b and c must be specified by keyword
ftn2(1, c=3)
ftn2(1, b=2, c=3)


# forwarding arguments
def trace(f, *args, **kwargs):
    print(f'args:{args} kwargs:{kwargs}')
    result = f(*args, **kwargs)
    print('result =', result)
    return result

print(trace(int, 'fe', base=16))
