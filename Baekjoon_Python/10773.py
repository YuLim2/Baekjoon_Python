import sys
input = sys.stdin.readline

n = int(input())
ls = []

for _ in range(n):
    num = int(input())
    if num == 0:
        ls.pop()
    else:
        ls.append(num)

print(sum(ls))