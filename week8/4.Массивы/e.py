string1 = input()  # чтобы проходило тест
n = input()
list = list()
result = False
for x in n.split():
    list.append(int(x))
for x in range(len(list)):
    if x != 0:
        if (list[x] > 0 and list[x - 1] > 0) or (list[x] < 0 and list[x - 1] < 0):
            result = True
            break
if result:
    print("YES")
else:
    print("NO")
