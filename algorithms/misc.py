# 100 doors puzzle
doors = [False] * 101

for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

true_vals = [i+1 for i, val in enumerate(doors[1:]) if val]
print(true_vals)


# nums divisible by 2
sol_brute_force = [i for i in range(1, 11) if i % 2 == 0]
sol_better = [i for i in range(2, 11, 2) if i % 2 == 0]
assert sol_brute_force == sol_better == [2, 4, 6, 8, 10]
