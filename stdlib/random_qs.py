import random
import string


# int
print('random int [1, 3]:', random.randint(1, 3))
print('random int range(5):', random.randrange(5))
print('random int range(1, 10, 2):', random.randrange(1, 10, 2))


# sequence
print('random lower-case letter:', random.choice(string.ascii_lowercase))


# float
print('random float [0.0, 1.0):', random.random())
print('random float [1.21, 3.14]:', random.uniform(1.21, 3.14))
