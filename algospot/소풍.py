import sys
input = sys.stdin.readline

def dfs(start, friend):
    if not friend:
        return 1
    res = 0

    for i in range(start, n):
        if not visited[i]:
            for j in range(i+1, n):
                if not visited[j] and isFriend[i][j]:
                    visited[i] = visited[j] = True
                    res += dfs(i, friend-2)
                    visited[i] = visited[j] = False
    return res

n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    visited = [False]*n
    isFriend = [[False]*n for _ in range(n)]
    ls = list(map(int, input().split()))

    for i in range(0, len(ls), 2):
        isFriend[ls[i]][ls[i+1]] = True
        isFriend[ls[i+1]][ls[i]] = True

    print(dfs(0, n))