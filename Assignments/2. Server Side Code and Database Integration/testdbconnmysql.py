import mysql.connector

def create_connection():
    conn = None
    try:
        # Connecting to MySQL without specifying a database
        conn = mysql.connector.connect(user='root', password='M@psa#926', host='localhost')
        cursor = conn.cursor()

        # Creating the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")

        # Connecting to the newly created or existing database
        conn = mysql.connector.connect(user='root', password='M@psa#926', host='localhost', database='studentdb')
        cursor = conn.cursor()

        cursor.execute("SELECT DATABASE()")
        info = cursor.fetchone()
        print("Connection established to: ", info)

    except Exception as e:
        print(e)
    return conn

def create_student_table(conn):
    try:
        cursor = conn.cursor()

        # Creating the 'student' table without auto-increment for id
        cursor.execute("CREATE TABLE IF NOT EXISTS student (id INT PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), address VARCHAR(100))")
        print("Table 'student' created successfully")

    except Exception as e:
        print(e)



def insert_data(conn, student_data):

    cur = conn.cursor()
    cur.executemany("INSERT INTO student(id, first_name, last_name, address) VALUES(%s, %s, %s, %s)", student_data)

    conn.commit()

def get_data_from_student():
    sid = input("Student ID: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    address = input("Address: ")
    return (sid,fname,lname,address)

def get_data_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM STUDENT''')
    rs = cursor.fetchall()
    return rs

def display_data(rset):
    for st in rset:
        print(st)


def add_student(conn, data):
    data_from_db = get_data_from_db(connection)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO student(id, first_name, last_name, address) VALUES(%s, %s, %s, %s)", data)
        conn.commit()
        print("Student added successfully.")
    except Exception as e:
        print(e)

def remove_student(conn, student_id):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM student WHERE id = %s", (student_id,))
        conn.commit()
        print("Student removed successfully.")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    connection = create_connection()
    if connection:
        create_student_table(connection)

        student_data = [
            (1, 'John', 'Doe', '123 Main St'),
            (2, 'Alice', 'Smith', '456 Elm St'),
            (3, 'Bob', 'Johnson', '789 Oak St'),
            (4, 'Emma', 'Davis', '101 Pine St'),
            (5, 'Michael', 'Wilson', '202 Cedar St')
        ]
        # Insert 5 records using
        insert_data(connection, student_data)

        # Displaying data from the database after insertion
        data_from_db = get_data_from_db(connection)
        display_data(data_from_db)


        data = [1, "","", ""]
        print("enter data for the new student you want to add")
        data[0] = int(input("Enter the ID of the student: "))
        data[1] = input("Enter the first name of the student: ")
        data[2] = input("Enter the first name of the student: ")
        data[3] = input("Enter the address of the student: ")

        add_student(connection, data)

        # Displaying data from the database after insertion
        data_from_db = get_data_from_db(connection)
        display_data(data_from_db)

        # Get student ID to remove
        student_id= int(input("Enter the ID of the student to remove: "))
        # Remove a student using the entered ID
        remove_student(connection, student_id)
        data_from_db = get_data_from_db(connection)
        display_data(data_from_db)