import copy

# "Assignment statements in Python do not copy objects" - PSF
# typical interview question, assignment/copy/deepcopy

d = {'a': [0, 1]}
#d_copy = copy.copy(d)   # shallow copy, same as:  d_copy = d.copy()
d_copy = copy.deepcopy(d)
d_copy['a'].append(2)
print(d, d_copy)
