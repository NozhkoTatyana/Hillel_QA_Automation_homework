from table_models.students import create_students_table
from table_models.courses import create_courses_table
from table_models.enrollments import create_enrollments_table
from seed import seed_data
from crud_operations import *


def main():
    # створення таблиць
    create_students_table()
    create_courses_table()
    create_enrollments_table()
    print("✅ База даних ініціалізована")

    # наповнення Faker-ом
    seed_data()


    get_students_by_course(6)
    get_courses_by_student(20)
    update_student(21, "New Name", "new_email@example.com")
    update_course(2, "new_course")
    delete_student(5)
    delete_course(1)


if __name__ == "__main__":
    main()
