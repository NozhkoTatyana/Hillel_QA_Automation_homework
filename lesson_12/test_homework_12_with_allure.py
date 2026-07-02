import pytest
import io
from contextlib import redirect_stdout
import allure
from lesson_12.funcs_homework import *


@allure.title("Перевірка вилучення рядків зі змішаного списку")
@pytest.mark.parametrize("data,expected", [
    (['1', 2, 'abc', True, None, 'xyz'], ['1', 'abc', 'xyz']),
    ([], []),
    ([1, 2, 3, False], [])
])
def test_extract_strings(data,expected):
    with allure.step(f"Викликати extract_strings з {data}"):
        result = extract_strings(data)
    with allure.step("Перевірити результат"):
        assert result == expected


@allure.title("Сумування чисел")
@pytest.mark.parametrize("data,expected", [
    ("2,3,4,5", 14),
    ("1,2,abc,4", "Не можу це зробити!")
])
def test_sum_numbers(data,expected):
    with allure.step(f"Викликати sum_numbers з '{data}'"):
        result = sum_numbers(data)
    with allure.step("Перевірити результат"):
        assert result == expected


@allure.title("Перевірка зміни середнього балу")
@pytest.mark.parametrize("new_avg,expected,output", [
    (90, 90, None),
    (120, 75, "Середній бал має бути від 0 до 100. Залишено попереднє значення.")
])
def test_student_change_avg(new_avg,expected,output):
    s = Student("Ivan", "Petrenko", 20, 75)
    buf = io.StringIO()
    with redirect_stdout(buf):
        s.change_avg(new_avg)
    result_output = buf.getvalue().strip() or None
    with allure.step("Перевірити результат"):
        assert s.avg_score == expected
        if output:
            assert result_output == output


@allure.title("Перевірка ромба")
@pytest.mark.parametrize("side,angle,expect_error,expected_str", [
    (10, 60, None, "Rhombus(side_a=10, angle_a=60, angle_b=120)"),
    (0, 60, ValueError, None),
    (10, 200, ValueError, None),
    (10, 45, None, "Rhombus(side_a=10, angle_a=45, angle_b=135)")
])
def test_rhombus(side,angle,expect_error,expected_str):
    if expect_error:
        with pytest.raises(expect_error):
            Rhombus(side_a=side, angle_a=angle)
    else:
        r = Rhombus(side_a=side, angle_a=angle)
        if expected_str:
            assert str(r) == expected_str
