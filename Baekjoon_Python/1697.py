from collections import deque

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(ls[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= MAX and not ls[i]:
                ls[i] = ls[x] + 1
                q.append(i)

MAX = 10**5
ls = [0] * (MAX+1)
n, k = map(int, input().split())

bfs()