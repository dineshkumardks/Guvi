a=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
for i in range(0,len(b)-1):
	if b[i]==0:
		b[i]="x"
	else:
		break
for i in range(0,len(b)):
	if b[i]!="x":
         print(b[i],sep="",end="")
