string1 = input()  # чтобы проходило тест
n = input()
list = [int(x) for x in n.split()]
for x in range(len(list)):
    if list[x] % 2 == 0:
        print(str(list[x]) + ' ', end='')
