from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    v_ls[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if v_ls[i] == 0 and graph[v][i] == 1:
                q.append(i)
                v_ls[i] = 1

def dfs(v):
    v_ls2[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if v_ls2[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
v_ls = [0] * (n+1)
v_ls2 = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


dfs(v)
print()
bfs(v)