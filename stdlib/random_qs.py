import random
import string


# int
print('random int [1, 3]:', random.randint(1, 3))
# like built in range, stop value is exclusive
print('random int range(5):', random.randrange(5))
print('random int range(0, 10, 2):', random.randrange(0, 10, 2))


# sequence
print('random lower-case letter:', random.choice(string.ascii_lowercase))
# sample means no repeated selections thus sample size cannot be bigger than population
print('5 samples from lower-case letters:', random.sample(string.ascii_lowercase, 5))

# float
print('random float [0.0, 1.0):', random.random())
print('random float [1.21, 3.14]:', random.uniform(1.21, 3.14))
