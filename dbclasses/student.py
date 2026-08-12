import sqlite3

conn=sqlite3.connect('dbclasses/students.db')
cursor=conn.cursor()
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS students
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT)
    '''
    )
conn.commit()
conn.close()

def insert_student(name, age, grade):
    conn=sqlite3.connect('dbclasses/students.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        INSERT INTO students (name, age, grade)
        VALUES (?, ?, ?)
        ''', (name, age, grade)
    )
    conn.commit()
    conn.close()

def get_all_students():
    conn=sqlite3.connect('dbclasses/students.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        SELECT * FROM students
        '''
    )
    students=cursor.fetchall()
    conn.close()
    return students
def get_student_by_id(student_id):
    conn=sqlite3.connect('dbclasses/students.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        SELECT * FROM students WHERE id=?
        ''', (student_id,)
    )
    student=cursor.fetchone()
    conn.close()
    return student
def update_student(student_id, name, age, grade):
    conn=sqlite3.connect('dbclasses/students.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        UPDATE students
        SET name=?, age=?, grade=?
        WHERE id=?
        ''', (name, age, grade, student_id)
    )
    conn.commit()
    conn.close()
def delete_student(student_id):
    conn=sqlite3.connect('dbclasses/students.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        DELETE FROM students WHERE id=?
        ''', (student_id,)
    )
    conn.commit()
    conn.close()

while True:
    print("1. Insert Student")
    print("2. Get All Students")
    print("3. Get Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        grade=input("Enter grade: ")
        insert_student(name, age, grade)
        print("Student inserted successfully.")
    elif choice==2:
        students=get_all_students()
        for student in students:
            print(student)
    elif choice==3:
        student_id=int(input("Enter student ID: "))
        student=get_student_by_id(student_id)
        if student:
            print(student)
        else:
            print("Student not found.")
    elif choice==4:
        student_id=int(input("Enter student ID: "))
        name=input("Enter new name: ")
        age=int(input("Enter new age: "))
        grade=input("Enter new grade: ")
        update_student(student_id, name, age, grade)
        print("Student updated successfully.")
    elif choice==5:
        student_id=int(input("Enter student ID: "))
        delete_student(student_id)
        print("Student deleted successfully.")
    elif choice==6:
        break
    else:
        print("Invalid choice. Please try again.")