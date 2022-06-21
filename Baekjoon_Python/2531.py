import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rsplit())
ls = [int(input().rstrip()) for _ in range(n)]
lp, rp = 0, 0
answer = 0

while lp != n:
    rp = lp + k
    case = set()
    addable = True
    for i in range(lp, rp):
        i %= n
        case.add(ls[i])
        if ls[i] == c: addable = False

    cnt = len(case)
    if addable: cnt += 1
    answer = max(answer, cnt)
    lp += 1

print(answer)