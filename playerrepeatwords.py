a=list(input())
tmp1=0
tmp2=0
for i in range(0,len(a)):
    n=a.count(a[i])
    if(n>tmp1):
        tmp1=n
        tmp2=a[i]
print(tmp2) 
