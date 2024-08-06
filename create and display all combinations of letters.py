data = {'1': ['o', 'p'], '2': ['q', 'r']}

combinations = []

for key, values in data.items():
    if not combinations:
        combinations.extend(values)
    else:
        new_combinations = []
        for combination in combinations:
            for value in values:
                new_combinations.append(combination + value)
        combinations = new_combinations

print(" Output:")
print(" ".join(combinations))
