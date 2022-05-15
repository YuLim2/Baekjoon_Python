a, b = map(int, input().split())
def reverse(r):
    r = (r // 100) + (((r % 100) // 10) * 10) + ((r % 10) * 100)
    return r

a = reverse(a)
b = reverse(b)

if a > b:
    print(a)
else:
    print(b)
