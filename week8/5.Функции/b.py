def myPower(a, b):
    a = float(a)
    b = int(b)
    power = a
    if b==0:
        return 1
    if b==1:
        return a
    for x in range(b-1):
        a *= power
    return a
n = input()
a = n.split()[0]
b = n.split()[1]
print(myPower(a,b))