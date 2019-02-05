s=input()
a=[]
for i in range(0,len(s)-1,2):
    a.append(s[i+1])
    a.append(s[i])
print("".join(a))    
