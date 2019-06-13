c,d=map(str,input().split())
v=abs(len(c)-len(d))
for i in range(len(c)):
        if len(d)==1 and d[i] in c:
            break
        if c[i]!=d[i]:
            v=v+1
print(v)
