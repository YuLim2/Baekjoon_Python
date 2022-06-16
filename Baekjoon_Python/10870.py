import sys
input = sys.stdin.readline

n = int(input())
a = [0, 1, 1]

def fibo(n):
    if n < 3:
        return a[n]
    n -= 2
    for i in range(n):
        a[i%3] = a[(i-1)%3] + a[(i-2)%3]
        if i == n-1:
            return a[i%3]

print(fibo(n))