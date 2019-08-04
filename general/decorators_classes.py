# must be callable to be used as decorator
class CallCounter:
    def __init__(self, f):
        self.f = f
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCounter
def func():
    pass


for _ in range(28):
    func()
print(f'func was called {func.count} times')




class Debug:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if self.enabled:
                print(f'arguments: {args} {kwargs}')
            return f(*args, **kwargs)
        return wrapper

debugger = Debug()

@debugger
def swap(a, b):
    return b, a

print(swap(1, 2))
debugger.enabled = False
print(swap(3, 4))
