b,d,=map(int,input().split())
for i in range(b,d):
 y=i
 t=0
 u=0
 while(y>0):
    c=y%10
    c=c*c*c
    u=u+c
    y=int(y/10)
 if(u==i):
   if(t==1):  
        print("  ")
        print(u,end=" ")
   else:
        print(u,end=" ")
        t=1
