# Объектно-ориентированное программирование (ООП) – это парадигма программирования, в которой основными элементами являются объекты. В Python ООП реализуется с помощью классов и объектов. Рассмотрим основные концепции ООП на примерах на языке Python.

# 1. Класс и его составляющие:
# Класс – это шаблон для создания объектов. Он содержит атрибуты (данные) и методы (функции). Например, класс "Автомобиль" может иметь атрибуты "марка", "модель", "цвет" и методы "запустить двигатель", "ускориться", "затормозить".

# Пример класса "Автомобиль" на Python:
class Automobile:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def start_engine(self):
        print(f"Запускаю двигатель {self.make} {self.model}.")
    
    def accelerate(self):
        print(f"{self.make} {self.model} ускоряется.")
    
    def brake(self):
        print(f"{self.make} {self.model} тормозит.")


# 2. Полиморфизм:
# Полиморфизм позволяет объектам разных классов использовать одни и те же методы, но с различной реализацией. Например, разные классы "Автомобиль", "Мотоцикл" и "Велосипед" могут иметь метод "ускориться", но с разной логикой внутри.

# Пример полиморфизма:
class Motorcycle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def accelerate(self):
        print(f"{self.make} {self.model} ускоряется быстрее.")

class Bicycle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def accelerate(self):
        print(f"{self.make} {self.model} ускоряется медленнее.")

automobile = Automobile("Toyota", "Camry", "Белый")
motorcycle = Motorcycle("Honda", "CBR600RR", "Красный")
bicycle = Bicycle("Schwinn", "Varsity", "Зелёный")

automobile.accelerate()  # "Toyota Camry ускоряется."
motorcycle.accelerate()  # "Honda CBR600RR ускоряется быстрее."
bicycle.accelerate()     # "Schwinn Varsity ускоряется медленнее."


# 3. Наследование:
# Наследование позволяет создавать новые классы, основанные на существующих. Дочерний класс наследует атрибуты и методы родительского класса.

# Пример наследования:
class ElectricCar(Automobile):
    def __init__(self, make, model, color, battery_capacity):
        super().__init__(make, model, color)
        self.battery_capacity = battery_capacity
    
    def charge_battery(self):
        print(f"Заряжаю аккумулятор {self.battery_capacity} кВт-ч в {self.make} {self.model}.")

electric_car = ElectricCar("Tesla", "Model S", "Чёрный", 100)
electric_car.start_engine()  # "Запускаю двигатель Tesla Model S."
electric_car.charge_battery()  # "Заряжаю аккумулятор 100 кВт-ч в Tesla Model S."


# 4. Инкапсуляция:
# Инкапсуляция – это механизм, который позволяет скрывать внутреннюю реализацию объекта от пользователя. В Python это реализуется с помощью методов доступа (геттеры и сеттеры).

# Пример инкапсуляции:
class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance
    
    def get_owner(self):
        return self.__owner
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount
        print(f"Внесено {amount} руб. Баланс: {self.__balance} руб.")
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Снято {amount} руб. Баланс: {self.__balance} руб.")
        else:
            print("Недостаточно средств.")

account = BankAccount("Иван Иванов", 1000)
print(account.get_owner())  # "Иван Иванов"
print(account.get_balance())  # 1000
account.deposit(500)  # Внесено 500 руб. Баланс: 1500 руб.
account.withdraw(2000)  # Недостаточно средств.
account.withdraw(800)  # Снято 800 руб. Баланс: 700 руб.


# В этом примере атрибуты __owner и __balance инкапсулированы (помечены)