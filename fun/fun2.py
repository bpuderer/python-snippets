# Run-length encoding
# https://en.wikipedia.org/wiki/Run-length_encoding


def encode_string(string):
    result = []
    prev_char = string[0]
    count = 0
    for ch in string:
        if ch != prev_char:
            # there was a change
            result.append((prev_char, count))
            count = 0

        prev_char = ch
        count += 1

    # have to run again since seeing a different char is what appends to result
    result.append((prev_char, count))
    return result


def decode_string(encoded_list):
    return ''.join((letter*num for letter, num in encoded_list))


test_str = 'aaabbbbbbcccaab'
assert encode_string(test_str) == [('a', 3), ('b', 6), ('c', 3), ('a', 2), ('b', 1)]
assert test_str == decode_string(encode_string(test_str))
