list_1=[]
for i in range(1, 50, 2):
    i=i**3
    list_1.append(i)
# print(list_1)
list_2=[]
for j in list_1:
    a=j%10
    b=j//10%10
    c=j//10//10%10
    d=j//10//10//10%10
    e=j//10//10//10//10%10
    f=j//10//10//10//10//10%10
    g=j//10//10//10//10//10//10%10
    z=a+b+c+d+e+f+g
    if z%7==0:
        list_2.append(j)
print("Элементов в списке:", len(list_1))
print("Сумма элементов, чья сумма цифр делится на 7:", sum(list_2))
list_3=[]
for i in list_1:
    x = i + 17
    list_3.append(x)
    for j in list_3:
        h=j%10
        v=j//10%10
        k=j//10//10%10
        l=j//10//10//10%10
        m=j//10//10//10//10%10
        n=j//10//10//10//10//10%10
        o=j//10//10//10//10//10//10%10
        y=h+v+k+l+m+n+o
    if y%7==0:
        list_3.append(y)
print(list_3)



