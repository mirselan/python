"""
# Задание_1
cnt = 0
while cnt < 5:
    m_f = open("my_file.txt", "a", encoding='UTF-8')
    data = input("Введите ваше сообщение: ") + "\n"
    m_f.writelines(data)
    cnt += 1
    m_f.close()

"""
"""
# Задание_2(Так и не понял как бороться с лишними пустыми строками
# которые выводятся принтом(пробовал ставить sep='', но не помогает))
with open("my_file_2.txt", "r", encoding='UTF-8') as f_2:
    a = f_2.readlines()
    for b in enumerate(a, 1,):
        print(b)
    print(f"В этом файле содержится строк: {b[0]}.")

    x = 0
    f_2.seek(0)
    while x < 5:
        c = f_2.readline()
        print(c)
        d = c.split(" ")
        for i in enumerate(d, 1):
            print(i)
        print(f"В этой строке содержится слов: {i[0]}.")
        x += 1
        
"""
"""
# Задание_3
print("Сотрудники, получающие меньше чем 20000: ")
with open("my_file_3.txt", "r", encoding='UTF-8') as f_3:
    x = 0
    y = 0
    while x < 5:
        a = f_3.readline()
        b = a.split(",")
        c = int(b[1])
        if c < 20000:
            print(b[0])  # Выводим фамилии тех, кто получает меньше 20000
        x += 1

        y = c + y  # Считаем общую зарплату
    f_3.seek(0)
    d = f_3.readlines()
    for e in enumerate(d, 1, ):
        j = e[0]  # Считаем число сотрудников
    k = y / j  # Считаем среднюю зарплату
    print(f"Средняя зарплата: {k}")
    
"""
"""
# Задание_4
# Открываем существующий начальный файл:
with open("my_file_4.txt", "r", encoding='UTF-8') as f_4:
    print("Изначальный файл:")
    print(f_4.read())
    f_4.seek(0)
    list_0 = ['Один', 'Два', 'Три', 'Четыре']  # Список подстановок в изначальный файл
    x = 0
    y = 0
    while x < 4:
        a = f_4.readline()
        b = a.split(" — ")
        dict_1 = {list_0[y]: b[1]}
        list_1 = list(dict_1.popitem())
        new_line = " — ".join(list_1)  # Переделанные строки в новый файл
        # Создание нового файла программно:
        with open("my_file_5.txt", "a", encoding='UTF-8') as f_5:
            f_5.write(new_line)
        x += 1  # Отсчет итераций цикла
        y += 1  # Перебор элементов списка "с" по индексу
# Открытие нового файла:
with open("my_file_5.txt", "r", encoding='UTF-8') as f_5:
    print("Новый файл:")
    print(f_5.read())
    
"""
"""
# Задание_5
with open("my_file_6.txt", "a+", encoding='UTF-8') as f_6:
    f_6.write('50 60 80 8 74 30 51 61')
    f_6.seek(0)
    a = f_6.read()
    b = a.split(" ")
    x = 0
    y = 0
    while x < 8:
        y = int(b[x]) + y
        x += 1
    print("Сумма чисел:")
    print(y)
    
"""
"""
# Задание_6
with open("my_file_7.txt", "r", encoding='UTF-8') as f_7:
    x = 0  # Счетчик цикла
    list_2 = []  # Список ключей будущего словаря
    list_3 = []  # Начальный список значений словаря
    list_4 = []  # Список общих количеств занятий по предметам
    dict_res = {}  # Итоговый словарь, выводимый на экран
    while x < 3:
        list_0 = f_7.readline()
        list_1 = list_0.split(":")  # Разделили файл по ":"
        list_2.append(list_1[0])
        list_3.append(list_1[1])
        x += 1
    for i in list_3:
        a = len(i)
        sublist_1 = []
        y = 0  # Счетчик цикла
        while y < a:  # Пока индекс не превышает длинну строки
            str_0 = ''
            z = i[y]
            while '0' <= z <= '9':  # Проверяем, что символ строки это цифра
                str_0 += z
                y += 1
                if y < a:
                    z = i[y]
                else:
                    break
            y += 1
            if str_0 != '':
                sublist_1.append(int(str_0))
        res = sum(sublist_1)
        list_4.append(res)
    e = 0  # Счетчик цикла
    while e < 3:
        dict_res_0 = {list_2[e]: list_4[e]}
        res_1 = dict_res_0
        dict_res.update(res_1)
        e += 1

    print(dict_res)  # Выводим итоговый словарь
    
"""
# Задание_7
"""
import json
with open("my_file_8.txt", "r", encoding='UTF-8') as f_8:
    x = 0  # Счетчик цикла
    list_1 = []  # Список с названиями фирм
    list_2 = []  # Список с прибылями фирм
    while x < 5:
        str_1 = f_8.readline()
        x += 1
        list_0 = str_1.split(" ")
        list_1.append(list_0[0])
        str_2 = list_0[3]  # Получаем последнее слово строки
        list_3 = str_2.split('.')  # Убираем "." и "\n" в конце строк
        list_2.append(int(list_0[2]) - int(list_3[0]))
    y = 0  # Счетчик цикла
    dict_res = {}  # Словарь названий фирм и их доходов
    while y < 5:
        dict_res_0 = {list_1[y]: list_2[y]}
        res_1 = dict_res_0
        dict_res.update(res_1)
        y += 1
    list_4 = [el for el in list_2 if el > 0]  # Список прибылей фирм без убытков
    average = sum(list_4) / len(list_4)
    dict_average = {"average_profit": average}  # Словарь средней прибыли
    res_list = [dict_res, dict_average]
    
with open("my_json.json", "w") as json_obj:
    e = json.dump(res_list, json_obj)
    
"""