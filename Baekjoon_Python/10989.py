import sys
input = sys.stdin.readline
n = int(input())
nums = [0]*10000 # 공간 할당

# 카운트 솔트
for _ in range(n):
    num = int(input())
    nums[num-1] += 1 # 입력 받고 바로 카운트
for i in range(10000):
    if nums[i] != 0:
        for j in range(nums[i]): # 카운팅 된 만큼 출력
            print(i+1)