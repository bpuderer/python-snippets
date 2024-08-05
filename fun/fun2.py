# Run-length encoding
# https://en.wikipedia.org/wiki/Run-length_encoding

def encode_string(string):
    if not string:
        return ''

    result = []
    prev_char = string[0]
    count = 1
    for ch in string[1:]:
        if ch == prev_char:
            count += 1
        else:
            # character changed
            result.extend([prev_char, str(count)])
            prev_char = ch
            count = 1

    # have to run again since seeing a different char is what appends to result
    result.extend([prev_char, str(count)])
    return ''.join(result)


test_str = 'aaabbbbbbbbbbbcccaab'
assert encode_string(test_str) == 'a3b11c3a2b1'
assert encode_string('') == ''
assert encode_string('z') == 'z1'
assert encode_string('za') == 'z1a1'
assert encode_string('zza') == 'z2a1'
