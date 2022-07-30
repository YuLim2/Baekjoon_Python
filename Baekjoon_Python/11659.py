import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    print(sum(ls[a-1:b]))