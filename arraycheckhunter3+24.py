a,b=map(int,input().split())
c=0
d=[int(x) for x in input().split()]
for i in range(0,a-1):
    for j in range(i+1,a):
        if(d[i]+d[j]==b):
            c=1
            break;
if(c==0):
    print("NO")
else:
    print("YES")
