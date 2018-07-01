# args=tuple, kwargs=dict
def ftn(a, b=0, *args, **kwargs):
    print("a b args kwargs:", a, b, args, kwargs)


ftn(1)
ftn(1, 2)
ftn(1, 2, 3)
ftn(1, c=42)

# unpack list or tuple
lst = [1, 2, 3]
ftn(*lst)

# unpack dict
d = {'c': 42}
ftn(1, **d)


# PEP 3102 keyword only args
def ftn2(a, *, b=None, c):
    print("a b c", a, b, c)

# b and c must be specified by keyword
ftn2(1, c=3)
ftn2(1, b=2, c=3)
