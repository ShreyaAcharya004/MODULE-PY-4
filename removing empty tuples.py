t=[('samm','5','70'),(),('Romanne','8','45'),(),('Shane','3','60')]

for i in t:
    if(len(i) == 0):
        t.remove(i)
        print(t)
