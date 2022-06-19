def jump(ls, x, y):
    if x >= n: return False
    if y >= n: return False
    if x == n-1 and y == n-1: return True
    res = record[x][y]
    if res != -1: return  res
    move = ls[x][y]
    res = max(res, jump(ls, x+move, y))
    res = max(res, jump(ls, x, y+move))
    record[x][y] = res
    return res

c = int(input())
for i in range(c):
    n = int(input())
    ls = []
    record = [[-1 for k in range(n)] for l in range(n)]
    for j in range(n):
        ls.append(list(map(int, input().split())))
    if jump(ls, 0, 0):
        print("YES")
    else:
        print("NO")