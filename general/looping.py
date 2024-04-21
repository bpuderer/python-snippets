import random
from math import sqrt


# continue - continue with next iteration of loop
for letter in "Spam, Spam, Spam, egg and Spam":
    if letter == "p":
        continue
    print(letter, sep='', end='')
print()


# no do-while in python
# https://www.python.org/dev/peps/pep-0315/
# https://mail.python.org/pipermail/python-ideas/2013-June/021610.html
# while True:
#    <code>
#    if condition:
#        break


while True:
    i = random.randint(0, 5)
    if i == 3:
        break
    print(i, "!= 3, trying again")


def is_prime(num):
    if num <= 1:
        return False
    for factor in range(2, int(sqrt(num)) + 1):
    #for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True
primes_up_to_twenty = [num for num in range(2, 20) if is_prime(num)]
print(primes_up_to_twenty)

def all_primes_up_to(up_to_num):
    # more efficient
    primes = [2]
    for num in range(3, up_to_num):
        sqrt_num = sqrt(num)
        for factor in primes:
            if num % factor == 0:
                # not a prime
                break
            if factor > sqrt_num:
                # is a prime
                primes.append(num)
                break
    return primes
print(all_primes_up_to(20))


# https://www.youtube.com/watch?v=OSGv2VnC0go#t=15m52s
# Raymond Hettinger
# same as list.index but returns -1 instead of ValueError if value not present
# else clause runs if not interrupted by break or return
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

lst = [1, 2, 13, -5]
print(find(lst, 13))
print(find(lst, 42))
