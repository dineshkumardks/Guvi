c,d=map(int,input().split())
n=[int(x) for x in input().split()]
n.sort()
n.reverse()
print(n[d-1])
