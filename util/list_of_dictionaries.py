""" list of dictionaries helpers """


def exists_lod(lst, key, val):
    """is key-value in list of dicts"""
    return any(d[key] == val for d in lst)

def index_lod(lst, key, val):
    """index of first occurrence key-value in list of dicts"""
    return next((i for (i, x) in enumerate(lst) if x[key] == val), -1)

def find_lod(lst, key, val):
    """get dict of first match of name-value pair in list of dicts"""
    return next((x for x in lst if x[key] == val), None)

def findall_lod(lst, key, val):
    """get list of dicts of all matches of key-value pair in list of dicts"""
    return [x for x in lst if x[key] == val]

def remove_lod(lst, key, val, only_first_occur=False):
    """remove from list matches of key-value pair in list of dicts"""
    for i in range(len(lst)-1, -1, -1):
        if lst[i][key] == val:
            del lst[i]
            if only_first_occur:
                return


if __name__ == "__main__":
    lst = [{'a': 0}, {'a': 1, 'b': 1}, {'a': 2}, {'a': 1}, {'a': 5}]
    print(exists_lod(lst, 'a', 3))
    print(exists_lod(lst, 'a', 2))

    print(index_lod(lst, 'a', 1))

    print(find_lod(lst, 'a', 1))
    print(findall_lod(lst, 'a', 1))

    print('---')
    remove_lod(lst, 'a', 1)
    #remove_lod(lst, 'a', 1, True)
    print(lst)
