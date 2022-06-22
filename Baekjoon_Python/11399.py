import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
ls.sort()
num = 0

for i in range(n):
    n_ls = ls[:i+1]
    num += sum(n_ls)

print(num)