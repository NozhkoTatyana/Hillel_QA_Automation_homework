from lesson_12.funcs_homework import *
from unittest import TestCase
import io
from contextlib import redirect_stdout
import allure


class TestExtractStrings(TestCase):

    @allure.title("Перевірка вилучення рядків зі змішаного списку")
    def test_mixed_types(self):

        with allure.step("Створити тестові дані"):
            data = ['1', 2, 'abc', True, None, 'xyz']

        with allure.step("Викликати функцію extract_strings"):
            result = extract_strings(data)

        with allure.step("Перевірити результат"):
            expected = ['1', 'abc', 'xyz']
            assert result == expected

    @allure.title("Перевірка порожнього списку та списку без рядків")
    def test_empty_and_no_strings(self):

        with allure.step("Перевірити порожній список"):
            assert extract_strings([]) == []

        with allure.step("Перевірити список без рядків"):
            assert extract_strings([1, 2, 3, False]) == []



class TestSumNumbers(TestCase):

    @allure.title("Успішне сумування чисел")
    def test_valid_numbers(self):

        with allure.step("Підготувати дані"):
            data = "2,3,4,5"

        with allure.step("Отримати суму"):
            result = sum_numbers(data)

        with allure.step("Перевірити результат"):
            assert result == 14

    @allure.title("Помилка при нечисловому значенні")
    def test_invalid_input(self):

        with allure.step("Підготувати некоректні дані"):
            data = "1,2,abc,4"

        with allure.step("Викликати функцію"):
            result = sum_numbers(data)

        with allure.step("Перевірити повідомлення про помилку"):
            assert result == "Не можу це зробити!"


class TestStudent(TestCase):

    @allure.title("Зміна середнього балу на валідне значення")
    def test_change_avg_valid(self):

        with allure.step("Створити студента"):
            s = Student("Ivan", "Petrenko", 20, 75)

        with allure.step("Змінити середній бал"):
            s.change_avg(90)

        with allure.step("Перевірити нове значення"):
            assert s.avg_score == 90

    @allure.title("Спроба встановити невалідний середній бал")
    def test_change_avg_invalid(self):

        with allure.step("Створити студента"):
            s = Student("Ivan", "Petrenko", 20, 75)

        with allure.step("Виконати зміну з невалідним значенням"):
            buf = io.StringIO()

            with redirect_stdout(buf):
                s.change_avg(120)

            output = buf.getvalue().strip()

        with allure.step("Перевірити, що значення не змінилось"):
            assert s.avg_score == 75

        with allure.step("Перевірити текст повідомлення"):
            assert output == (
                "Середній бал має бути від 0 до 100. "
                "Залишено попереднє значення."
            )

    @allure.title("Перевірка методу info")
    def test_info_output(self):

        with allure.step("Створити студента"):
            s = Student("Ivan", "Petrenko", 20, 85)

        with allure.step("Отримати інформацію про студента"):
            result = s.info()

        with allure.step("Перевірити результат"):
            expected = "Студент: Ivan Petrenko, Вік: 20, Середній бал: 85"
            assert result == expected

class TestRhombus(TestCase):

    @allure.title("Створення валідного ромба")
    def test_valid_rhombus(self):

        with allure.step("Створити ромб"):
            r = Rhombus(side_a=10, angle_a=60)

        with allure.step("Перевірити атрибути"):
            assert r.side_a == 10
            assert r.angle_a == 60
            assert r.angle_b == 120

    @allure.title("Помилка при невалідній стороні")
    def test_invalid_side(self):

        with allure.step("Створити ромб з невалідною стороною"):
            with self.assertRaises(ValueError) as context:
                Rhombus(side_a=0, angle_a=60)

        with allure.step("Перевірити текст помилки"):
            self.assertEqual(
                str(context.exception),
                "Side 'a' must be greater than 0"
            )

    @allure.title("Помилка при невалідному куті")
    def test_invalid_angle(self):

        with allure.step("Створити ромб з невалідним кутом"):
            with self.assertRaises(ValueError) as context:
                Rhombus(side_a=10, angle_a=200)

        with allure.step("Перевірити текст помилки"):
            self.assertEqual(
                str(context.exception),
                "Angle 'a' must be between 0 and 180"
            )

    @allure.title("Перевірка автоматичного обчислення angle_b")
    def test_angle_b_assignment(self):

        with allure.step("Створити ромб"):
            r = Rhombus(side_a=10, angle_a=90)

        with allure.step("Спробувати встановити angle_b вручну"):
            with self.assertRaises(AttributeError) as context:
                r.angle_b = 100

        with allure.step("Перевірити текст помилки"):
            self.assertEqual(
                str(context.exception),
                "angle_b is calculated automatically"
            )

    @allure.title("Перевірка рядкового представлення ромба")
    def test_str_output(self):

        with allure.step("Створити ромб"):
            r = Rhombus(side_a=10, angle_a=45)

        with allure.step("Перевірити результат str()"):
            expected = "Rhombus(side_a=10, angle_a=45, angle_b=135)"
            assert str(r) == expected