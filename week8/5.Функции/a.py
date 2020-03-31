def minOfFour(a, b, c, d):
    if a < b and a < c and a < d:
        return a
    elif b < c and b < c:
        return b
    elif c < d:
        return c
    else:
        return d

n = input()
list = list()
for x in n.split():
    list.append(x)
print(minOfFour(list[0],list[1],list[2],list[3]))