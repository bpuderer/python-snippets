import random


# continue - continue with next iteration of loop
for letter in "Spam, Spam, Spam, egg and Spam":
    if letter == "p":
        continue
    print(letter, sep='', end='')
print()


# no do-while in python
# https://www.python.org/dev/peps/pep-0315/
# while True:
#    <setup code>
#    if not <condition>:
#        break
#    <loop body>


while True:
    i = random.randint(0, 5)
    if i == 3:
        break
    print(i, "!= 3, trying again")


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
