h, m = map(int, input().split())
if m < 45:
    m = 15+m
    if h < 1:
        h = 23
    else:
        h = h-1
else:
    m = m-45
print(h, m)
