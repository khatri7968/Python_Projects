from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

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

def insert_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM student")
    count = cursor.fetchone()[0]
    if count == 0:  # Check if the table is empty
        data = [
            (1, 'Babar', 'Azam', '123 Main St'),
            (2, 'Alice', 'Smith', '456 Elm St'),
            (3, 'Chris', 'Gayle', '789 Oak St'),
            (4, 'Emma', 'Davis', '101 Pine St'),
            (5, 'Mohmad', 'Amir', '202 Cedar St')
        ]
        cursor.executemany("INSERT INTO student(id, first_name, last_name, address) VALUES(%s, %s, %s, %s)", data)
        conn.commit()


def get_data_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM student''')
    rs = cursor.fetchall()
    return rs

def add_student(conn, data):
    try:
        cur = conn.cursor()
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

# Establish a connection to the database
connection = create_connection()
# Ensure the student table exists
create_student_table(connection)

@app.route('/')
def show_names():
    # Retrieve data from the database
    student_data = get_data_from_db(connection)
    return render_template('index.html', students=student_data)

@app.route('/add_student', methods=['POST'])
def add_student_route():
    new_student = (
        int(request.form['id']),
        request.form['firstName'],
        request.form['lastName'],
        request.form['address']
    )
    add_student(connection, new_student)
    return jsonify({"message": "Student added successfully"})

@app.route('/remove_student', methods=['POST'])
def remove_student_route():
    remove_id = int(request.form['removeId'])
    remove_student(connection, remove_id)
    return jsonify({"message": "Student removed successfully"})

if __name__ == '__main__':

    app.run(debug=True)

