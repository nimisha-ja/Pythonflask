from flask import Flask, request

# Create the Flask application
app = Flask(__name__)

# Display the form
@app.route("/")
def home():

    # Return the HTML form
    return """
    <h2>Simple Flask Form</h2>

    <form action="/submit" method="POST">

        Name:<br>
        <input type="text" name="name"><br><br>

        Email:<br>
        <input type="email" name="email"><br><br>

        <input type="submit" value="Submit">

    </form>
    """

# Handle the form submission
@app.route("/submit", methods=["POST"])
def submit():

    # Get the values entered in the form
    name = request.form["name"]
    email = request.form["email"]

    # Return the submitted values
    return f"""
    <h2>Form Submitted</h2>

    <p><b>Name:</b> {name}</p>

    <p><b>Email:</b> {email}</p>

    <a href="/">Back</a>
    """

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)