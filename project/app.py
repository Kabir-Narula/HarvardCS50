# export API_KEY=AIzaSyAmfVWfMceaa4smClnH_deKGlrXMMvCIQw
from cs50 import SQL
from flask import Flask, app, render_template, request, redirect, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import requests

# Configure application
app = Flask(__name__)

# Configure Sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#configuring the database for the application
db = SQL("sqlite:///user.db")

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Homepage
@app.route("/", methods=["GET", "POST"])
def index():
    """ Homepage """
    return render_template("index.html")

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    """ Register User """
    if request.method == "POST":

        # Collecting the details provided by the user
        name = request.form.get("fullname")
        username = request.form.get("username")
        password = request.form.get("password")
        check = request.form.get("confirmation")

        # generating a hash password
        hash = generate_password_hash(request.form.get("password"))

        # Validating the inputs
        if not name or not username or not password or not check:
            message = "All fields were not filled"
            return render_template("apology.html", message=message)

        if request.form.get("password") != request.form.get("confirmation"):
            message = "Passwords do not match"
            return render_template("apology.html", message=message)

        # Querying the database and determining whether the username already exists
        rows = db.execute("SELECT * FROM registrants WHERE username=:un", un = username)

        if len(rows) != 0:
            message = "Username already exists"
            return render_template("apology.html", message=message)

        # Password Validation
        if len(request.form.get("password")) < 5:
            message = "Password should be at least 5 characters long"
            return render_template("apology.html", message=message)

        # Storing the user's data
        db.execute("INSERT INTO registrants (name, username, password) VALUES(?, ?, ?);", name, username, hash)

        # Redirecting the user to the login page
        return redirect("/login")

    else:
        return render_template("register.html")

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    """ User can log in """

    # Forget any user_id
    session.clear()

    if request.method == "POST":
        # Validating the inputs
        if not request.form.get("username") or not request.form.get("password"):
            message = "All fields were not filled"
            return render_template("apology.html", message=message)

        # Querying the database
        rows = db.execute("SELECT * FROM registrants WHERE username = :un", un = request.form.get("username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            message = "Incorrect username or password"
            return render_template("apology.html", message=message)

        # Creating a session
        session["username"] = request.form.get("username")

        # Redirecting the user to homepage if everything is correct
        return redirect("/")

    else:
        return render_template("login.html")

# Allows the user to log out
@app.route("/logout", methods=["GET", "POST"])
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# Allows the user to search for the books they want to add in their reading list
@app.route("/search", methods=["GET", "POST"])
def search():
    """ Users can search for books """
    # Validating input
    if not request.form.get("book"):
        message = "Search field left empty"
        return render_template("apology.html", message=message)

    return render_template("search.html", books = requests.get("https://www.googleapis.com/books/v1/volumes?q=" +
                               request.form.get("book") + "&key=AIzaSyAmfVWfMceaa4smClnH_deKGlrXMMvCIQw").json())

# Allows user to create a list of the books they read
@app.route("/reading-list", methods=["GET", "POST"])
def readingList():
    """ Users can make a list of the books they have read """
    # Users have to log in in order ot create a reading list
    if not session.get("username"):
        return redirect("/login")

    if request.method == "POST":
        db.execute("INSERT INTO userBookList (title, author) VALUES(?, ?);", request.form.get("title"), request.form.get("author"))

        return redirect("/reading-list")

    else:
        books = db.execute("SELECT * FROM userBookList")
        return render_template("readingList.html", books=books)

# Allows user to reset their reading list
@app.route("/remove-all", methods=["GET", "POST"])
def remove_all():
    """ Erases all the books stored by the user """
    db.execute("DELETE FROM userBookList")
    return redirect("/reading-list")

if __name__ == "__main__":
    app.run(debug=True)