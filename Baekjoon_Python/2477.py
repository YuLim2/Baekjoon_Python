k = int(input())

w = []
h = []

for _ in range(6):
    n, m = map(int, input().split())
    if n == 1 or n == 2:
        h.append(m)
    else:
        w.append(m)

print((max(h)*max(w) - h[1]*w[2])*k)