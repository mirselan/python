"""
# Задание_1
list_1 = [[1, 2, 4], [7, 5, 3], [5, 6, 8]]
list_2 = [[8, 1, 9], [6, 7, 9], [4, 8, 6]]


class Matrix:
    def __init__(self, list_new):
        self.list_new = list_new

    def __str__(self):
        return '\n'.join(map(str, self.list_new))

    def __add__(self, other):
        list_3 = []
        for a in range(len(self.list_new)):
            list_3.append([])
            for b in range(len(self.list_new[0])):
                list_3[a].append(self.list_new[a][b] + other.list_new[a][b])
        return '\n'.join(map(str, list_3))


m1 = Matrix(list_1)
m2 = Matrix(list_2)
print(m1, '\n')
print(m2, '\n')
print(m1 + m2)

"""
"""
# Задание_2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def cost(self):
        ...

    def __add__(self, other):
        return self.cost + other.cost


class Coat(Clothes):

    @property
    def cost(self):
        return round(self.param / 6.5) + 0.5


class Suit(Clothes):

    @property
    def cost(self):
        return (2 * self.param + 0.3) / 100


coat = Coat(41)
suit = Suit(180)
print(coat + suit)

"""
"""
# Задание_3 


def cheek(fun):
    def cheek_obj(*args, **kwargs):
        if not isinstance(args[1], type(args[0])):
            raise TypeError(f'В функцию передан объект не типа {type(args[0])}')
        return fun(*args, **kwargs)
    return cheek_obj


class OrganicCell:
    volume = 5  # Ячеек в ряду

    def __init__(self, number: int):
        self.number = number

    def __str__(self) -> str:
        i = self.number // self.volume
        j = self.number % self.volume
        lists = [*['*' * self.volume for _ in range(i)], '*' * j]
        return '\n'.join(lists)

    @cheek
    def __add__(self, obj: object) -> object:
        return OrganicCell(self.number + obj.number)

    @cheek
    def __sub__(self, obj) -> object:
        if self.number < obj.number:
            raise AssertionError("Разность количества ячеек двух клеток меньше нуля")
        return OrganicCell(self.number - obj.number)

    @cheek
    def __mul__(self, obj) -> object:
        return OrganicCell(self.number * obj.number)

    @cheek
    def __truediv__(self, obj) -> object:
        if not obj.number:
            raise ZeroDivisionError("Клетка-делитель пуста")
        return OrganicCell(self.number // obj.number)

    def make_order(self, volume: int) -> str:
        self.volume = volume
        print(self.__str__())


a = OrganicCell(12)
b = OrganicCell(5)
try:
    print(f"Сумма:\n{a + b}")
    print(f"Разность:\n{a - b}")
    print(f"Умножение:\n{a * b}")
    print(f"Деление:\n{a / b}")
    print(f"Замена количества ячеек в ряду:")
    a.make_order(10)
    print(f"Замена количества ячеек в ряду:")
    b.make_order(10)
    print(f"Замена количества ячеек в ряду:")
    (a * b).make_order(10)
except Exception as err:
    print(f'Ошибка: {err}')

"""