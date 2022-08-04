import sys
input = sys.stdin.readline

ls = [int(input()) for _ in range(9)]
sum = sum(ls)

for i in range(9):
    for j in range(i+1, 9):
        if 100 == sum - (ls[i] + ls[j]):
            a, b = ls[i], ls[j]

ls.remove(a)
ls.remove(b)

print(*sorted(ls), sep='\n')