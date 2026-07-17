from flask import Flask, request, render_template, redirect
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
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# Save form data into MySQL
@app.route("/save", methods=["POST"])
def save():

    # Get form values
    name = request.form["name"]
    email = request.form["email"]

    # Connect to database
    db = get_db_connection()

    # Create cursor
    
    #creates a cursor object that lets Python communicate with your MySQL database.
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

@app.route("/users")
def users():

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("users.html", users=rows)
@app.route("/edit/<int:id>")
def edit(id):

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id=%s",
        (id,)
    )

    user = cursor.fetchone()

    cursor.close()
    db.close()

    return render_template("edit.html", user=user)


@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    name = request.form["name"]
    email = request.form["email"]

    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (name, email, id)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect("/users")
@app.route("/delete/<int:id>")
def delete(id):

    db = get_db_connection()
    cursor = db.cursor()
    #creates a cursor object that lets Python communicate with your MySQL database.
    cursor.execute(
        "DELETE FROM users WHERE id=%s",
        (id,)
    )

    db.commit()

    cursor.close()
    db.close()

    return redirect("/users")

    


@app.route("/about")#must start from the left sid
def about():#must start from the left sid
    return render_template("about.html")


# Create object

# Start Flask server
if __name__ == "__main__":
    app.run(debug=True)