n = int(input())
res = 0
for i in range(1, n):
    ls = list(map(int, str(i)))
    res = i+sum(ls)
    if res == n:
        res = i
        break
print(res)