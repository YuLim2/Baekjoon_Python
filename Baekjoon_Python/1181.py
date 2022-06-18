import sys
input = sys.stdin.readline

n = int(input())
ls = []

for _ in range(n):
    ls.append(input().strip()) # '\n'제외하여 입력

ls = list(set(ls))
ls.sort()
ls.sort(key=len)

for i in ls:
    print(i)