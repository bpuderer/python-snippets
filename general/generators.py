# Resumable function - function is suspended/resumed at yield

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

for n in fib(20):
    print(n)


# PEP 380 subgenerator
# hello world example, need ex with 2 way comm with subgenerator
def f(s):
    yield from s[::-1]
print(list(f('spam')))



# generator expression
# more performant, mem efficient than list comp if only iterating over result once
data = 'abcd'
g = (data[i] for i in range(len(data)-1, -1, -1))
print(list(g))
