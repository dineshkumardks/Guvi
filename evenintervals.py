m,n=input().split()
odd=[]
even=[]
if(m.isnumeric()):
	m=int(m)
	if(n.isnumeric()):
		n=int(n)
		m=m+1
		for i in range(m,n):
			if(i%2!=0):
				odd.append(i)
			else:
				even.append(i)
		
		print(even)
	else:
		print("invalid")
else:
    print("invalid")
