# Some words may repeat

from collections import Counter
l=[]
for i in range(int(input())):
    l.append(input())

c=Counter(l)
print(len(c))
for i in c:
    print(c.get(i),end=' ')
print()


# D21CS105
# Atharva Joshi