import argparse

# python3 argparse_qs.py blah --port 8080 --storefalse --loglevel DEBUG --const --multiple 1 --multiple 2 --twovals 2 1


parser = argparse.ArgumentParser(description='argparse demo', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# default type is string, default action=store

# positional arguments do not begin with '-'
parser.add_argument("positional", help="help for positional arg")

# optional args begin with '-'
parser.add_argument("--optional", "-opt", default="default value")

# int, required
parser.add_argument("--port", type=int, required=True)

# default values are False and True respectively
parser.add_argument("--storetrue", action="store_true")
parser.add_argument("--storefalse", action="store_false")

# restricted set of vals
parser.add_argument("--loglevel", choices=["TRACE", "DEBUG", "WARN", "INFO", "ERROR"], default="INFO")

# store constant
parser.add_argument("--const", action="store_const", const=42.)

# append to list
parser.add_argument("--multiple", action="append")

# append to list
# https://docs.python.org/3/library/argparse.html#nargs
parser.add_argument("--twovals", nargs=2)


args = parser.parse_args()

print("args.positional:", args.positional)
print("args.optional:", args.optional)
print("args.port:", args.port, type(args.port))
print("args.storetrue:", args.storetrue)
print("args.storefalse:", args.storefalse)
print("args.loglevel:", args.loglevel)
print("args.const:", args.const, type(args.const))
print("args.multiple:", args.multiple)
print("args.twovals:", args.twovals)
