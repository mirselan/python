time = int(input("Введите время в секундах: "))
sec = time % 60
minute = time // 60
minute_1 = minute % 60
hour = minute // 60

print(f"Ваше время: {hour:02d}: {minute_1:02d}: {sec:02d}")
