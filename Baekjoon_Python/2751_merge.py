import sys
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    ls.append(int(input()))

def merge(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls)//2
    l = merge(ls[:mid])
    r = merge(ls[mid:])
    res = []
    i, j = 0, 0
    while i < len(l) and j <len(r):
        if(l[i] > r[j]):
            res.append(r[j])
            j += 1
        else:
            res.append(l[i])
            i += 1
    if i != len(l):
        res += l[i:]
    if j != len(r):
        res += r[j:]
    return res

res = merge(ls)
for i in res:
    print(i)