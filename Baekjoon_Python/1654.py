k, n = map(int, input().split())
ls = [int(input()) for _ in range(k)]
s, e = 1, max(ls)

while s <= e:
    m = (s+e)//2
    l = 0
    for i in ls:
        l += i//m
    if l >= n:
        s = m+1
    else:
        e = m-1

print(e)