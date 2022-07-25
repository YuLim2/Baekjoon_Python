from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())
for i in range(n):
    q.append(i+1)

while len(q) != 1:
    q.popleft()
    num = q.popleft()
    q.append(num)

print(q[0])