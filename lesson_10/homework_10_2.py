"""
Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур,
та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

    Трапеція (Trapezoid)
Площа: S = ((a + b) / 2) * h
де a і b — основи, h — висота
Периметр: P = a + b + c + d
  де c і d — бічні сторони

    Прямокутник (Rectangle)
Площа: S = a * b
Периметр: P = 2 * (a + b)

    Прямокутний трикутник (Right Triangle)
Площа: S = (a * b) / 2   (де a і b — катети)
Периметр: P = a + b + √(a^2 + b^2)   (гіпотенуза = √(a^2 + b^2))
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b

    def area(self) -> float:
        return self.__a * self.__b

    def perimeter(self) -> float:
        return 2 * (self.__a + self.__b)


class Trapezoid(Shape):
    def __init__(self, a: float, b: float, c: float, d: float, h: float):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__h = h

    def area(self) -> float:
        return ((self.__a + self.__b) / 2) * self.__h

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c + self.__d


class RightTriangle(Shape):
    def __init__(self, a: float, b: float):
        self.__a = a
        self.__b = b
        self.__c = math.sqrt(self.__a**2 + self.__b**2)

    def area(self) -> float:
        return (self.__a * self.__b) / 2

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c


shapes = [
    Rectangle(4, 6),
    RightTriangle(5,25),
    Trapezoid(7,14, 10, 12, 5)
]

for shape in shapes:
    print(f"{shape.__class__.__name__}: area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")








