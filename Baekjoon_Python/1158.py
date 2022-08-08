import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = [i for i in range(1, n+1)]
result = []
num = 0
for i in range(n):
    num+=(k-1)
    if num >= len(ls):
        num %= len(ls)
    result.append(ls[num])
    ls.pop(num)
print('<', end='')
print(*result, sep=', ', end='')
print('>')