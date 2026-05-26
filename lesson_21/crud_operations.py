from db_connection import get_connection
from tabulate import tabulate


# --- SELECT ---
def get_students_by_course(course_id):
    print()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.title, s.id, s.name, s.email
        FROM students s
        JOIN enrollments e ON s.id = e.student_id
        JOIN courses c ON e.course_id = c.id
        WHERE e.course_id = %s;
    """, (course_id,))
    rows = cur.fetchall()
    if rows:
        course_title = rows[0][0]
        print(f"Студенти на курсі {course_title}:")
        # формуємо таблицю
        table = [(r[1], r[2], r[3]) for r in rows]
        print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))
    else:
        print("На цьому курсі немає студентів.")

    print()
    cur.close()
    conn.close()

def get_courses_by_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT s.name, s.id, c.id, c.title
        FROM courses c
        JOIN enrollments e ON c.id = e.course_id
        JOIN students s ON e.student_id = s.id
        WHERE e.student_id = %s;
    """, (student_id,))
    rows = cur.fetchall()

    if rows:
        student_name = rows[0][0]
        student_id_val = rows[0][1]
        print(f"Курси студента {student_name} (ID: {student_id_val}):")

        # формуємо таблицю: ID курсу + назва
        table = [(r[2], r[3]) for r in rows]
        print(tabulate(table, headers=["Course ID", "Course Title"], tablefmt="grid"))
    else:
        print("Студент не зареєстрований на жоден курс.")

    print()
    cur.close()
    conn.close()


# --- UPDATE ---
def update_student(student_id, new_name, new_email):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE students
        SET name = %s, email = %s
        WHERE id = %s;
    """, (new_name, new_email, student_id))
    conn.commit()

    cur.execute("SELECT id, name, email FROM students WHERE id = %s;", (student_id,))
    row = cur.fetchone()
    print("Оновлений студент:")
    if row:
        print(tabulate([row], headers=["ID", "Name", "Email"], tablefmt="grid"))
    else:
        print("Студента з таким ID не знайдено.")

    print()
    cur.close()
    conn.close()

def update_course(course_id, new_title):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE courses
        SET title = %s
        WHERE id = %s;
    """, (new_title, course_id))
    conn.commit()

    cur.execute("SELECT id, title FROM courses WHERE id = %s;", (course_id,))
    row = cur.fetchone()

    print("Оновлений курс:")
    if row:
        print(tabulate([row], headers=["Course ID", "Title"], tablefmt="grid"))
    else:
        print("Курс із таким ID не знайдено.")

    print()
    cur.close()
    conn.close()


# --- DELETE ---
def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM students WHERE id = %s;", (student_id,))
    row = cur.fetchone()

    cur.execute("DELETE FROM students WHERE id = %s;", (student_id,))
    conn.commit()

    print("Видалений студент:")
    if row:
        print(tabulate([row], headers=["ID", "Name", "Email"], tablefmt="grid"))
    else:
        print("Студента не знайдено.")

    print()
    cur.close()
    conn.close()


def delete_course(course_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title FROM courses WHERE id = %s;", (course_id,))
    row = cur.fetchone()

    cur.execute("DELETE FROM courses WHERE id = %s;", (course_id,))
    conn.commit()

    print("Видалений курс:")
    if row:
        print(tabulate([row], headers=["Course ID", "Title"], tablefmt="grid"))
    else:
        print("Курс не знайдено.")

    print()
    cur.close()
    conn.close()
