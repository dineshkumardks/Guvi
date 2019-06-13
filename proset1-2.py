from itertools import combinations
ltr1,num1=map(int,input().split())
num2=len(str(ltr1))
a=list(combinations(str(ltr1),num2-num1))
a=(sorted(a))
b="".join(a[0])
print(b)
