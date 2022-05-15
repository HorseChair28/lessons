input_duration = input('Введите длительность в секундах: ')
duration=int(input_duration)
duration_sec = duration%60
duration_mins = duration//60
duration_hours = duration_mins//60
duration_days = duration_hours//24



if 0<=duration<60:
    print(duration_sec,"сек")
if 60<=duration<3600:
    print(duration_mins,"мин",duration_sec,"сек")
if 3600<=duration<86400:
    print(duration_hours, "часов",duration_mins, "мин", duration_sec, "сек")









#print(duration_days, "дней", duration_hours, "часов", duration_mins,"минут",duration_sec,"секунд")