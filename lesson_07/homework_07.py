# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(0)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
# 3x6=18
# 3x7=21
# 3x8=24


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(num_1, num_2):
    return num_1 + num_2
num1 = 5
num2 = 8
print(f'Сума чисел {num1} i {num2} становить {sum_numbers(num1, num2)}')


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_numbers(list_numbers):
    if not isinstance(list_numbers, list):
        return "Аргумент має бути списком чисел"
    res_average = sum(list_numbers) / len(list_numbers)
    return res_average

numbers = [5, 2, 3, 10]
result = average_numbers(numbers)
print(f'Середнє значення списку {numbers} становить {result}')


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_line(str_line):
    return str_line[::-1]
print(reverse_line("Hello, world!"))


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    if not isinstance(words, list):
        return "Аргумент має бути списком слів"
    if not words:
        return None
    return max(words, key=len)

words_list = ["сонце", "дерево", "комп'ютер", "енциклопедія", "кіт"]
print(f"Найдовше слово у списку: {longest_word(words_list)}")


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        return  str1.find(str2)
    return -1

str1 = "Hello, world!"
str2 = "world"
pos = find_substring(str1, str2)
print(f"Індекс входження: {pos}")  # 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
pos = find_substring(str1, str2)
print(f"Індекс входження: {pos}")  # -1


# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


def ask_word_with_h() -> None:
    """
    Функція просить користувача ввести слово, яке містить літеру 'h' або 'H'.
    Цикл повторюється, доки користувач не введе правильне слово.
    """
    while True:
        word: str = input("Введіть слово з літерою 'h/H': ")
        if "h" in word.lower():
            print("Дякую, слово підходить!")
            break
        else:
            print("У слові немає 'h/H'. Спробуйте ще раз.")

ask_word_with_h()


def extract_strings(lst: list) -> list[str]:
    """
    Формує новий список, який містить лише елементи типу str
    з переданого списку.
    """
    return [item for item in lst if isinstance(item, str)]

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = extract_strings(lst1)
print(lst2)


def sum_even_numbers(numbers: list[int]) -> int:
    """
    Обчислює суму всіх парних чисел у списку.
    """
    return sum(num for num in numbers if num % 2 == 0)

numbers_list = [1, 5, 6, 89, 41, 3, 42, 2, 4]
sum_of_even_numbers = sum_even_numbers(numbers_list)
print(f"Сума парних чисел становить: {sum_of_even_numbers}")


def check_age_condition(people_records: list[list], indexes: list[int]) -> bool:
  """
  Перевіряє, чи всі люди у списку `people_records` за заданими індексами
  мають вік 30 років або більше.
  """
  return all(people_records[i][2] >= 30 for i in indexes)

indexes_to_check = [2, 3, 0]
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
]
condition = check_age_condition(people_records, indexes_to_check)
print("Усі мають вік >=30:", condition)