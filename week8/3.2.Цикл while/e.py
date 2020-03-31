n = int(input())
result = 1
power = 0
while result <= n * n:
    if result >= n:
        print(power)
        break
    result *= 2
    power += 1