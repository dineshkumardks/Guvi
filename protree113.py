n,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,k):
    a,b=map(int,input().split())
    tmp=999999999
    for j in range(a-1,b):
        if(l[j]<temp):
            tmp=l[j]
print(tmp)        
