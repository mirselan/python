"""
# Задание_1
from itertools import count


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        print({'TrafficLight': self.__color})


tl_colors = ['RED', 'YELLOW', 'GREEN']
seconds = 0
col_val = ''
for el in count(0):
    if el > 16:
        break
    else:
        seconds = el
    if seconds == 0:
        col_val = tl_colors[0]
    elif seconds == 8:
        col_val = tl_colors[1]
    elif seconds == 10:
        col_val = tl_colors[2]
    else:
        continue

    result = TrafficLight(col_val)
    result.running()

"""
"""
# Задание_2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def m_road(self):
        m_1_sm = 25
        road_height = 5
        res = self._length * self._width * m_1_sm * road_height
        print(f'Формула подсчета кол-ва асфальта: {self._length}м. '
              f'* {self._width}м. * {m_1_sm}кг. * {road_height}см. '
              f'= {res}т.')
        print(f"Асфальта необходимо: {res}т.")


work = Road(20, 5000)
work.m_road()

"""
"""
# Задание_3


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя и должность: {self.position} - {self.name} {self.surname}.")

    def get_total_income(self):
        res = self._income.get("wage") + self._income.get("bonus")
        print(f"Доход с премией: {res}$.")


worker_data = Position('Иван', 'Петров', 'Клерк', 20000, 5000)
worker_data.get_full_name()
worker_data.get_total_income()

"""
"""
# Задание_4


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police == True:
            print(f"Полицейский {self.color} автомобиль {self.name} поехал.")
        else:
            print(f"{self.color} автомобиль {self.name} поехал.")

    def stop(self):
        if self.is_police == True:
            print(f"Полицейский {self.color} автомобиль {self.name} остановился.")
        else:
            print(f"{self.color} автомобиль {self.name} остановился.")

    def turn_direction(self):
        if self.is_police == True:
            print(f"Полицейский {self.color} автомобиль {self.name} повернул.")
        else:
            print(f"{self.color} автомобиль {self.name} повернул.")

    def show_speed(self):
        if self.is_police == True:
            print(f"Полицейский автомобиль едет со скоростью: {self.speed} км/ч.")
        else:
            print(f"Автомобиль едет со скоростью: {self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Внимание!!! TownCar {self.name} едет с превышением скорости!!!.")
        else:
            print(f"TownCar {self.name} едет со скоростью: {self.speed} км/ч.")


class SportCar(Car):
    def noise(self):
        print(f"{self.color} SportCar {self.name} громко газует!!!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Внимание!!! WorkCar {self.name} едет с превышением скорости!!!.")
        else:
            print(f"WorkCar {self.name} едет со скоростью: {self.speed} км/ч.")


class PoliceCar(Car):
    def alarm(self):
        print(f"{self.color} полицейский автомобиль {self.name} включил сирену!!!")


car_1 = Car(40, "Зеленый", "Жигули")
car_1.go()
car_1.stop()
car_1.turn_direction()
car_1.show_speed()
car_2 = TownCar(90, "Желтый", "Волга",)
car_2.show_speed()
car_3 = SportCar(200, "Красный", "Ferrari",)
car_3.noise()
car_3.show_speed()
car_3.turn_direction()
car_3.stop()
car_4 = WorkCar(30, "Белый", "Reno")
car_4.show_speed()
car_5 = PoliceCar(100, "Белый", "BMW", True)
car_5.alarm()
car_5.go()
car_5.show_speed()
car_5.stop()

"""
"""
# Задание_5


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки.({self.title})")


class Pen(Stationery):
    def draw(self):
        print("Рисуем шариковой ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Рисуем карандашом.")


class Handle(Stationery):
    def draw(self):
        print("Рисуем маркером.")


point_1 = Stationery("Карандаш")
point_1.draw()
point_2 = Pen("pen")
point_2.draw()
point_3 = Pencil("pencil")
point_3.draw()
point_4 = Handle("handle")
point_4.draw()

"""