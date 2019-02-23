n=int(input())
l=[]
m=[]
for i in range(0,n):
    l=[int(x) for x in input().split()]
    for j in range(0,len(l)):
        m.append(l[j])
    l=[]    
m.sort()
print(*m)
