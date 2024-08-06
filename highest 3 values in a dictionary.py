d = {'a': 10, 'b': 20, 'c': 60, 'd': 17, 'e': 28}

sorted_values = sorted(d.values(), reverse=True)
highest_3 = sorted_values[:3]

print("Highest 3 values in the dictionary:", highest_3)
