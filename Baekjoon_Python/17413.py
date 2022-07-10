ls = list(input())
cnt = [0]*len(ls) + [1]
open, c = 0, 0
max, min = 0, 100000
for i in range(len(ls)):
    if ls[i] == '<':
        open = 1
    elif ls[i] == '>':
        open = 0
        cnt[i] = 1
    elif ls[i] == ' ':
        cnt[i] = 1
    if open == 1:
        cnt[i] = 1

i=0
j=0
while i < len(ls):
    while j < len(ls):
        if cnt[i] == 0:
            if cnt[j] == 0 and cnt[j+1] == 1:
                print(i, j+1)
                if max < j+1: max = j+1
                if min > i: min = i
                i = j+1
                j = j+2
        j += 2
    print(ls[min:max])
    print(min, max)
    i += 1
