# Задание_1
'''
var1 = "Добрый день!"
var2 = "Сегодня: "
var3 = int(input("Какое сегодня число?"))
var4 = input("Какой сейчас месяц?")

print(var1)
print(var2, var3, var4)
'''
# Задание_2
'''
time = int(input("Введите время в секундах: "))
sec = time % 60
minute = time // 60
minute_1 = minute % 60
hour = minute // 60

print(f"Ваше время: {hour:02d}: {minute_1:02d}: {sec:02d}")
'''
# Задание_3
'''
num = input("Введите число: ")
num_2 = num * 2
num_3 = num * 3
num_4 = int(num)
num_5 = int(num_2)
num_6 = int(num_3)
final = num_4 + num_5 + num_6
print(f"{num} + {num_2} + {num_3} =", final)
'''
# Задание_4
'''
num = int(input("Введите целое положительное число: "))
num_1 = num // 10  # первая цифра числа меньше 100
num_2 = num % 10  # вторая цифра числа меньше 100
num_3 = num // 100  # первая цифра числа от 100 до 999
num_4 = num % 100
num_5 = num_4 // 10  # вторая цифра числа от 100 до 999
num_6 = num_4 % 10  # третья цифра числа от 100 до 999

while num < 100:
    if num_1 - num_2 > 0:
        print(f"{num_1} - Это самая большая цифра в вашем числе!")
        break
    else:
        print(f"{num_2} - Это самая большая цифра в вашем числе!")
        break

while 100 < num < 1000:
    if num_3 - num_5 > 0 and num_3 - num_6 > 0:
        print(f"{num_3} - Это самая большая цифра в вашем числе!")
        break
    if num_3 - num_5 > 0 and num_3 - num_6 < 0:
        print(f"{num_6} - Это самая большая цифра в вашем числе!")
        break
    if num_3 - num_5 < 0 and num_3 - num_6 > 0:
        print(f"{num_5} - Это самая большая цифра в вашем числе!")
        break
    if num_3 - num_5 < 0 and num_3 - num_6 < 0:
        print(f"{num_6} - Это самая большая цифра в вашем числе!")
        break
'''
# Задание_5
'''
income = int(input("Какая выручка в вашей фирме(в рублях)? "))
outcome = int(input("Какие издержки в вашей фирме(в рублях)? "))
result = income - outcome
rent = (result / income) * 100

if result > 0:
    print(f"Ваша фирма отработала с прибылью: {result} руб.")
    print(f"Рентабельность вашей фирмы: {rent} %.")
    people = int(input("Сколько сотрудников в вашей компании? "))
    result_2 = result / people
    print(f"Прибыль на одного сотрудника составила: {result_2} руб.")
else:
    print(f"Ваша фирма отработала с убытком: {result} руб.")
'''
# Задание_6
'''
first = int(input("Сколько км. спортсмен пробежал в 1-й день тренировок? "))
last = int(input("Сколько км. нужно пробежать в последний день тренировок? "))
count = 1

while first < last:
    count += 1
    first = first + (first * 0.1)

print(f"На {count}-й день спортсмен достиг результата — не менее {last} км.")

'''