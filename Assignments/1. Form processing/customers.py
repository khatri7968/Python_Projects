from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ArrayList of Student Information
student_list = [
    {"id": 1, "firstName": "Babar", "lastName": "Azam", "address": "123 Main St"},
    {"id": 2, "firstName": "Ahmad", "lastName": "Shahzad", "address": "456 Elm St"},
    {"id": 3, "firstName": "Mohmad", "lastName": "Amir", "address": "123 Main St"},
    {"id": 4, "firstName": "Shoab", "lastName": "Malik", "address": "456 Elm St"},
    {"id": 5, "firstName": "Chirs", "lastName": "Gayle", "address": "123 Main St"}
]

# Show the list of names
@app.route('/')
def show_names():
    return render_template('index.html', students=student_list)

# Add a student to the list
@app.route('/add_student', methods=['POST'])
def add_student():
    new_student = {
        "id": int(request.form['id']),
        "firstName": request.form['firstName'],
        "lastName": request.form['lastName'],
        "address": request.form['address']
    }
    student_list.append(new_student)
    return jsonify({"message": "Student added successfully"})

# Remove a student from the list
@app.route('/remove_student', methods=['POST'])
def remove_student():
    remove_id = int(request.form['removeId'])
    for student in student_list:
        if student["id"] == remove_id:
            student_list.remove(student)
            return jsonify({"message": "Student removed successfully"})
    return jsonify({"message": "Student ID not found"})

if __name__ == '__main__':
    app.run(debug=True)
