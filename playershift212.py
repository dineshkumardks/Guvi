n,q=map(int,input().split())
a=[int(x) for x in input().split()]
for i in range(0,q):
    x=a[n-1]
    a=[x]+a
    del a[n]
print(*a) 
