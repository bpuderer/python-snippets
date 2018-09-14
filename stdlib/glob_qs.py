import glob

for fn in glob.iglob('../**/s*.py', recursive=True):
    print(fn)
