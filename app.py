from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

def read_users_from_csv():
    users = []
    with open('users.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def validate_user(username, password):
    users = read_users_from_csv()
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_user(username, password):
            return redirect(url_for('protected'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')

@app.route('/protected')
def protected():
    return 'You are logged in!'

if __name__ == '__main__':
    app.run(debug=True)