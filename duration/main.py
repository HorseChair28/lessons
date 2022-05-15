input_duration = input('Введите длительность в секундах: ')
duration=int(input_duration)
duration_days = duration//86400
duration_hours = duration//3600
duration_mins = duration//60
duration_sec = duration%60
if 1<=duration<60:
    print(duration_sec,"сек")
if 61<=duration<3600:
    print(duration_mins,"мин",duration_sec,"сек")
if 3601<=duration<24:
    print(duration_hours, "часов",duration_mins, "мин", duration_sec, "сек")














    #print(duration_hours, "часов", duration_mins,"минут",duration_sec,"секунд")