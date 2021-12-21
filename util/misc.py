from random import randrange
import textwrap
import time


# From Stack Overflow
# http://stackoverflow.com/a/2785908
# http://stackoverflow.com/users/95810/alex-martelli
def wait_until(predicate, timeout=5, period=0.25, *args, **kwargs):
    """periodically check condition is true with timeout"""
    mustend = time.time() + timeout
    while time.time() < mustend:
        if predicate(*args, **kwargs): return True
        time.sleep(period)
    return False


def is_hex(s):
    """check if string is all hex digits"""
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def random_mac(separator='', uppercase=False, oui=''):
    """return random mac address. OUI should not contain separators"""
    if len(oui) == 6 and is_hex(oui):
        digits = textwrap.wrap(oui, 2)
        digits += [format(randrange(256), '02x') for _ in range(3)]
    else:
        digits = [format(randrange(256), '02x') for _ in range(6)]
    if uppercase:
        return separator.join(digits).upper()
    return separator.join(digits).lower()


# https://stackoverflow.com/a/312464
# https://stackoverflow.com/users/14343/ned-batchelder
def chunks(seq, n):
    """yield n-sized chunks from sequence"""
    for start in range(0, len(seq), n):
        yield seq[start:start + n]


def substrings(test_str):
    length = len(test_str)
    return [test_str[i: j+1] for i in range(length) for j in range(i, length)]
    #return [test_str[i: j] for i in range(length) for j in range(i + 1, length + 1)]


# https://stackoverflow.com/a/3844832
def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == x for x in iterator)


if __name__ == "__main__":
    print(random_mac(separator='-'))
    print(random_mac(oui='09be84'))
    print(random_mac(separator=':', uppercase=True))

    print(list(chunks('abcdefghijklmnop', 3)))
    print(list(chunks([1,2,3,4,5,6,7,8,9,10], 3)))

    print(substrings("abcde"))

    print(all_equal([1,1,1,1,1]))
    print(all_equal(iter([1,1,1,2,1])))
