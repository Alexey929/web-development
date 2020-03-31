string1 = input()  # чтобы проходило тест
n = input()
list = list()
numberOfPositiveElemets = 0
for x in n.split():
    list.append(int(x))
for x in range(len(list)):
    if list[x]>0:
        numberOfPositiveElemets += 1
print(numberOfPositiveElemets)

