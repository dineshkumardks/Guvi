b=int(input())
m=[int(x) for x in input().split()]
m.sort()
for i in range(0,b,2):
    if(i==b-1):
        print(m[b-1])
    else:    
     if(m[i]!=m[i+1]):
        print(m[i])
        break;
