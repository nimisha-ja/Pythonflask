from flask import Flask, request
import mysql.connector

# Create Flask application
app = Flask(__name__)


# MySQL database connection function
def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",       # Add your MySQL password if you have one
        database="test1"
    )
    return db


# Home page - show form
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask MySQL Form</title>
    </head>

    <body>

        <h2>Add User</h2>

        <form action="/save" method="POST">

            Name:
            <br>
            <input type="text" name="name" required>

            <br><br>

            Email:
            <br>
            <input type="email" name="email" required>

            <br><br>

            <button type="submit">
                Save
            </button>

        </form>

    </body>
    </html>
    """


# Save form data into MySQL
@app.route("/save", methods=["POST"])
def save():

    # Get form values
    name = request.form["name"]
    email = request.form["email"]

    # Connect to database
    db = get_db_connection()

    # Create cursor
    cursor = db.cursor()

    # Insert query
    sql = """
    INSERT INTO users (name, email)
    VALUES (%s, %s)
    """

    values = (name, email)

    # Execute query
    cursor.execute(sql, values)

    # Save changes
    db.commit()

    # Close connection
    cursor.close()
    db.close()

    return f"""
    <h2>Data Saved Successfully</h2>

    <p>Name: {name}</p>
    <p>Email: {email}</p>

    <a href="/">Add Another User</a>
    """


# Display all users
@app.route("/users")
def users():

    db = get_db_connection()
    cursor = db.cursor()

    # Get data
    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()

    html = """
    <h2>User List</h2>
    <table border="1">
    <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Email</th>
    </tr>
    """

    for user in rows:
        html += f"""
        <tr>
            <td>{user[0]}</td>
            <td>{user[1]}</td>
            <td>{user[2]}</td>
        </tr>
        """

    html += """
    </table>
    <br>
    <a href="/">Add User</a>
    """

    cursor.close()
    db.close()

    return html


# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)