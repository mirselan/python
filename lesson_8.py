"""
# Задание_1
import datetime


class Date:
    date = 0
    month = 0
    year = 0

    def __init__(self, text) -> None:
        text = text.split("-")
        try:
            Date.date = int(text[0])
            Date.month = int(text[1])
            Date.year = int(text[2])
        except:
            print("Ошибка: дата введена не в формате «день-месяц-год».")

    def __str__(self) -> str:
        try:
            return Date.date_text().strftime("%d:%m:%Y")
        except:
            return f''

    @staticmethod
    def validating_number(date, month, year) -> datetime:
        try:
            date = datetime.date(year, month, date)
            return date
        except ValueError as err:
            print(f"Ошибка: {err}")

    @classmethod
    def date_text(cls):
        return Date.validating_number(cls.date, cls.month, cls.year)


date_run = Date("10-1-2021")
print(date_run)
date_run_1 = Date("56-2-2021")
print(date_run_1)
date_run_2 = Date("15-17-2021")
print(date_run_2)
date_run_3 = Date("17-3-0")
print(date_run_3)
date_run_4 = Date("18: 1: 0")
print(date_run_4)

"""
"""
# Задание_2


class Zerodivision(Exception):

    @staticmethod
    def division(div_1, div_2) -> float:
        try:
            return div_1/div_2
        except Exception as err:
            return f"Ошибка: {err}"


namb = [[4.5, 5], [150, 25.3], [6, 0], ["4.5", 2], [10, "5"], [25, 5]]
for i in namb:
    print(f"{i[0]} / {i[1]} = {Zerodivision.division(i[0],i[1])}")

"""
"""
# Задание_3


class Exception_1(Exception):

    @staticmethod
    def checking_number_type(namb):
        try:
            return float(namb)
        except:
            print("Ошибка: введенный символ не является числом!!!")


namb_list = []
while True:
    namb = input("Введите число или stop для окончания ввода:  ")
    if namb == "stop": break
    namb = Exception_1.checking_number_type(namb)
    if namb != None:
        namb_list.append(namb)
print(namb_list)

"""
"""
# Задание_4, 5, 6
from prettytable import PrettyTable


class OfficeEquipment:

    def __init__(self, types, company, year, state, location) -> None:
        self.equipment = {"Тип": types,
                          "Фирма производитель": company,
                          "Год выпуска": year,
                          "Состояние": state,
                          "Место хранения": location
                          }

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"], self.equipment["Фирма производитель"],
                       self.equipment["Год выпуска"], self.equipment["Состояние"],
                       self.equipment["Место хранения"]]
                      )
        return table.get_string()

    def __getitem__(self, key):
        return self.equipment.get(key)

    def keys(self):
        return list(self.equipment.keys())


class Printer(OfficeEquipment):

    def __init__(self, types, company, year, state, location, print_speed) -> None:
        super().__init__(types, company, year, state, location)
        self.equipment["Скорость печати ст/мин"] = print_speed

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"], self.equipment["Фирма производитель"],
                       self.equipment["Год выпуска"], self.equipment["Состояние"],
                       self.equipment["Место хранения"], self.equipment["Скорость печати ст/мин"]]
                      )
        return table.get_string()

    def __getitem__(self, key):

        return self.equipment.get(key)

    def keys(self):
        return list(self.equipment.keys())


class Scanner(OfficeEquipment):

    def __init__(self, types, company, year, state, location, scanner_size) -> None:
        super().__init__(types, company, year, state, location)
        self.equipment["Скорость сканирования ст/мин"] = scanner_size

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"], self.equipment["Фирма производитель"],
                       self.equipment["Год выпуска"], self.equipment["Состояние"],
                       self.equipment["Место хранения"], self.equipment["Скорость сканирования ст/мин"]]
                      )
        return table.get_string()

    def __getitem__(self, key):
        return self.equipment.get(key)

    def keys(self):
        return list(self.equipment.keys())


class Xerox(OfficeEquipment):

    def __init__(self, types, company, year, state, location, print_speed, scanner_size) -> None:
        super().__init__(types, company, year, state, location)
        self.equipment["Скорость печати ст/мин"] = print_speed
        self.equipment["Скорость сканирования ст/мин"] = scanner_size

    def __str__(self) -> str:
        table = PrettyTable()
        table.field_names = self.equipment.keys()
        table.add_row([self.equipment["Тип"], self.equipment["Фирма производитель"],
                       self.equipment["Год выпуска"], self.equipment["Состояние"],
                       self.equipment["Место хранения"], self.equipment["Скорость печати ст/мин"],
                       self.equipment["Скорость сканирования ст/мин"]]
                      )
        return table.get_string()

    def __getitem__(self, key):
        return self.equipment.get(key)

    def keys(self):
        return list(self.equipment.keys())


class WarehouseEquipment:

    def __init__(self) -> None:
        self.warehouse = {"Принтер": [],
                          "Сканер":  [],
                          "Ксерокс": []
                          }

    def set_equipment(self, types, company, year, state, location, print_speed, scanner_size):
        try:
            self.set_validation(types, state, location, print_speed, scanner_size)
            if types == "Принтер":
                self.warehouse["Принтер"].append(Printer(types, company, year, state, location, print_speed))
            elif types == "Сканер":
                self.warehouse["Сканер"].append(Scanner(types, company, year, state, location, scanner_size))
            elif types == "Ксерокс":
                self.warehouse["Ксерокс"].append(Xerox(types, company, year, state, location, print_speed, scanner_size))
        except TypeError as err:
            print(f" Ошибка: {err}")

    def get_equipment(self, types, position):
        try:
            self.get_validation(types, position)
            if types == "Принтер":
                return self.warehouse["Принтер"].pop(position)
            elif types == "Сканер":
                return self.warehouse["Сканер"].pop(position)
            elif types == "Ксерокс":
                return self.warehouse["Ксерокс"].pop(position)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __str__(self) -> str:
        table = PrettyTable()
        table.add_column("Тип", list(self.warehouse.keys()))
        table.add_column("Количество", [len(self.warehouse["Принтер"]), len(self.warehouse["Сканер"]),
                                        len(self.warehouse["Ксерокс"])])
        return f" На складе: \n {table.get_string()}"

    def set_validation(self, types, state, location,print_speed,scanner_size):
        types = types.capitalize()
        if types not in list(self.warehouse.keys()):
            raise TypeError("Вам не на этот склад, это склад Оргтехники")
        types = types.capitalize()
        if state != "Исправен":
            raise TypeError(f" Сначала {types} отнесите в мастерскую")
        if not isinstance(print_speed, int) or not isinstance(scanner_size, int):
            raise TypeError("Скорость печати или сканирования должны выражаться целым числом")
        for i in self.warehouse.values():
            for j in i:
                if j["Место хранения"] == location:
                    raise TypeError("Это место уже занято")

    def get_validation(self, types, position):
        types = types.capitalize()
        if types not in list(self.warehouse.keys()):
            raise TypeError("Вам не на этот склад, это склад Оргтехники")
        if not isinstance(position, int):
            raise TypeError("Позиция должна выражаться целым числом")
        num = 0
        for i in self.warehouse.values():
            num += len(i)
        if position > num:
            raise TypeError("Такой позиции нет на складе")

    def print_product_range(self):
        table = PrettyTable()
        cap = self.warehouse["Ксерокс"][0].keys()
        cap.insert(0, " № ")
        table.field_names = cap
        num = 1
        for i in self.warehouse.values():
            for j in i:
                table.add_row([num, j["Тип"], j["Фирма производитель"], j["Год выпуска"], j["Состояние"],
                             j["Место хранения"], j["Скорость печати ст/мин"], j["Скорость сканирования ст/мин"]])
                num += 1
        print(table)


warehouse = WarehouseEquipment()
print("Принимаем на склад: \n")
warehouse.set_equipment("Принтер", "Samsung", 2020, "Не Исправен", "2-б", 1000, 0)
warehouse.set_equipment("Сканер", "Samsung", 2015, "Исправен", "3-a", 0, 20)
warehouse.set_equipment("Ксерокс", "Xserox", 2021, "Исправен", "5-г", 1500, 35)
warehouse.set_equipment("Принтер", "Samsung", 2020, "Исправен", "1-a", 1000, 0)
warehouse.set_equipment("Сканер", "Samsung", 2015, "Исправен", "2-a", 0, 20)
warehouse.set_equipment("Ксерокс", "Xserox", 2021, "Исправен", "3-г", "1500", 35)
warehouse.set_equipment("Принтер", "Samsung", 2020, "Исправен", "4-б", 1000, 0)
warehouse.set_equipment("Сканер", "Samsung", 2015, "Исправен", "2-a", 0, 20)
warehouse.set_equipment("Ксерокс", "Xserox", 2021, "Исправен", "4-г", 1500, 35)
warehouse.set_equipment("Принтер", "Samsung", 2020, "Исправен", "5-б", 1000, 0)
warehouse.set_equipment("Монитор", "Samsung", 2015, "Исправен", "7-a", 0, 20)
warehouse.set_equipment("Ксерокс", "Xserox", 2021, "Исправен", "1-г", 1500, "35")
print("\n Распечатаем всё что есть: \n")
print(warehouse)
warehouse.print_product_range()
print("\n Передадим в другое подразделение компании: \n")
print(warehouse.get_equipment("Принтер", 0))
print(warehouse.get_equipment("Сканер", 0))
print(warehouse.get_equipment("Ксерокс", 0))
print("\n Распечатаем что осталось: \n")
print(warehouse)
warehouse.print_product_range()

"""
"""
# Задание_7


class ComplexNumber:
    
    def __init__(self, reals, imaginary) -> None:
        try:
            self.reals = float(reals)
            self.imaginary = float(imaginary)
        except ValueError as err:
            print(f" Ошибка: {err}")
            self.reals = 0
            self.imaginary = 0

    def __add__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(self, obj_complex)
            return ComplexNumber(self.reals + obj_complex.reals, self.imaginary + obj_complex.imaginary)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __radd__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex, self)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __sub__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(self, obj_complex)
            return ComplexNumber(self.reals - obj_complex.reals, self.imaginary - obj_complex.imaginary)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __rsub__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex, self)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __mul__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(self, obj_complex)
            a = self.reals*obj_complex.reals - self.imaginary*obj_complex.imaginary
            b = self.reals*obj_complex.imaginary + obj_complex.reals*self.imaginary
            return ComplexNumber(a, b)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __rmul__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex, self)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __truediv__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(self, obj_complex)
            a = (self.reals*obj_complex.reals + obj_complex.imaginary*self.imaginary)/(obj_complex.reals**2 + obj_complex.imaginary**2)
            b = (obj_complex.reals*self.imaginary - self.reals*obj_complex.imaginary)/(obj_complex.reals**2 + obj_complex.imaginary**2)
            return ComplexNumber(a, b)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __rtruediv__(self, obj_complex):
        try:
            ComplexNumber.checking_object_type(obj_complex, self)
        except TypeError as err:
            print(f" Ошибка: {err}")

    def __str__(self) -> str:
        if self.imaginary < 0:
            return f"{self.reals:.02f} - j*{abs(self.imaginary):.02f}"
        return f"{self.reals:.02f} + j*{self.imaginary:.02f}"

    @staticmethod
    def checking_object_type(object_1, object_2):
        if not isinstance(object_2, type(object_1)):
            raise TypeError(f"Тип объекта {type(object_1)} не равен {type(object_2)}")


z1 = ComplexNumber(-2, 6)
z2 = ComplexNumber(5, -9)
print(z1)
print(z2)
print(f"({z1}) + ({z2}) = {z1+z2}")
print(f"({z1}) - ({z2}) = {z1-z2}")
print(f"({z2}) - ({z1}) = {z2-z1}")
print(f"({z1}) * ({z2}) = {z1*z2}")
print(f"({z2}) / ({z1}) = {z2/z1}")
print(f"({z1}) / ({z2}) = {z1/z2}")
z1 = ComplexNumber("-2", 6)
z2 = ComplexNumber(5, "-9")
print(z1)
print(z2)
z4 = ComplexNumber("-2", "y")
print(z4)
z3 = ComplexNumber("f", -9)
print(z3)
print(f"(b) + ({z1}) = {'b'+z1}")
print(f"({z1}) - 1 = {z1-1}")
print(f"({z2}) - 1.5 = {z2-1.5}")
print(f"(b) * ({z1}) = {'b'*z1}")
print(f"2 / ({z2}) = {2/z2}")
print(f"({z1}) / 5.3 = {z1/5.3}")

"""
