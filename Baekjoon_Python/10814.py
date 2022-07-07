n = int(input())
ls = []

for i in range(n):
    age, name = map(str, input().split())
    ls.append((int(age), name))

ls.sort(key = lambda x : x[0])

for i in ls:
    print(i[0], i[1])