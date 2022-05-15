print('Добро пожаловть в онлайн ресепшн нашего медицинского центра.')
print('Пожалуйста заполните нашу медицинскую анкету, чтобы мы могли вам дать оценку вашего состояния.')
name = input('Введите свое имя')
print('Здравстуйте,', name)
print (name)
surname = input('Введите пожалуйста свою фамилию')
print (name+surname)
print('Рады знакмоству Mr.', surname)
print ('Mr.', surname)
age = int(input('Пожалуйста напишите сколько Вам лет'))
print('И последний вопрос Mr.', surname)
weight = int(input('напишите ваш вес'))
if age <= 30:
if weight >= 50 or weight <=120:
print ('Вы в хорошем состояние Mr.', surname)
elif age >= 31 and age < 39:
if weight <50 or weight >120:
print('Вам требуется заняться собой')
if weight > 50 or weight < 120:
print('У вас все в порядке Mr.', surname)
elif age >40:
if weight <50 or weight >120:
print('Вам требуется врачебный осмотр')

print('Благодарим за уделенное время')
print('Теперь мы сможем подобрать для вас специальные предложения от нашего медицинского центра.')
