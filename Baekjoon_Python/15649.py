import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = []

def f(): # dfs
    if len(ls) == m:
        print(*ls)
        return
    for i in range(1, n+1):
        if i not in ls: # 가지치기
            ls.append(i)
            f()
            ls.pop()

f()