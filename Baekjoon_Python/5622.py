dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
tm = 0
for i in range(len(word)):
    for j in range(len(dial)):
        if word[i] in dial[j]:
            tm += j+3
print(tm)