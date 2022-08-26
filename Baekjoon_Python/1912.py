n = int(input())
ls = list(map(int, input().split()))
sum = [ls[0]]
for i in range(len(ls) - 1):
    sum.append(max(sum[i] + ls[i + 1], ls[i + 1]))
print(max(sum))