def extract_strings(lst: list) -> list[str]:
    """
    Формує новий список, який містить лише елементи типу str
    з переданого списку.
    """
    return [item for item in lst if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = extract_strings(lst1)


def sum_numbers(numbers_str):
    """
       Приймає рядок чисел, розділених комами, і повертає їхню суму або повідомлення про помилку.
    """
    try:
        return sum(map(int, numbers_str.split(",")))
    except ValueError:
        return "Не можу це зробити!"

numbers_str = "qwerty1,2,3"
#numbers_str = "1,2,3,4"


class Student:
    """
    Клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
    Метод класу "Студент" change_avg, дозволяє змінювати середній бал студента.
    Метод info --- вивід інформації про студента
    """

    def __init__(self, name: str, surname: str, age: int, avg_score: int = 80):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_score = avg_score

    def change_avg(self, new_score: int) -> None:
        if 0 <= new_score <= 100:
            self.avg_score = new_score
        else:
            print("Середній бал має бути від 0 до 100. Залишено попереднє значення.")

    def info(self) -> str:
        return (f"Студент: {self.name} {self.surname}, "
                f"Вік: {self.age}, "
                f"Середній бал: {self.avg_score}")

student1 = Student("Tetiana", "Nozhko", 30)


class Rhombus:
    """
    1. Значення сторони сторона_а повинно бути більше 0.
    2. Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
    3. Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
    значення кут_б обчислюється автоматично.
    """
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

r1 = Rhombus(6, 100)
#r1.angle_b = 50


if __name__ == '__main__':
    print(lst2)
    print(sum_numbers(numbers_str))
    print(student1.info())
    print(r1)