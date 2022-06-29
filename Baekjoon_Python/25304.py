import sys
input = sys.stdin.readline

total = int(input())
num = int(input())
for _ in range(num):
    m, n = map(int, input().split())
    total -= n*m
    print(total)
print('NO') if total != 0 else print('YES')
