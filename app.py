import logging
# test.py

from flask import Flask, abort, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    try:
        logging.info('Rendering index page')
        return render_template('html2.html', )#content=dynamic_content)
    except Exception as e:
        return str(e)

@app.route('/test', methods=['POST'])
def handle_form_submission():
    username = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    subject = request.form.get('subject')

    # Save form data to CSV file
    with open('form_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, mobile, email, subject])

    # For testing purposes, let's just print the values
    print(f"Username: {username}")
    print(f"Password: {password}")
    print(f"Mobile: {mobile}")
    print(f"Email: {email}")
    print(f"Subject: {subject}")

    return render_template('html1.html')
if __name__ == '__main__':
    app.run(debug=False)
