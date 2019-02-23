s1,s2=input().split()
i=0
tmp=0
while i+2<=len(s1):
	      if s1[i:i+2] in s2:
		          tmp=1
		          print("yes")
		          break
	      i+=1
if tmp==0:
      print("no")
