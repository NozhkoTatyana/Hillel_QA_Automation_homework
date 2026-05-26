from lesson_21.db_connection import get_connection

def create_courses_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
