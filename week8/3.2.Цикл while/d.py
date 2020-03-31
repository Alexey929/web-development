n = int(input())
power = 1
result = False
while power <= n:
    if power == n:
        result = True
        break
    else:
        result = False
    power *= 2
if result:
    print("YES")
else:
    print("NO")
