"""
Завдання 1

Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer,
які успадковуються від Employee. Клас Manager повинен мати додатковий атрибут department,
а клас Developer - атрибут programming_language.

Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer.
Цей клас представляє керівника з команди розробників. Клас TeamLead повинен мати всі атрибути
як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість
розробників у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
"""
from decimal import Decimal


class Employee:
    def __init__(self, name: str , salary: Decimal) -> None:
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, salary: Decimal, department: str) -> None:
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name: str, salary: Decimal, programming_language: str) -> None:
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name: str,
                 salary: Decimal,
                 department: str,
                 programming_language: str,
                 team_size: int) -> None:
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


def check_test_teamlead_attrs(teamlead: tuple, expected_attrs: list) -> None:
    attrs = [attr for attr in dir(teamlead) if not attr.startswith("__")]

    for attr in expected_attrs:
        if attr in attrs:
            print(f"✅ TeamLead має атрибут '{attr}'")
        else:
            print(f"❌ TeamLead НЕ має атрибут '{attr}'")


teamlead = TeamLead("Nika", Decimal("1000"), "IT","Python", 5)
expected_attrs = ["department", "programming_language", "bonus"]
#expected_attrs = ["name", "salary", "department", "programming_language", "team_size"]
check_test_teamlead_attrs(teamlead, expected_attrs)



