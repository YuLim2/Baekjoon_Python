import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] * n for _ in range(n + 1)]  # 총 입력이 되는 2차원 배열
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 각 노드에 연결된 값 정리
    graph[b].append(a)

cnt = 0
visited = [0] * (n + 1) # 방문 체크 변수


def dfs(start):
    global cnt
    visited[start] = 1  # 방문 체크
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


dfs(1)  # 1번 컴퓨터부터 실행
print(cnt)  # 1과 이어진 노드의 갯수 출력