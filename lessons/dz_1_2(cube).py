list_1 = []
for i in range(1, 1000, 2):
    i = i ** 3
    list_1.append(i)
list_2 = []
list_3 = []
for j in list_1:
    a = j % 10
    b = j // 10 % 10
    c = j // 10 // 10 % 10
    d = j // 10 // 10 // 10 % 10
    e = j // 10 // 10 // 10 // 10 % 10
    f = j // 10 // 10 // 10 // 10 // 10 % 10
    g = j // 10 // 10 // 10 // 10 // 10 // 10 % 10
    z = a + b + c + d + e + f + g
    if z % 7 == 0:
        list_2.append(j)
for j in list_1:
    k = j + 17
    ax = k % 10
    bx = k // 10 % 10
    cx = k // 10 // 10 % 10
    dx = k // 10 // 10 // 10 % 10
    ex = k // 10 // 10 // 10 // 10 % 10
    fx = k // 10 // 10 // 10 // 10 // 10 % 10
    gx = k // 10 // 10 // 10 // 10 // 10 // 10 % 10
    zx = ax + bx + cx + dx + ex + fx + gx
    if zx % 7 == 0:
        list_3.append(k)
print("Элементов в списке:", len(list_1))
# print(list_1)
print("Сумма элементов, чья сумма цифр делится на 7:", sum(list_2), "и таких элементов", len(list_2))
print("Сумма элементов, чья сумма цифр делится на 7 при добавлении 17:", sum(list_3), "и таких элементов", len(list_3))
#17485588610
#15392908808
