import sys
input = sys.stdin.readline
a, b = map(int, input().split())
c = (100-b)/100 # 방어율 계산
if a*c >= 100: # 조건
    print(0)
else:
    print(1)