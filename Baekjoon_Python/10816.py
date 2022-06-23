import sys
from collections import Counter
from sys import stdin

input = sys.stdin.readline

n = input()
ls1 = list(map(int, input().split()))
m = input()
ls2 = list(map(int, input().split()))

count = Counter(ls1)

for i in range(len(ls2)):
    if ls2[i] in count:
        print(count[ls2[i]], end=' ')
    else:
        print(0, end=' ')