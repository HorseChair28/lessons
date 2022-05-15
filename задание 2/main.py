while True:
    number = int(input('Введите число: '))
    if 0 < number < 10:
        break
    print('Неправильное число')
print(number ** 2)
