from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import errorcode

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="pavan",
    password="atari",
    database="userdb"
)

mycursor = mydb.cursor()

# Create database and table if they don't exist
def create_database_and_table():
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS userdb")
        mycursor.execute("USE userdb")
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL
            )
        """)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

create_database_and_table()

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    username = request.headers.get('Username')
    password = request.headers.get('Password')

    mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = mycursor.fetchone()

    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/signup', methods=['POST'])
def signup():
    username = request.headers.get('Username')
    password = request.headers.get('Password')

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    try:
        mycursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mydb.commit()
        return jsonify({"message": "Signup successful"}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"message": "Username already exists"}), 409

if __name__ == '__main__':
    app.run()
