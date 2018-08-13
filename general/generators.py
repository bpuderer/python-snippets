# Resumable function - function is suspended/resumed at yield

def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

for n in fib(20):
    print(n)


# generator expression
# more performant, mem efficient than list comp if only iterating over result once
data = 'abcd'
g = (data[i] for i in range(len(data)-1, -1, -1))
for char in g:
    print(char)
