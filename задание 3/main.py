name = (input("Ваше имя?"))
sourname = (input("Ваша фамиялия?"))
age = int(input("Ваш возраст?"))
weight = int(input("Ваш вес?"))
if age <= 30 and weight >= 50 and weight <= 120:
    print(name, sourname, ',', age, "лет", ',', weight, "килограмм - Ваше состояние хорошее")
elif age >= 30 and weight < 50 or weight > 120:
    print(name, sourname, ',', age, "лет", ',', weight, "килограмм - Вам следует заняться собой")
elif age >= 40 and weight < 50 or weight > 120:
    print(name, sourname, ',', age, "лет", ',', weight, "килограмм - Вам срочно следует обратится к врачу")
elif age >= 50 and weight > 50 or weight < 120:
    print(name, sourname, ',', age, "лет",',', weight, 'килограмм - Вам следует обратится к врачу')