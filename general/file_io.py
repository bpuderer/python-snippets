test_file = 'file_io_demo.txt'

# use with() to ensure file is closed
# 'w' overwrites, 'a' appends, 'r' for reading (default), 'r+' for reading and writing
# add 'b' to end for binary files
# can also use multiple open statements within single with()
# ex. with open('temp1.txt') as f1, open('temp2.txt') as f2:


with open(test_file, 'w') as f:
    f.write('first line\n')


with open(test_file, 'a') as f:
    lines = ['second line\n', 'third line\n']
    f.writelines(lines)


# f.read(size)
# omit size to read entire file at once
with open(test_file) as f:
    print("all lines as str:", f.read())


# read single line. includes \n unless last line and file
# doesn't end with a \n
with open(test_file) as f:
    print("line 1:", f.readline())


print("line by line:")
with open(test_file) as f:
    for line in f:
        print(line)


with open(test_file) as f:
    print("all lines as list:", list(f))
    #print("all lines as list:", f.readlines())
