from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Registration form route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        # Save data to registration.csv
        with open('registration.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, course])
        
        return f"Thanks {name} , you have registered for {course}!"
    
    return render_template('register.html')

# View all registered students
@app.route('/students')
def view_students():
    students = []
    try:
        with open('registration.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        pass  # File will be created on first registration
    
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)