n=int(input())
inc=list(map(int,input().split()))
l=0
c=1
for i in range(n-1):
	      if  inc[i]<inc[i+1]:
                  c+=1
		              if i==n-2:
			                    if c>l:
				                       l=c
				else:
		          if c>l:
			             l=c
		          c=1
print(l)
