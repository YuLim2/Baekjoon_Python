import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
ls = []
for i in range(n, m+1):
    if i != 1:
        ok = True
        for j in range(2, i):
            if i % j == 0:
                ok = False
                break
        if ok:
            ls.append(i)
if len(ls) == 0:
    print(-1)
else:
    print(sum(ls))
    print(min(ls))