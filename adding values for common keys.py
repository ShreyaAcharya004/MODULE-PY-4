d1 = {'a': 15, 'b': 30, 'c':40}
d2 = {'x': 100, 'b': 200, 'z': 300}

for i in d2:
    if i in d1:
        d2[i] = d2[i] + d1[i]
    else:
        pass
         
print(d2)
