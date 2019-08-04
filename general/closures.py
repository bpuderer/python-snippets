def enclosing():
    x = 'closed over'
    def local_func():
        print(x)
    return local_func


lf = enclosing()
print(lf.__closure__)
lf()
print(lf.__closure__)
