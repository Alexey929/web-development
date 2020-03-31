stringtest = input()  # for succesful test
n = input()
list = list()
count = 0
for x in n.split():
    list.append(int(x))
for x in range(len(list)):
    if x != 0 and x != len(list) - 1:
        if list[x] > list[x - 1] and list[x] > list[x + 1]:
            count += 1
print(count)
