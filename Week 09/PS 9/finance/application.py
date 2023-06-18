import os
# export API_KEY=pk_13302fabef474f64a4fa8e5e77a549b7
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # get user cash total
    result = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    cash = result[0]['cash']

    # Using the database to get values
    stocks = db.execute("SELECT StockSymbol, StockName, StockShares, StockPrice FROM purchase_details WHERE UserID=:ui", ui=session["user_id"])
    total = cash

    for stock in stocks:
        total +=  stock["StockPrice"] * stock["StockShares"]

    return render_template("index.html", stocks=stocks, cash=cash, usd=usd, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        # Checking for shares
        elif not request.form.get("shares").isdigit():
            return apology("Invalid number of shares")

        try:
            # Using the lookup() function
            StockInfo = lookup(request.form.get("symbol"))

            StockSymbol=StockInfo["symbol"]
            StockName=StockInfo["name"]
            StockPrice=StockInfo["price"]

        except TypeError:
            return apology("symbol is not valid")

        # Checking for validity
        if StockInfo == None:
            return apology("symbol is not valid")

        # Total Cost
        totalCost = int(request.form.get("shares")) * StockPrice

        # Checking whether the user can afford them
        userMoney = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
        if totalCost > userMoney[0]["cash"]:
            return apology("Not enough money to carry out this transaction")
        else:
            db.execute("UPDATE users SET cash=cash-:cost WHERE id=:id", cost=totalCost, id=session["user_id"]);

        # Adding number of shares if they already exist or making new if they dont
        current = db.execute("SELECT StockShares FROM purchase_details WHERE StockSymbol=:stock", stock=StockSymbol)

        if current:
            db.execute("UPDATE purchase_details SET StockShares=StockShares+:new_shares WHERE StockSymbol=:StockSymbol;", new_shares = request.form.get("shares"), StockSymbol = StockSymbol)

        else:
            # Storing values in a database
            db.execute("INSERT INTO purchase_details (userID, stockSymbol, StockName, StockShares, StockPrice, PurchaseDate) VALUES(?, ?, ?, ?, ?, ?);", session["user_id"], StockSymbol, StockName, int(request.form.get("shares")), StockPrice, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Keeping track
        db.execute("INSERT INTO history VALUES (?, ?, ?, ?);", request.form.get("symbol"), int(request.form.get("shares")), StockPrice, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return redirect("/")

    else:
        return render_template("purchase.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT * FROM history")
    return render_template("history.html", stocks=history, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        # Checking whether the name of stock was submitted
        if not request.form.get("symbol"):
            return apology("Enter a stock symbol")

        try:
            # Using the lookup() function
            quote = lookup(request.form.get("symbol"))

            symbol=quote["symbol"]
            name=quote["name"]
            price=usd(quote["price"])
        except TypeError:
            return apology("symbol is not valid")

        # if stock name is valid
        else:
            return render_template("quoted.html", symbol=symbol, name=name, price=price)

        return render_template("quoted.html")

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password")

        # Ensure password (again) was submitted
        if not request.form.get("confirmation"):
            return apology("must confirm your password")

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match")

        # hash password
        hash = generate_password_hash(request.form.get("password"))

        # Store the values in a database
        try:
            storing = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hash)
        except:
            return apology("username already exists")

        # Checking for a unique username
        if not storing:
            return apology("username already exists")

        # Keeping track of logged in users
        session["user_id"] = storing

        # redirect to the login page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    if request.method == "POST":
        # checking if symbol is provided
        if not request.form.get("symbol"):
            return apology("must provide stock symbol")

        # checking if the user is selling at least one stock
        if int(request.form.get("shares")) < 1:
            return apology("must sell at least one share")

        # checking if the user owns the number of stocks which are being sold
        numberOfStocks = db.execute("SELECT StockShares FROM purchase_details WHERE StockSymbol=:Stock;", Stock=request.form.get("symbol").upper())
        if numberOfStocks[0]['StockShares'] < int(request.form.get("shares")):
            return apology("you do not have enough shares")

        # Updating the database
        # pull quote
        quote = lookup(request.form.get("symbol"))
        name = quote["name"]
        price = quote["price"]

        db.execute("UPDATE purchase_details SET StockShares=StockShares-:number WHERE StockSymbol=:s", number=request.form.get("shares"), s=request.form.get("symbol").upper())
        db.execute("UPDATE users SET cash=cash+:new WHERE id=:ID;", new=price*int(request.form.get("shares")), ID=session["user_id"])

        # Keeping track
        db.execute("INSERT INTO history VALUES (?, ?, ?, ?);", request.form.get("symbol"), "-"+request.form.get("shares"), price, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        return redirect("/")

    else:
        currPortfolio = db.execute("SELECT StockSymbol FROM purchase_details")
        return render_template("sell.html", stocks=currPortfolio)

@app.route("/add-cash", methods=["GET", "POST"])
@login_required
def add_cash():
    """Adding to the users existing cash"""
    if request.method == "POST":
        # Checking for valid input
        if not request.form.get("cash"):
            return apology("Please enter some cash")

        db.execute("UPDATE users SET cash=cash+:C WHERE id=:ID;", C=int(request.form.get("cash")), ID=session["user_id"])

        return redirect("/")

    else:
        cash = db.execute("SELECT cash FROM users WHERE id=:ID;", ID=session["user_id"])
        user_cash = cash[0]['cash']
        return render_template("cash.html", cash=user_cash, usd=usd)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
