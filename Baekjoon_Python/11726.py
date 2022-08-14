# 피보나치수열처럼 점화식 설정
ls = [0, 1, 2]
for i in range(3, 1001):
  ls.append(ls[i - 2] + ls[i - 1])
n = int(input())
print(ls[n] % 10007)