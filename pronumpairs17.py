n,k=map(int,input().split())
a=0
s=[int(x) for x in input().split()]
for i in range(0,n):
    for j in range(0,n):
        if(i!=j):
            if(s[i]+s[j]==k):
                a=1
                break
if(a==0):
    print("no")
else:
    print("yes")
