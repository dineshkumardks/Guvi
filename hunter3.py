a=int(input())
u=0
t=[int(x) for x in input().split()]
for i in range(0,a):
    if(i==t[i]):
        if(u==0):
          print(i,end="")
          u=1
        else:
            print(" ",end="")
            print(i,end="")
if(u==0):
    print("-1")
