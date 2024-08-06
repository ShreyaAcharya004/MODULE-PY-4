l=[1,2,3,,4,4,5,5,6,6]
x=[]

for i in l:
    if i not in x:
        x.append(i)
        print(x) 
