list_1=[]
for i in range(1, 101, 2):
    i=i**3
    list_1.append(i)
print(list_1)
print(len(list_1))
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
    j=j+1
    if z%7==0:
        list_2.append(z)
print(list_2)
print(len(list_2))
#
list_3=[]
if i in list_1 and j in list_2:
    True
    list_3.append(i)
