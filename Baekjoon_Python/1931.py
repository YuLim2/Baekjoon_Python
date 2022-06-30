import sys
input = sys.stdin.readline

time = []
n = int(input())

for _ in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last = 0
cnt = 0

for i, j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)