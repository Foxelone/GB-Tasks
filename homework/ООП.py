class Auto:
    # атрибуты класса
    auto_name = "Land Rover"
    auto_model = "Discovery 4"
    auto_year = 2008

    # методы класса
    def on_auto_start(self):
        print(f"Заводим автомобиль")

    def on_auto_stop(self):
        print("Останавливаем работу двигателя")


a = Auto()  # экземпляр класса Auto
print(a)  # содержимое переменной a (класс auto)
print(type(a))  # тип переменной а (Land Rover(автомобиль))
print(a.auto_name)  # доступ к атрибуту класса Auto (в данном случае Имя)
a.on_auto_start()  # запуск метода1 класса Auto (старт)
a.on_auto_stop()  # запуск метода2 класса Auto (стоп)


class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("Автомобиль заведен")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1


a = Auto()
a.on_auto_start("Land Rover", "Discovery 4", 2008)
print(a.auto_name)
print(a.auto_count)

a_2 = Auto()
a_2.on_auto_start("Mazda", "CX 9", 2018)
print(a_2.auto_name)
print(a_2.auto_count)

class Shape:
    def __init__(self, color, param_1, param_2):
        self.color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p


r = Rectangle("white", 10, 20, True)
print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
print(t.color)
print(t.square())
print(t.get_t_p())


class Player:
    def player_method(self):
        print("Родительский метод класса Player")


class Navigator:
    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")

# Класс Transport
class Transport:
    def transport_method(self):
        print("Это родительский метод из класса Transport")


# Класс Auto, наследующий Transport
class Auto(Transport):
    def auto_method(self):
        print("Это метод из дочернего класса")