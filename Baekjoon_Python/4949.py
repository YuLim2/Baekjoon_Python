import sys
input = sys.stdin.readline

while True :
    n = input()
    ls = []

    if n == "." :
        break

    for i in n:
        if i == '[' or i == '(':
            ls.append(i)
        elif i == ']':
            if len(ls) != 0 and ls[-1] == '[':
                ls.pop()
            else:
                ls.append(']')
                break
        elif i == ')':
            if len(ls) != 0 and ls[-1] == '(':
                ls.pop()
            else:
                ls.append(')')
                break
    if len(ls) == 0:
        print('yes')
    else:
        print('no')