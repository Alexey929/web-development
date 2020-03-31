stringtest = input()  # for succesful test
n = input()
list = list()
for x in n.split():
    list.append(x)
# print(int(len(list) / 2))
for x in range(int(len(list) / 2)):
    list[x], list[len(list) - x - 1] = list[len(list) - x - 1], list[x]
for x in range(len(list)):
    print(list[x] + ' ', end='')
