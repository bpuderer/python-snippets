
def is_palindrome(s):
    def to_chars(s):
        return ''.join(c for c in s.lower() if c.isalpha())

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            # check first and last char, if False short circuits
            # [1:-1] moves in at each end one char
            return s[0] == s[-1] and is_palindrome(s[1:-1])

    return is_pal(to_chars(s))

print(is_palindrome("A man, a plan, a canal - Panama"))



def print_move(frm, to):
    print(f'move from rod {frm} to rod {to}')

def towers(num_disks, from_rod, to_rod, spare_rod):
    if num_disks == 1:
        print_move(from_rod, to_rod)
    else:
        towers(num_disks-1, from_rod, spare_rod, to_rod)
        towers(1, from_rod, to_rod, spare_rod)
        towers(num_disks-1, spare_rod, to_rod, from_rod)
towers(3, 1, 3, 2)
