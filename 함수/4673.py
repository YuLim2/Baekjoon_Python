numbers = set(range(1, 10000))
remove_set = set()
for num in numbers:
    for n in str(num):
        num += int(n)
    remove_set.add(num)

for self_num in sorted(numbers - remove_set):
    print(self_num)