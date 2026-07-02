import allure
from conftest import logger

@allure.feature("Database connection")
def test_connection(conn):
    with allure.step("Перевірка, що з'єднання існує"):
        assert conn is not None


@allure.feature("Insert student")
def test_insert_student(conn):
    with allure.step("Вставка нового студента"):
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s) RETURNING id;",
            ("Test Student", "test@student.com")
        )
        student_id = cur.fetchone()[0]
        conn.commit()
        logger.info(f"Вставлено студента id={student_id}, name='Test Student', email='test@student.com'")
        assert student_id is not None


@allure.feature("Select students")
def test_select_students(conn):
    with allure.step("Вибірка студентів з таблиці"):
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM students;")
        rows = cur.fetchall()
        logger.info(f"У таблиці students {len(rows)} записів: {rows}")
        assert isinstance(rows, list)


@allure.feature("Update student")
def test_update_student(conn):
    with allure.step("Оновлення імені студента"):
        cur = conn.cursor()
        cur.execute(
            "UPDATE students SET name = %s WHERE email = %s;",
            ("Updated Student", "test@student.com")
        )
        conn.commit()
        logger.info("Оновлено ім’я студента на 'Updated Student'")
    with allure.step("Перевірка, що ім’я оновлено"):
        cur.execute("SELECT name FROM students WHERE email = %s;", ("test@student.com",))
        name = cur.fetchone()[0]
        assert name == "Updated Student"


@allure.feature("Delete student")
def test_delete_student(conn):
    with allure.step("Видалення студента"):
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE email = %s;", ("test@student.com",))
        conn.commit()
        logger.info("Видалено студента з email='test@student.com'")
    with allure.step("Перевірка, що студента немає"):
        cur.execute("SELECT COUNT(*) FROM students WHERE email = %s;", ("test@student.com",))
        count = cur.fetchone()[0]
        assert count == 0
