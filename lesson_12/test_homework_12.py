from lesson_12.funcs_homework import *
from unittest import TestCase
import io
from contextlib import redirect_stdout



class TestExtractStrings(TestCase):
    def test_mixed_types(self):
        data = ['1', 2, 'abc', True, None, 'xyz']
        result = extract_strings(data)
        expected = ['1', 'abc', 'xyz']
        assert result == expected, f"Expected {expected}, but got {result}"

    def test_empty_and_no_strings(self):
        assert extract_strings([]) == [], "Empty list should return empty list"
        assert extract_strings([1, 2, 3, False]) == [], "List without strings should return empty list"


class TestSumNumbers(TestCase):
    def test_valid_numbers(self):
        data = "2,3,4,5"
        result = sum_numbers(data)
        expected = 14
        assert result == expected, f"Expected {expected}, but got {result}"

    def test_invalid_input(self):
        data = "1,2,abc,4"
        result = sum_numbers(data)
        expected = "Не можу це зробити!"
        assert result == expected, f"Expected '{expected}', but got {result}"


class TestStudent(TestCase):
    def test_change_avg_valid(self):
        s = Student("Ivan", "Petrenko", 20, 75)
        s.change_avg(90)
        assert s.avg_score == 90, f"Expected avg_score=90, got {s.avg_score}"

    def test_change_avg_invalid(self):
        s = Student("Ivan", "Petrenko", 20, 75)
        buf = io.StringIO()
        with redirect_stdout(buf):
            s.change_avg(120)
        output = buf.getvalue().strip()
        assert s.avg_score == 75, f"Expected avg_score unchanged=75, got {s.avg_score}"
        assert output == "Середній бал має бути від 0 до 100. Залишено попереднє значення.",\
            f"Expected warning message, got '{output}'"

    def test_info_output(self):
        s = Student("Ivan", "Petrenko", 20, 85)
        result = s.info()
        expected = "Студент: Ivan Petrenko, Вік: 20, Середній бал: 85"
        assert result == expected, f"Expected '{expected}', got '{result}'"


class TestRhombus(TestCase):
    def test_valid_rhombus(self):
        r = Rhombus(side_a=10, angle_a=60)
        assert r.side_a == 10
        assert r.angle_a == 60
        assert r.angle_b == 120

    def test_invalid_side(self):
        with self.assertRaises(ValueError) as context:
            Rhombus(side_a=0, angle_a=60)
        self.assertEqual(str(context.exception), "Side 'a' must be greater than 0")

    def test_invalid_angle(self):
        with self.assertRaises(ValueError) as context:
            Rhombus(side_a=10, angle_a=200)
        self.assertEqual(str(context.exception), "Angle 'a' must be between 0 and 180")

    def test_angle_b_assignment(self):
        r = Rhombus(side_a=10, angle_a=90)

        with self.assertRaises(AttributeError) as context:
            r.angle_b = 100
        self.assertEqual(str(context.exception), "angle_b is calculated automatically")

    def test_str_output(self):
        r = Rhombus(side_a=10, angle_a=45)
        expected = "Rhombus(side_a=10, angle_a=45, angle_b=135)"
        assert str(r) == expected


