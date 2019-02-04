b,c=input().split()
a=0
for i in range(0,len(b)):
    if(b[i]!=c[i]):
        a+=1
    if(a>1):
        break;
if(a<=1):
    print("yes")
else:
    print("no")
