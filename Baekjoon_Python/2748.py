n = int(input())
ls = [i for i in range(n + 1)]
ls[1] = 1 # 배열 세칸으로 메모리제이션

for i in range(2, n + 1):
    ls[i] = ls[i - 1] + ls[i - 2]

print(ls[-1])