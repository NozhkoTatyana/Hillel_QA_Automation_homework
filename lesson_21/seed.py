from db_connection import get_connection
from faker import Faker
import random

fake = Faker()

def seed_data():
    conn = get_connection()
    cur = conn.cursor()

    # перевіряємо чи вже є студенти
    cur.execute("SELECT COUNT(*) FROM students;")
    students_count = cur.fetchone()[0]

    if students_count > 0:
        print("ℹ️ База вже заповнена")
        cur.close()
        conn.close()
        return

    # 5 курсів
    courses = [
        'Mathematics',
        'Physics',
        'Computer Science',
        'History',
        'Literature'
    ]

    for c in courses:
        cur.execute(
            "INSERT INTO courses (title) VALUES (%s);",
            (c,)
        )

    # 20 студентів
    for _ in range(20):
        name = fake.name()
        email = fake.unique.email()

        cur.execute(
            """
            INSERT INTO students (name, email)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (name, email)
        )

        student_id = cur.fetchone()[0]

        # випадкові курси
        course_ids = random.sample(
            range(1, 6),
            k=random.randint(1, 3)
        )

        for course_id in course_ids:
            cur.execute(
                """
                INSERT INTO enrollments (student_id, course_id)
                VALUES (%s, %s);
                """,
                (student_id, course_id)
            )

    conn.commit()

    print("✅ Дані успішно згенеровані")

    cur.close()
    conn.close()
