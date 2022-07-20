import sys
input = sys.stdin.readline

n = int(input())
ls = []

for _ in range(n):
    x, y = map(int, input().split())
    ls.append((x, y))

for i in ls:
    cnt = 1
    for j in ls:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')