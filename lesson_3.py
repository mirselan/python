"""
# Задание_1
while True:


    def my_func():
        try:
            var_1 = float(input("Введите первое число: "))
            var_2 = float(input("Введите второе число: "))
            result = var_1 / var_2
        except ZeroDivisionError:
            return "Второе число не должно быть равно нулю!"
        return result


    print(f"Результат: {my_func()}")

"""
"""
# Задание_2


def user_data(var_1, var_2, var_3, var_4, var_5, var_6):
    print(" ")
    print("ДАННЫЕ ПОЛЬЗОВАТЕЛЯ: ")
    print(f"Имя: {var_1}, Фамилия: {var_2}, Год рождения: {var_3}, "
          f"Город проживания: {var_4}, Email: {var_5}, Телефон: {var_6}")


user_data(
    var_1=input("Ваше имя: "),
    var_2=input("Ваша фамилия: "),
    var_3=input("Год рождения: "),
    var_4=input("Город проживания: "),
    var_5=input("Email: "),
    var_6=input("Телефон: ")
)

"""
"""
# Задание_3


def my_func(var_1, var_2, var_3):
    minimum = min(var_1, var_2, var_3)
    result_1 = var_1 + var_2 + var_3
    result_2 = result_1 - minimum
    return result_2


print(my_func(6, 3, 9))

"""
"""
# Задание_4(c **)


def my_func(x, y):
    if x > 0 > y and int(y) == float(y):
        var_1 = x ** y
        return var_1
    else:
        return "'x' - должен быть действительным положительным числом, а 'y' - целым отрицательным числом!"


print(my_func(3, -2))

"""
"""
# Задание_4(без **)


def my_func(x, y):
    if x > 0 > y and int(y) == float(y):
        x_1 = x
        while y < -1:
            x_1 = x_1 * x
            y += 1
        return 1 / x_1
    else:
        return "'x' - должен быть действительным положительным числом, а 'y' - целым отрицательным числом!"


print(my_func(8, -3))

"""
"""
# Задание_5(Как выходить из программы после появления спецсимвола так и не разобрался...)
el_2 = 0
while True:
    var_1 = input("Ведите числа через пробел: ")
    var_2 = var_1.split()
    for i in var_2:
        try:
            el = int(i)
            el_2 = el_2 + el
        except ValueError:
            print("Пишите только цифры!")

    print(el_2)
    
    """
"""
# Задание_6


def int_func():
    var_1 = input("Ведите слово или предложение из маленьких латинских букв: ")
    var_2 = var_1.title()
    return var_2


print(int_func())

"""