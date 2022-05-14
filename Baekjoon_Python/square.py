def solution(brown, yellow):
    if yellow == 1:
        if brown == 8:
            return [3, 3]
    for i in range(yellow, 1, -1):
        if(yellow%i != 0):
            x = i
            y = yellow // i
            n = 2*(x+y+2)
            if(n == brown):
                return [x+2, y+2]

solution()