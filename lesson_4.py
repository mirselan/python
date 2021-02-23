"""
# Задание_1
from sys import argv


def income(*args):
    work_h = int(argv[1])  # Выработка в час
    pay_h = int(argv[2])  # Плата за час
    super_pay = int(argv[3])  # Премия
    result = (work_h * pay_h) + super_pay
    return result


print(income(*argv[1:]))

"""
"""
# Задание_2
# 1) Исходный список:
l_0 = [25, 4, 4, 5, 6, 3, 10, 2, 2, 5]
print("Исходный список:")
print(l_0)
# 2) Новый список из элементов исходного списка, значения которых
# больше предыдущего элемента:
answer = [l_0[i+1] for i in range(len(l_0)-1) if l_0[i] < l_0[i+1]]
print("Новый список:")
print(answer)

"""
"""
# Задание_3
l_1 = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(l_1)

"""
"""
# Задание_4
# Исходный список:
l_0 = [1, 1, 1, 2, 2, 3, 5, 10, 10, 555, 10, 1, 5]
print("Исходный список:")
print(l_0)
# Список из элементов исходного списка, не имеющих повторений:
l_1 = [el for el in l_0 if l_0.count(el) == 1]
print("Результат:")
print(l_1)

"""
"""
# Задание_5
from functools import reduce
l_1 = [el for el in range(100, 1002) if el % 2 == 0]
print("Четные числа от 100 до 1000:")
print(l_1)


def my_func(a, b):
    #  a - предыдущий элемент списка l_1
    #  b - следующий элемент списка l_1
    return a * b


print("Результат произведения всех элементов списка:")
print(reduce(my_func, l_1))

"""
"""
# Задание_6
from itertools import cycle
from itertools import count
l_1 = ["С", "п", "и", "с", "о", "к", "!"]
cnt = 0
for x in cycle(l_1):
    cnt += 1
    if cnt < 15:
        print(x)
    else:
        break
cnt = 8
for x in count(10):
    cnt += 1
    if cnt < 15:
        print(x)
    else:
        break
        
"""
"""
# Задание_7


def fact(n):
    a = 1
    b = 1
    while b <= n:
        a = a * b
        b += 1
        yield a
        
        
for el in fact(4):
    print(el)
    
"""