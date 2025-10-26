from flask import Flask, jsonify, request, render_template_string

app = Flask(__name__)

# 👨‍🎓 In-memory student data
students = [
    {"name": "Jedidiah Defacto", "grade": 95, "bmi": 22.3, "address": "Iloilo City", "gender": "Male", "age": 21}
]

# 🏠 Home page (User Interface)
@app.route('/')
def home():
    html = """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Student Manager | Jedidiah Defacto</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(135deg, #74b9ff, #a29bfe);
                margin: 0;
                color: #2d3436;
            }
            h1 {
                text-align: center;
                color: #fff;
                padding: 20px 0;
                text-shadow: 2px 2px 6px rgba(0,0,0,0.2);
            }
            .quote {
                text-align: center;
                color: #fff;
                font-style: italic;
                margin-bottom: 20px;
                font-size: 1.1em;
            }
            form {
                background: #ffffff;
                padding: 20px;
                border-radius: 15px;
                width: 340px;
                margin: 20px auto;
                box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            }
            form h3 {
                text-align: center;
                color: #0984e3;
            }
            input, select, button {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
                font-size: 15px;
            }
            button {
                background: #0984e3;
                color: white;
                border: none;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: #0652DD;
                transform: scale(1.02);
            }
            .student-list {
                max-width: 700px;
                margin: 30px auto;
                background: rgba(255,255,255,0.9);
                border-radius: 15px;
                padding: 20px;
                box-shadow: 0 3px 8px rgba(0,0,0,0.2);
            }
            .student-card {
                background: #f1f2f6;
                padding: 15px 20px;
                margin-bottom: 15px;
                border-radius: 10px;
                box-shadow: 0 1px 4px rgba(0,0,0,0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
                position: relative;
            }
            .student-info {
                flex: 1;
            }
            .student-info strong {
                color: #2d3436;
                font-size: 18px;
            }
            .delete-btn {
                background: #d63031;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 6px;
                cursor: pointer;
                transition: 0.3s;
                font-size: 14px;
            }
            .delete-btn:hover {
                background: #b71c1c;
                transform: scale(1.05);
            }
            footer {
                text-align: center;
                color: #fff;
                margin: 20px 0;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <h1>📘 Student Management System</h1>
        <p class="quote">"Success doesn’t come from what you do occasionally, it comes from what you do consistently." – Jedidiah Defacto</p>

        <form method="POST" action="/add_student">
            <h3>Add New Student</h3>
            <input type="text" name="name" placeholder="Full Name" required>
            <input type="number" name="grade" placeholder="Grade (0-100)" required>
            <input type="number" step="0.1" name="bmi" placeholder="BMI" required>
            <input type="text" name="address" placeholder="Address" required>
            <select name="gender" required>
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
            <input type="number" name="age" placeholder="Age" required>
            <button type="submit">➕ Add Student</button>
        </form>

        <div class="student-list">
            <h3>📋 List of Students</h3>
            {% for s in students %}
                <div class="student-card">
                    <div class="student-info">
                        <strong>{{ s.name }}</strong><br>
                        Grade: {{ s.grade }} | BMI: {{ s.bmi }} | Age: {{ s.age }} | Gender: {{ s.gender }}<br>
                        Address: {{ s.address }}
                    </div>
                    <form method="POST" action="/delete_student">
                        <input type="hidden" name="name" value="{{ s.name }}">
                        <button class="delete-btn" type="submit">🗑️ Delete</button>
                    </form>
                </div>
            {% endfor %}
        </div>

        <footer>Created by <strong>Jedidiah Defacto</strong> | Flask App © 2025</footer>
    </body>
    </html>
    """
    return render_template_string(html, students=students)

# ➕ Add Student
@app.route('/add_student', methods=['POST'])
def add_student():
    new_student = {
        "name": request.form['name'],
        "grade": int(request.form['grade']),
        "bmi": float(request.form['bmi']),
        "address": request.form['address'],
        "gender": request.form['gender'],
        "age": int(request.form['age'])
    }
    students.append(new_student)
    return home()

# ❌ Delete Student by name
@app.route('/delete_student', methods=['POST'])
def delete_student():
    name = request.form['name']
    global students
    students = [s for s in students if s['name'] != name]
    return home()

# 🧩 Optional: JSON API endpoint
@app.route('/api/students')
def get_all_students():
    return jsonify(students)

if __name__ == '__main__':
    app.run(debug=True)
