"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""


class Student:
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
print(student1.info())

student1.change_avg(88)
print(student1.info())

student1.change_avg(150)
print(student1.info())