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



if __name__ == "__main__":
    print(random_mac(separator='-'))
    print(random_mac(oui='09be84'))
    print(random_mac(separator=':', uppercase=True))

    print(list(chunks('abcdefghijklmnop', 3)))
    print(list(chunks([1,2,3,4,5,6,7,8,9,10], 3)))
