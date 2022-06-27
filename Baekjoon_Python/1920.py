import sys
input = sys.stdin.readline

n = int(input())
ln = set(map(int, input().split()))
m = int(input())
lm = list(map(int, input().split()))

for i in lm:
    print(1) if i in ln else print(0)