from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'varun@vk13'
app.config['MYSQL_PASSWORD'] = 'varun@vk13'
app.config['MYSQL_DB'] = 'khk'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        if password == confirm_password:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO varun (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
            mysql.connection.commit()
            cur.close()
            return 'Registration successful'
        else:
            return 'Passwords do not match'
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)