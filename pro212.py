n,m=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,m):
    a,b=map(int,input().split())
    c=0
    for j in range(a-1,b):
        c=c+l[j]
print(c) 
