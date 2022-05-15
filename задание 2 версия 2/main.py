while True:
    number = int(input('Введите число: '))
    if 0 < number < 10:
        break
    if 0 < number:
        print('Введите число меньше, пожалуйста')
    if 10 > number:
        print('Введите число больше, пожалуйста')
print(number ** 2)
print('Спасибо')
