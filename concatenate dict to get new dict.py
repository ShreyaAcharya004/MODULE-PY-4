dic1 = {1: 10, 4: 40}
dic2 = {2: 20, 5: 50}
dic3 = {3: 30, 6: 60}

dic4={}

for d in (dic1, dic2, dic3):
        dic4.update(d)

print(dic4)
