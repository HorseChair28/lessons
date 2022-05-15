duration=int(input("Введите время в секундах: "))

days=duration // 86400

# hours = duration // 3600
hours=(duration - days * 86400) // 3600

minutes=(duration - hours * 3600) // 60

seconds=duration - (hours * 3600 + minutes * 60)

print(days, "дней", hours, "час", minutes, "мин", seconds, "сек")
