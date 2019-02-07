a=int(input())
y=[int(x) for x in input().split()]
d=[]
for i in range(0,a):
    x=y.count(y[i])
    d.append(x)
x=d.index(1)
print(y[x])
