import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(int(input()))

ls = list(reversed(ls))

cnt = 0
for i in ls:
    cnt += k//i
    k = k%i

print(cnt)