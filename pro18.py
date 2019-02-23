def gcd(c,d):
    #toprint(c,d)
    while(c>0):
        c,d=d%c,c
    return(d)
j,k=map(int,input().split())
l=[int(x) for x in input().split()]
for i in range(0,k):
    x,y=map(int,input().split())
    r=l[x-1]
    for j in range(x-1,y):
        #toprint(j)
        r=gcd(r,l[j])
print(r) 
