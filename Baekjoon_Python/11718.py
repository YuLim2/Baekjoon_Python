while True :
    try :
        print(input())
    except EOFError: # 입출력 오류
        break