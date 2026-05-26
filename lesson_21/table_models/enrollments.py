from lesson_21.db_connection import get_connection

def create_enrollments_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            student_id INT REFERENCES students(id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(id) ON DELETE CASCADE,
            PRIMARY KEY (student_id, course_id)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
