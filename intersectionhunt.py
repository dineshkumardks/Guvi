x,k=map(int,input().split())
arr=[]
for i in range(x):
	arr1=list(map(int,input().split()))
	arr.append(set(arr1))
setEx=set.intersection(*arr)
print(*setEx)
