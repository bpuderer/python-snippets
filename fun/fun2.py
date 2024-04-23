from collections import Counter


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



def sanitize(string):
    tmp = (ch for ch in string.lower() if ch.isalpha() or ch.isdigit() or ch in [' ', '-', '\''])
    return ''.join(tmp)

def most_common_word(string):
    ctr = Counter(sanitize(string).split())
    # Elements with equal counts are ordered in the order first encountered
    return ctr.most_common(1)[0][0]

def my_counter(iterable):
    # https://docs.python.org/3/whatsnew/3.7.html  June 27, 2018
    # the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.
    d = {}
    for item in iterable:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d

def most_common_word_no_counter(string):
    d = my_counter(sanitize(string).split())
     # https://docs.python.org/3/library/functions.html#max
    # If multiple items are maximal, the function returns the first one encountered.
    return max(d, key=d.get)

def second_most_common_word_no_counter(string):
    # 'second most' here has a smaller number of occurrences than the most
    d = my_counter(sanitize(string).split())

    occurences = list(d.values())
    occurences.sort(reverse=True)
    max = occurences[0]

    for val in occurences:
        if val < max:
            second_max = val
            break
    else:
        return None    # all words have same num occurences or there's only one

    for k, v in d.items():
        if v == second_max:
            return k


TEST_STR = "\"blah\" A Blah BLAH bl-ah bl-ah BL's bl's bl-AH?"
assert most_common_word(TEST_STR) == 'blah'
assert most_common_word_no_counter(TEST_STR) == 'blah'
assert second_most_common_word_no_counter(TEST_STR) == 'bl\'s'

assert second_most_common_word_no_counter("blah blah blah hey hey my my") == 'hey'


def first_unique_character(string):
    d = my_counter(string)
    for k, v in d.items():
        if v == 1:
            return k
    return None

def first_nonunique_character(string):
    d = my_counter(string)
    for k, v in d.items():
        if v > 1:
            return k
    return None

assert first_unique_character('aabbcd') == 'c'
assert first_unique_character('aabbccddd') == None

assert first_nonunique_character('abcdddddddddddd') == 'd'
assert first_nonunique_character('abcddddddddddddeee') == 'd'
assert first_nonunique_character('abcd123xyz') == None
