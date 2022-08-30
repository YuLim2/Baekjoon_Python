import itertools
from itertools import combinations

nums = []
ls = list(list(map(int, input().split())) for _ in range(19))
rls = [[0] * 19 for i in range(19)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    nums.append(x-1)
    nums.append(y-1)

nums = set(nums)
nums = itertools.product(nums, repeat = 2)

for i in nums:
    x, y = i[0], i[1]
    print(x, y)
    rls[y][x] = ls[y][x]
    print(rls[y][x])
    if rls[y][x] == 1: rls[y][x] = 0
    elif rls[y][x] == 0: rls[y][x] = 1
    ls[y][x] = rls[y][x]

for i in range(19):
    for j in range(19):
        print(rls[i][j], end=' ')
    print()