# 백준에서 pypy로 제출해야 함
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = map(int, input().split())

start, end = 0, max(ls)

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in ls:
        if i > mid:
            tree += i - mid
    if tree >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)