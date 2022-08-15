import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = []

def f(a): # dfs
    if len(ls) == m:
        print(*ls)
        return
    for i in range(a, n+1):
        if i not in ls: # 가지치기
            ls.append(i)
            f(i+1)
            ls.pop()

f(1)