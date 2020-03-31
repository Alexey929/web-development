string1 = input()  # чтобы проходило тест
n = input()
list = list()
numberOfRequiredElemets = 0
for x in n.split():
    list.append(int(x))
for x in range(len(list)):
    if x!=0:
        if list[x]>list[x-1]:
            numberOfRequiredElemets += 1
print(numberOfRequiredElemets)

