n = int(input())
ls = [float(input()) for _ in range(n)]

for i in range(1, n):
    ls[i] = max(ls[i], ls[i]*ls[i-1])
print("%.3f" % (max(ls)))
