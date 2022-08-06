# pypy3으로 제출해야 됨
import sys
input = sys.stdin.readline

def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

while True:
    n = int(input())
    cnt = 0
    if n == 0: break
    for i in range(n+1, n*2+1): # n~2n까지 소수인지 판별하여 cnt++
        if sosu(i):
            cnt += 1
    print(cnt)