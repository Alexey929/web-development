import math

x = int(input())
i = 1
root = math.sqrt(x)
while i <= root:
    print(str(i * i) + " ", end='')
    i += 1
