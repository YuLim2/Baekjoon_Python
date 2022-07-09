n = int(input())
ls = []
for _ in range(n):
    x, y = map(int, input().split())
    ls.append((x, y))

ls.sort(key=lambda x: (x[0], x[1]))
for i in ls:
    print(i[0], i[1])