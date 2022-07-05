import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))
sls = list(sorted(ls))
cnt = [0]*len(ls)
flag = 0
for i in range(len(ls)):
    if ls[i] == sls[i]:
        cnt[i] = 1

for i in range(len(ls)):
    for j in range(len(ls)):
        if (cnt[i] == 0 and cnt[j] == 0) and i != j:
            if int((ls[i]*ls[j])**(1/2)) == (ls[i]*ls[j])**(1/2):
                flag = 13

if flag == 1:
    print('YES')
else:
    print('NO')