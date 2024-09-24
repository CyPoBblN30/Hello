import sqlite3

conn = sqlite3.connect('mydatabase.db')
sql = conn.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, age INTEGER, grade TEXT);')
sql.execute('INSERT INTO students VALUES(1, "Vladimir", 23, "5");')
conn.commit()
sql.execute('INSERT INTO students VALUES(2, "Anna", 20, "4");')
conn.commit()
sql.execute('INSERT INTO students VALUES(3, "Dasha", 27, "3");')
conn.commit()

def get_student_by_name():
    new_name = input('Введите имя студента:')
    if new_name == 'Vladimir':
        print(sql.execute('SELECT * FROM students WHERE name="Vladimir";').fetchall())
    elif new_name == 'Anna':
        print(sql.execute('SELECT * FROM students WHERE name="Anna";').fetchall())
    elif new_name == 'Dasha':
        print(sql.execute('SELECT * FROM students WHERE name="Dasha";').fetchall())

get_student_by_name()

def update_student_grade():
    c_name = input('Введите имя студента:')
    new_grade = input('Введите оценку студента: ')
    if c_name == 'Vladimir' and new_grade == '5':
        sql.execute('UPDATE students SET name="Vladimir" WHERE grade=5;')
        conn.commit()
    elif c_name == 'Vladimir' and new_grade == '4':
        sql.execute('UPDATE students SET name="Vladimir" WHERE grade=4;')
        conn.commit()
    elif c_name == 'Vladimir' and new_grade == '3':
        sql.execute('UPDATE students SET name="Vladimir" WHERE grade=3;')
        conn.commit()
    elif c_name == 'Vladimir' and new_grade == '2':
        sql.execute('UPDATE students SET name="Vladimir" WHERE grade=2;')
        conn.commit()
    elif c_name == 'Vladimir' and new_grade == '1':
        sql.execute('UPDATE students SET name="Vladimir" WHERE grade=1;')
        conn.commit()
    elif c_name == 'Anna' and new_grade == '5':
        sql.execute('UPDATE students SET name="Anna" WHERE grade=5;')
        conn.commit()
    elif c_name == 'Anna' and new_grade == '4':
        sql.execute('UPDATE students SET name="Anna" WHERE grade=4;')
        conn.commit()
    elif c_name == 'Anna' and new_grade == '3':
        sql.execute('UPDATE students SET name="Anna" WHERE grade=3;')
        conn.commit()
    elif c_name == 'Anna' and new_grade == '2':
        sql.execute('UPDATE students SET name="Anna" WHERE grade=2;')
        conn.commit()
    elif c_name == 'Anna' and new_grade == '1':
        sql.execute('UPDATE students SET name="Anna" WHERE grade=1;')
        conn.commit()
    elif c_name == 'Dasha' and new_grade == '5':
        sql.execute('UPDATE students SET name="Dasha" WHERE grade=5;')
        conn.commit()
    elif c_name == 'Dasha' and new_grade == '4':
        sql.execute('UPDATE students SET name="Dasha" WHERE grade=4;')
        conn.commit()
    elif c_name == 'Dasha' and new_grade == '3':
        sql.execute('UPDATE students SET name="Dasha" WHERE grade=3;')
        conn.commit()
    elif c_name == 'Dasha' and new_grade == '2':
        sql.execute('UPDATE students SET name="Dasha" WHERE grade=2;')
        conn.commit()
    elif c_name == 'Dasha' and new_grade == '1':
        sql.execute('UPDATE students SET name="Dasha" WHERE grade=1;')
        conn.commit()

update_student_grade()
get_student_by_name()

def delete_student():
    delete_name = input('Введите имя студента: ')
    if delete_name == 'Vladimir':
        sql.execute('DELETE FROM students WHERE name="Vladimir";')
        conn.commit()
    elif delete_name == 'Anna':
        sql.execute('DELETE FROM students WHERE name="Anna";')
        conn.commit()
    elif delete_name == 'Dasha':
        sql.execute('DELETE FROM students WHERE name="Dasha";')
        conn.commit()

delete_student()
get_student_by_name()

