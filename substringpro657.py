a,b=input().split()
i=0
tmp=0
while i+2<=len(a):
	if a[i:i+2] in b:
	      tmp=1
              print("yes")
              break
	i+=1
if tmp==0:
       print("no")
