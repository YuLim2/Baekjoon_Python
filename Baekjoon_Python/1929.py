m, n = map(int, input().split())
arr=[]

for i in range(m, n+1):
    if i==1:
        pass
    elif i==2:
        print(i)
    else:
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
               print(i)