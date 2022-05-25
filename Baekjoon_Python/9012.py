n = int(input())
for i in range(n):
    cnt = 0
    ls = input()
    for j in ls:
        if j == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
                break
    if cnt == 0:
        print("YES")
    else:
        print("NO")