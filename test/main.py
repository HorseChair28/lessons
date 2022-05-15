print('Соревнования по гундежу')
count: int=int(input('Введите количество участников: '))
i=count
members=[]
while i>0:
    name=input('Кто занял {} место:'.format(i))
    i-=1
    members.append(name)
members.reverse()
print('В соревнованиях учавствовали: ', sorted(members))
result=members[:3]
print('Победители: {}. Поздравляем!'.format(result))
