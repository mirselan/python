# Задание_1
"""
list_1 = ["новый_список", 65, 5.3, True]
x = 0
while x < 4:
    print(type(list_1[x]))
    x += 1

"""
# Задание_2
'''
str_1 = input("Введите любое количество значений любых типов через пробел: ")
list_1 = list(str_1.split())
var_1 = len(list_1)
n = 0
while n < var_1 - 1:
    list_1[0 + n], list_1[1 + n] = list_1[1 + n], list_1[0 + n]
    n += 2
print(list_1)

'''
# Задание_3 Через list
'''
num = int(input("Введите номер месяца: "))
month = ["Это Зима", "Это Весна", "Это Лето", "Это Осень"]
if num < 1 or num > 12:
    num = int(input("Введите номер месяца от 1 до 12: "))
if num < 3 or num > 11:
    print(month[0])
elif 2 < num < 6:
    print(month[1])
elif 5 < num < 9:
    print(month[2])
elif 8 < num < 12:
    print(month[3])

'''
# Задание_3 Через dict
'''
num = int(input("Введите номер месяца: "))
month = {12: "Это Зима", 1: "Это Зима", 2: "Это Зима",
         3: "Это Весна", 4: "Это Весна", 5: "Это Весна",
         6: "Это Лето", 7: "Это Лето", 8: "Это Лето",
         9: "Это Осень", 10: "Это Осень", 11: "Это Осень"}
if num < 1 or num > 12:
    num = int(input("Введите номер месяца от 1 до 12: "))
print(month.get(num))

'''
# Задание_4
'''
str_1 = input("Введите несколько слов через пробел: ")
list_1 = list(str_1.split())
for a, b in enumerate(list_1, 1):
    if len(b) < 10:
        print(a, b)
    else:
        print(a, b[0:10])
'''
# Задание_5
'''
print("Наш рейтинг на сегодня:")
num = [7, 5, 3, 3, 2]
print(num)
while True:
    num_2 = int(input("Введите следующее число в рейтинг: "))
    num.append(num_2)
    num.sort(reverse=True)
    print(num)
'''
# Задание_6
'''
name = input("Введите название товара: ")
price = int(input("Введите цену товара: "))
num = int(input("Введите количество товара: "))
numb = input("Введите еденицу измерения: ")
name_2 = input("Введите название следующего товара: ")
price_2 = int(input("Введите цену товара: "))
num_2 = int(input("Введите количество товара: "))
numb_2 = input("Введите еденицу измерения: ")
name_3 = input("Введите название следующего товара: ")
price_3 = int(input("Введите цену товара: "))
num_3 = int(input("Введите количество товара: "))
numb_3 = input("Введите еденицу измерения: ")
print("ТОВАРЫ:")
list_1 = [(1, {"Название": name, "Цена": price, "Количество": num, "Еденица измерения": numb}),
          (2, {"Название": name_2, "Цена": price_2, "Количество": num_2, "Еденица измерения": numb_2}),
          (3, {"Название": name_3, "Цена": price_3, "Количество": num_3, "Еденица измерения": numb_3})]
for x in list_1:
    print(x)
list_2 = [name, name_2, name_3]
list_2 = list(set(list_2))
list_3 = [price, price_2, price_3]
list_3 = list(set(list_3))
list_4 = [num, num_2, num_3]
list_4 = list(set(list_4))
list_5 = [numb, numb_2, numb_3]
list_5 = list(set(list_5))
print("СТАТИСТИКА ТОВАРОВ:")
statistic = {"Название": list_2,
             "Цена": list_3,
             "Количество": list_4,
             "Еденица измерения": list_5}
for a, b in statistic.items():
    print(a, ":", b)
'''
