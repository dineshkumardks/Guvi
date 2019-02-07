c=input()
tmp=[]
from itertools import permutations
perm = [''.join(p) for p in permutations(c)]
for i in range(len(perm)):
    if perm[i] not in tmp:
        tmp.append(perm[i])
for i in range(len(tmp)):
        print (tmp[i])
