
x = int(input())
sum = list()  # empty list
for num in range(1, x + 1):
    if x % num == 0:
        sum.append(num)
print(sum)
print(len(sum))
