import psycopg2 as pg


def create_db(): # создает таблицы
    pass


def get_students(course_id): # возвращает студентов определенного курса
    pass


def add_students(course_id, students): # создает студентов и
                                       # записывает их на курс
    pass


def add_student(student): # просто создает студента
    pass


def get_student(student_id):
    pass


def main():
    with pg.connect(database='netology_students',
                      user='netology',
                      password='k23ldr8',
                      host='127.0.0.1',
                      port='5432') as conn:
        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Test(
        id integer);
        ''')


if __name__ == '__main__':
    main()