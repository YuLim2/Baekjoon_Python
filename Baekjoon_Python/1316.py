n = int(input())
cnt = n
for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]: # j 이후에 중복 글자 존재 유무
            cnt -= 1
            break
print(cnt)