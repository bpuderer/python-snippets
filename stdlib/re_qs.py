import re


# https://docs.python.org/3/library/re.html#regular-expression-syntax
# Use raw string notation for regex patterns
# to avoid collisions with python special characters

text = 'text text [pass] [error] [pass] pass [fail] text'
pattern = r'\[.+?\]'
capture_pattern = r'\[(.+?)\]'


# search looks for *first* match anywhere in string starting at beginning
result = re.search(capture_pattern, text)
print(result.string, result.re.pattern)
print(result.group(0), result.start(), result.end(), result.groups())


# finditer
print()
for result in re.finditer(capture_pattern, text):
    print(result.group(0), result.start(), result.end(), result.groups())


# findall
print()
print(re.findall(pattern, text))
print(re.findall(capture_pattern, text))


# sub
print()
pat = r'(\[)(.+?)(\])'
print(re.sub(pat, '\g<3>\g<2>\g<1>', text))


# split
print()
print(re.split(r'\W+', text))
print(re.split(r'(\W+)', text))


# compile, not necessary for scripts with just a few regex
print()
regex_obj = re.compile(pattern)
print(regex_obj.findall(text))
re.purge() # clear re cache
