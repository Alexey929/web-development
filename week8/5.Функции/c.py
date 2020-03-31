def myXor(x,y):
    if x==y:
        return 0
    else:
        return 1
n = input()
print(myXor(n.split()[0],n.split()[1]))