def update_dict_val(d, this_key, new_val):
    for k, v in d.items():
        if isinstance(v, dict):
            update_dict_val(v, this_key, new_val)
        elif k == this_key:
            d[this_key] = new_val

d = {'a': 1, 'b': {'2a': 9, '2b': {'3b': 10, '3c': {'4b': [1,2,3]}}}}
print(d)
update_dict_val(d, '3b', 11)
print(d)
