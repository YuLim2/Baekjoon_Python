a = int(input())
zero = [1, 0, 1] # 0, 1, 2에서의 fibo(0) 호출 횟수
one = [0, 1, 1] # 0, 1, 2에서의 fibo(1) 호출 횟수

def fibo(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2]) # fibo(n)의 0호출 횟수 = fibo(n-1)의 0호출 횟수 + fibo(n-2)의 0호출 횟수
            one.append(one[i - 1] + one[i - 2]) # fibo(n)의 1호출 횟수 = fibo(n-1)의 1호출 횟수 + fibo(n-2)의 1호출 횟수
    print("%d %d" % (zero[num], one[num]))


for i in range(a):
    n = int(input())
    fibo(n)