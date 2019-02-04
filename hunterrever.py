a=list(input().split())
b=[]
for i in range(0,len(a)):
    b=list(a[i])
    b.reverse()
    if(i!=len(a)-1):
      print(''.join(b),end=" ")
    else:
      print(''.join(b),end="")
