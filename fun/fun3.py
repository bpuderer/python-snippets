from collections import Counter


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
    word_counts = my_counter(sanitize(string).split())

    occurrences = list(set(word_counts.values()))
    occurrences.sort()
    second_most_common_count = occurrences[-2] # last is most common
    if len(occurrences) < 2:
        return None

    for word, count in word_counts.items():
        if count == second_most_common_count:
            return word


TEST_STR = "\"blah\" A Blah BLAH bl-ah bl-ah BL's bl's bl-AH?"
assert most_common_word(TEST_STR) == 'blah'
assert most_common_word_no_counter(TEST_STR) == 'blah'
assert second_most_common_word_no_counter(TEST_STR) == 'bl\'s'

assert second_most_common_word_no_counter("blah blah blah hey hey my my") == 'hey'


def first_unique_character(string):
    if not string:
        return None
    if len(string) == 1:
        return string
    counts = my_counter(string)
    for char in string:
        if counts[char] == 1:
            return char
    return None

def first_nonunique_character(string):
    if len(string) <= 1:
        return None
    counts = my_counter(string)
    for char in string:
        if counts[char] > 1:
            return char
    return None

assert first_unique_character('aabbcd') == 'c'
assert first_unique_character('aabbccddd') == None
assert first_unique_character('a') == 'a'
assert first_unique_character('') == None


assert first_nonunique_character('abcdad') == 'a'
assert first_nonunique_character('abcddddddddddddeee') == 'd'
assert first_nonunique_character('abcd123xyz') == None
assert first_nonunique_character('z') == None
assert first_nonunique_character('') == None
