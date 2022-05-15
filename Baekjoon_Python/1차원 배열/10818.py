n = int(input())
a = list(map(int, input().split()))
MAX = a[0]
MIN = a[0]

for i in range(n):
    if a[i] > MAX:
        MAX = a[i]
    elif a[i] < MIN:
        MIN = a[i]

print(MIN, MAX)
