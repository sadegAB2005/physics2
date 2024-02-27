import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure MySQL database connection
db_config = {
    'host': 'sadegAB.mysql.pythonanywhere-services.com',
    'user': 'sadegAB',
    'password': '9>T-@7q_HMMhX%?',
    'database': 'sadegAB$default',
}

@app.route('/')
def index():
    return render_template('html2.html')

@app.route('/test', methods=['POST'])
def handle_form_submission():
    username = request.form.get('username')
    password = request.form.get('password')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    subject = request.form.get('subject')

    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute SQL query to insert form data into the database
        query = "INSERT INTO UserData (username, password, mobile, email, subject) VALUES (%s, %s, %s, %s, %s)"
        data = (username, password, mobile, email, subject)
        cursor.execute(query, data)

        # Commit the transaction
        connection.commit()

        # Close database connection
        cursor.close()
        connection.close()

        return render_template('html1.html')

    except mysql.connector.Error as error:
        return f"Error: {error}"

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=8001)
