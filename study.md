Flask and Django are both Python frameworks used to build websites and web applications.

A framework is a collection of tools and rules that helps you build applications faster instead of creating everything from scratch.

Flask

Flask is a small and flexible Python web framework
-----

Your current app can:
Browser Form
      |
      ↓
Flask Route (@app.route)
      |
      ↓
Python Code (request.form)
      |
      ↓
MySQL Connector
      |
      ↓
MySQL Database (testdb → users)

✅ Show a form
✅ Receive user input
✅ Insert data into MySQL
✅ Display saved records

Good next steps to learn:

Update user records
Edit button
Update name/email in MySQL
Delete records
Delete button
Remove data from MySQL
Use HTML templates
Move HTML from app.py into templates/
Similar to Laravel Blade or PHP views
Add CSS styling
Make the page look professional
Add login system
User registration
Password hashing
Sessions

You already have the foundation of a small Flask web application.

--completedon11-07

class Student:

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

Good next topics to learn:
Python
Classes and objects (OOP)
student1 = Student("John", 20, 90)

# Call method
student1.display()

try:
    number = int(input("Enter a number: "))

    print(number)

except:
    print("Please enter a valid number")
    
Error handling (try/except)
File handling
Modules and packages
Virtual environments
Flask
Bootstrap UI
Flash messages
User login system
Password hashing
Sessions
Blueprints
Database
Relationships (one-to-many, many-to-many)
SQL joins
ORM with SQLAlchemy-queries