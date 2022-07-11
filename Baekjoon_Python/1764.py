import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = set()
lo = set()
for _ in range(n):
    ls.add(input())

for _ in range(m):
    lo.add(input())

result = sorted(list(ls & lo))

print(len(result))
print(*result, sep='')