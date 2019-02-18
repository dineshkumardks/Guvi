n=int(input())
m=[]
b=[]
for i in range(0,n):
    m=[int(x) for x in input().split()]
    for j in range(0,len(m)):
        b.append(m[j])
    m=[]    
b.sort()
print(*b)
