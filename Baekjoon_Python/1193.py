n = int(input())

k = 1
while n > k:
    n -= k
    k += 1

if k % 2 == 0:
    a = n
    b = k - n + 1
else:
    a = k - n + 1
    b = n

print(a, '/', b, sep='')