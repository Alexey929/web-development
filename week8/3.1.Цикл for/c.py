import math

a = int(input())
b = int(input())
for num in range(a, b + 1):
    if math.sqrt(num) - int(math.sqrt(num)) == 0:
        print(str(num) + ' ', end='')
