import sys
input = sys.stdin.readline

n = int(input())
INF = sys.maxsize
dp = [[INF]*(1 << n) for _ in range(n)]
graph = []

def dfs(x, visited): # 현재위치
    if visited == (1 << n) - 1:  # 모두 방문햇다면
        return graph[x][0] or INF  # 0으로 가는방법 반환 없으면 INF반환

    if dp[x][visited] is not None:  # 이미 계산되어잇다면
        return dp[x][visited]  # 있는값 반환

    tmp = INF
    for city in range(n):  # 모든 도시에서
        if visited & (1 << city) == 0 and graph[x][city] != 0:  # 아직 방문하지 않았고 cur->i로 가는길이 있다면
            tmp = min(tmp, dfs(city, visited | (1 << city)) + graph[x][city])
    dp[x][visited] = tmp
    return tmp


print(dfs(0, 1 << 0))