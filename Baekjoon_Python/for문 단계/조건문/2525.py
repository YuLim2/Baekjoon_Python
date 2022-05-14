hour, mint = map(int, input().split())
time = int(input())
mint = mint + time
hour = hour + mint//60
print(hour%24, mint%60)