from conftest import logger


def test_connection(conn):
    assert conn is not None

def test_insert_student(conn):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s) RETURNING id;",
        ("Test Student", "test@student.com")
    )
    student_id = cur.fetchone()[0]
    conn.commit()
    logger.info(f"Вставлено студента id={student_id}, name='Test Student', email='test@student.com'")
    assert student_id is not None

def test_select_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM students;")
    rows = cur.fetchall()
    logger.info(f"У таблиці students {len(rows)} записів: {rows}")
    assert isinstance(rows, list)

def test_update_student(conn):
    cur = conn.cursor()
    cur.execute(
        "UPDATE students SET name = %s WHERE email = %s;",
        ("Updated Student", "test@student.com")
    )
    conn.commit()
    logger.info("Оновлено ім’я студента на 'Updated Student'")
    cur.execute("SELECT name FROM students WHERE email = %s;", ("test@student.com",))
    name = cur.fetchone()[0]
    assert name == "Updated Student"

def test_delete_student(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE email = %s;", ("test@student.com",))
    conn.commit()
    logger.info("Видалено студента з email='test@student.com'")
    cur.execute("SELECT COUNT(*) FROM students WHERE email = %s;", ("test@student.com",))
    count = cur.fetchone()[0]
    assert count == 0