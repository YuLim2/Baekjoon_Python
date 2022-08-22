n = int(input())

ls = []
for i in str(n):
    ls.append(int(i))

ls.sort(reverse=True)

print(*ls, sep='')