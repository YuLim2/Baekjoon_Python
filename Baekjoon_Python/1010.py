num = int(input())

def f(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

for _ in range(num):
    n, m = map(int, input().split())
    print(f(m-1)*f(n))