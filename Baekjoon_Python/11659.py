import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

for i in range(n-1):
    ls[i+1] += ls[i]
ls = [0] + ls

for _ in range(m):
    a,b = map(int,input().split())
    print(ls[b]-ls[a-1])