p=int(input())
i=0
while(p>0):
    x=p%10
    i=i+(x*x)
    p=int(p/10)
print(i) 
