word = input()
alpha = list(range(97,123))  # 아스키코드 숫자 범위

for i in alpha:
    print(word.find(chr(i))) 