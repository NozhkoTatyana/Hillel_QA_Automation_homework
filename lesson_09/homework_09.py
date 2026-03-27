"""
Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

1. Значення сторони сторона_а повинно бути більше 0.
2. Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
3. Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
значення кут_б обчислюється автоматично.
4. Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:
    angle_b: int

    def __init__(self, side_a: int, angle_a: int) -> None:
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("Side 'a' must be greater than 0")
        elif name == "angle_a":
            if not (0 <= value <= 180):
                raise ValueError("Angle 'a' must be between 0 and 180")

            super().__setattr__("angle_b", 180 - value)

        elif name == "angle_b":
            raise AttributeError("angle_b is calculated automatically")
        super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"


r1 = Rhombus(6, 23)
#r1.angle_b = 50
print(r1)

