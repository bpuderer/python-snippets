# https://docs.python.org/3/whatsnew/3.7.html
# the insertion-order preservation nature of dict objects has been declared to be an official part of the Python language spec.


user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "kenny": "SP",
    "theme": None,
}
user_preferences["currency"] = "USD"

# for del, KeyError if key does not exist
print(user_preferences.get("kenny"))
del user_preferences["kenny"]

# pop- remove key and return, KeyError if key does not exist and no default is passed
print(user_preferences.pop("kenny1", None))
print(user_preferences.get("kenny"))
print(user_preferences.get("kenny", "default on get"))



def remove_none_from_dict(dct):
    return {k: v for k, v in user_preferences.items() if v is not None}

print(remove_none_from_dict(user_preferences))

