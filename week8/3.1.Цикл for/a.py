a = int(input())
b = int(input())
i = a
for num in range(a, b + 1):
    if num % 2 == 0:
        print(str(num) + ' ', end='')
