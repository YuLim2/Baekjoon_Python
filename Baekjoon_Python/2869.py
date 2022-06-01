import math
a, b, v = map(int, input().split())

nv = v - a # 규칙을 제외한 날을 제외
day = math.ceil(nv/(a-b)) + 1 # 남은 거리를 이동한 날 + 규칙을 제외한 날
print(day)