import psycopg2 as pg


def delete_tables(cur):
    cur.execute('''
        DROP TABLE IF EXISTS student_course;
        DROP TABLE IF EXISTS students;
        DROP TABLE IF EXISTS courses;
        ''')


def create_db(cur):  # создает таблицы
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(100) NOT NULL DEFAULT 'NULL',
        gpa DECIMAL(10,2) NULL DEFAULT NULL,
        birth TIMESTAMPTZ NULL DEFAULT NULL
        );
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS courses (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(100) NOT NULL DEFAULT 'NULL'
        );
        ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS student_course (
        id SERIAL PRIMARY KEY NOT NULL,
        student_id INTEGER NOT NULL DEFAULT NULL,
        course_id INTEGER NOT NULL DEFAULT NULL
        );
        ''')

    cur.execute('''
        ALTER TABLE student_course ADD FOREIGN KEY (student_id) REFERENCES students (id);
        ALTER TABLE student_course ADD FOREIGN KEY (course_id) REFERENCES courses (id);
        ''')


def get_students(cur, course_id):  # возвращает студентов определенного курса
    cur.execute('''
        SELECT name FROM students
        JOIN student_course ON students.id = student_course.student_id
        WHERE student_course.course_id = %s
        ''', (course_id,))
    print(cur.fetchall())


def add_students(cur, course_id, students):  # создает студентов и записывает их на курс
    for student in students:
        add_student(cur, student)

        cur.execute('''
            SELECT id FROM students
            WHERE name = %s
            ''', (student['name'],))
        student_id = cur.fetchone()

        cur.execute('''
            INSERT INTO student_course (student_id, course_id) VALUES
            (%s, %s)
            ''', (student_id, course_id))


def add_student(cur, student):  # просто создает студента
    cur.execute('''
    INSERT INTO students (name, gpa, birth) VALUES
    ( %s, %s, %s);
    ''', (student['name'], student['gpa'], student['birth']))


def add_course(cur, course):
    cur.execute('''
        INSERT INTO courses (name) VALUES
        (%s);
        ''', (course['name'],))


def get_student(cur, student_id):
    cur.execute('''
        SELECT name FROM students
        WHERE id = %s
        ''', (student_id,))
    print(cur.fetchall())


def main():
    with pg.connect(database='netology_students',
                    user='netology',
                    password='k23ldr8',
                    host='127.0.0.1',
                    port='5432') as conn:
        cur = conn.cursor()
        delete_tables(cur)
        create_db(cur)

        course_1 = {
            'name': 'AdPy'
        }

        add_course(cur, course_1)

        student_1 = {
            'name': 'student_name_1',
            'gpa': 4.44,
            'birth': '01.01.2001'
        }

        student_2 = {
            'name': 'student_name_2',
            'gpa': 4.45,
            'birth': '02.02.2002'
        }

        students = (student_1, student_2)

        add_students(cur, 1, students)

        get_students(cur, 1)
        get_students(cur, 2)

        # add_student(cur, student_1)
        # add_student(cur, student_2)

        # cur.execute('''
        #     SELECT * FROM students
        #     ''')
        # print(cur.fetchall())

        # get_student(cur, 1)


if __name__ == '__main__':
    main()