def doubler(n):
    return n * 2


nums = [i for i in range(1, 11)]

print(f"nums: {nums}")
print("--")

print("each nums val doubled:")
print(list(map(doubler, nums)))
print([num*2 for num in nums])
print("--")

print("even nums vals:")
print(list(filter(lambda x: x % 2 == 0, nums)))
print([num for num in nums if num % 2 == 0])
print("--")

print("doubled nums which are divisible by 3:")
print(list(filter(lambda x: x % 3 == 0, map(doubler, nums))))
print([num*2 for num in nums if num*2 % 3 == 0])

