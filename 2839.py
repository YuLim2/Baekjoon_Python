n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n//5
        print(cnt)
        break
    n -= 3
    cnt += 1
else: # n이 5의 배수로 떨어지지 않으면서 0 미만일 때
    print(-1)