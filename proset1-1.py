b=int(input())
m=[]
for i in range(0,b):  
    d=input()
    m.append(d)
list=[]
for i in zip(*m):
    if (i.count(i[0])==len(i)): 
        list.append(i[0])
    else:
        break
print(''.join(list))
