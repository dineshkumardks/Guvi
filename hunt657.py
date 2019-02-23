n=int(input())
rep=list(map(int,input().split()))
for i in range(n):
	      if rep.count(rep[i])==1:
print(rep[i])
