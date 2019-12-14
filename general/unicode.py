# comments, code, everything below from Ned Batchelder's Pragmatic Unicode
# Thanks Ned!!!
# Essential viewing, reading:
# https://www.youtube.com/watch?v=sgHbC6udIqc
# http://nedbatchelder.com/text/unipain.html

# http://unicode.org/charts/

# I/O is always bytes
# everything in a computer is bytes, files on disk, network connections
# need convention to give bytes meaning

# The best strategy is to decode incoming bytes as soon as possible,
# producing unicode. You use unicode throughout your program,
# and then when outputting data, encode it to bytes as late as possible.

# At any point in your program, you need to know whether you have a byte string
# or a unicode string. This shouldn't be a matter of guessing, it should be by design.
# In addition, if you have a byte string, you should know what encoding it is
# if you ever intend to deal with it as text.

# unicode- code points
# code point- number for each character 0-10FFFF
# normally referred to by "U+" followed by number

# str- sequence of code points (unicode)
# bytes- a sequence of bytes


# Hi ℙƴ☂ℌøἤ
s = 'Hi \u2119\u01b4\u2602\u210c\xf8\u1f24'
print(s, type(s))


# encode- code points -> bytes
# default encoding is 'utf-8'
# https://docs.python.org/3/library/stdtypes.html#str.encode
b_utf8 = s.encode()
print(b_utf8, type(b_utf8))


# decode- bytes -> code points
# default encoding is 'utf-8'
# https://docs.python.org/3/library/stdtypes.html#bytes.decode
s_back = b_utf8.decode()
print(s_back, type(s_back))


s_3_4 = '¾'
# ord returns code point for single char str
print(ord(s_3_4))
# chr returns single char str for code point
print(chr(190))
