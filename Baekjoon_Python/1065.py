n = int(input())

num = 0
for i in range(1, n+1):
    ls = list(map(int, str(i)))
    if i < 100:
        num += 1
    elif ls[0]-ls[1] == ls[1]-ls[2]:
        num += 1
print(num)