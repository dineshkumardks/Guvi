b=int(input())
v=list(input())
h=[]
for i in range(0,len(v)):
    if(v[i]!='a' and v[i]!='e' and v[i]!='i' and v[i]!='o' and v[i]!='u' and v[i]!='A' and v[i]!='E' and v[i]!='I' and v[i]!='O' and v[i]!='U'):
        h.append(v[i])
h.reverse()
print(''.join(h))
