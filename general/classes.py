"""https://www.youtube.com/watch?v=HTLu2DFOdTg

great presentation from Raymond Hettinger
most docstrings below quote and paraphrase RH
"""

class MyClass:

    version = '0.1'    # class variable. be very careful with mutables
    _spam = 1234       # name prefixed with underscore should be treated as non-public

    def __init__(self, val):
        """dunder init is not a constructor.

        self is the instance that has already been made when init is called.
        it is an initializer that populates self.
        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=7m40s """
        self.lst = []
        self.val = val

    def add(self, x):
        self.lst.append(x)

    def double_add(self, x):
        self.add(x)    # method calling another method
        self.add(x)

    def foo(self):
        """return double bar"""
        return self.__bar() * 2

    def bar(self):
        """bar returns 100% of val"""
        return self.val * 1.0

    @staticmethod
    def func_in_class():
        """purpose of static method is to attach functions to classes

        why? because that's where people look for it
        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=30m8s"""
        return "just a function hanging out in a class"

    @classmethod
    def from_triple_val(cls, tval):
        """alternative constructor

        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=23m28s"""
        val = tval / 3
        return cls(val)

    def __str__(self):
        return f'val:{self.val}  lst:{self.lst}  ver:{self.version}'

    def __add__(self, other):
        tmp = MyClass(self.val + other.val)
        tmp.lst = self.lst + other.lst
        return tmp

    # private copy using name mangling used to prevent clashes with subclass
    # class local reference. __bar replaced with _MyClass__bar
    # https://www.youtube.com/watch?v=HTLu2DFOdTg&t=33m25s
    __bar = bar


class MyClass2(MyClass):
    """MyClass2 inherits from MyClass"""

    def double_add(self, x):
        """override double_add to add a value doubled to lst, not add twice"""
        self.add(x*2)

    def bar(self):
        """override bar to return 110% of val"""
        return MyClass.bar(self) * 1.1



c1 = MyClass(42)
print(c1.foo(), c1.bar())
c1.add(2112)
c1.double_add(2001)
print(c1)


print('--')


c2 = MyClass2(42)
print(c2.foo(), c2.bar())    # foo uses MyClass bar, not MyClass2 bar
c2.add(2112)
c2.double_add(2001)
print(c2)


print('--')


c3 = MyClass.from_triple_val(27)    # alt constructor
print(c3)


print('--')


print(MyClass.func_in_class())
print(c1 + c2)
