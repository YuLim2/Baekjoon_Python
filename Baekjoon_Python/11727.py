ls = [0, 1, 3]
for i in range(3, 1001):
    ls.append((ls[i - 2] * 2) + ls[i - 1])
n = int(input())
print(ls[n] % 10007)