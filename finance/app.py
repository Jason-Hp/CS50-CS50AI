import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    help = 0
    Current = db.execute("SELECT cash from users WHERE id = ?", session["user_id"])
    rows = db.execute("SELECT * from buy WHERE who_id = ?", session["user_id"])
    for rowz in rows:
        help += rowz["total"]
    jes = Current[0]["cash"] + help
    return render_template("index.html", current=Current, rows=rows, jes=jes)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    if request.method == "POST":
        symp = request.form.get("symbol")
        shar = request.form.get("shares")
        if not shar.isdigit():
            return apology("bro?")
        elif not float(shar).is_integer:
            return apology("bro?")
        elif not lookup(symp) or lookup(symp) == None or 0>int(shar):
            return apology("bro?")
        else:
            gg = lookup(symp)["price"]
            ggs = gg*int(shar)
            moni = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            if float(moni[0]["cash"]) - ggs<0:
                return apology("U NO ENUF MONI")
            else:
                sad = db.execute("SELECT symbol,share from buy WHERE who_id=? AND symbol=?", session["user_id"], symp)
                if not sad:
                    db.execute("INSERT INTO buy (who_id, symbol, price, share, total) VALUES(?, ?, ?, ?, ?)", session["user_id"], symp, lookup(symp)["price"], int(shar), ggs)
                    update = float(moni[0]["cash"]) - ggs
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", update, session["user_id"])
                    return redirect("/")
                else:
                    new = int(shar) + int(sad[0]["share"])
                    newer = new*gg
                    db.execute("UPDATE buy SET share = ? WHERE who_id=? AND symbol=?", new, session["user_id"], symp)
                    db.execute("UPDATE buy SET total = ? WHERE who_id=? AND symbol=?", newer, session["user_id"], symp)
                    update2 = float(moni[0]["cash"]) - ggs
                    db.execute("UPDATE users SET cash = ? WHERE id = ?", update2, session["user_id"])
                    return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

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
    if request.method == "GET":
        return render_template("quote.html")
    if request.method == "POST":
        sym = request.form.get("symbol")
        if lookup(sym) == None:
            return apology("cb what symbol")
        else:

            return render_template("quoted.html", bro=lookup(sym))



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        erow = db.execute("SELECT * FROM users")
        for row in erow:

            if request.form.get("username") == row["username"]:
                return apology("Username Taken")
        if not request.form.get("username") or not request.form.get("password") or request.form.get("password")!=request.form.get("confirmation"):
            return apology("Sorry :_(")
        else:
             name =  request.form.get("username")

             secret = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
             db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", name, secret)
             return redirect("/login")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    elol = db.execute("SELECT symbol from buy where who_id=?", session["user_id"])

    if request.method == "POST":
        simp = request.form.get("symbol")
        shat = request.form.get("shares")
        old = db.execute("SELECT share FROM buy WHERE who_id=? AND symbol = ?", session["user_id"], simp)
        moni = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        gg = lookup(simp)["price"]
        ggs = gg*int(shat)

        new = int(old[0]["share"]) - int(shat)
        if new>0 and int(shat)>0:
            newer = gg*new
            db.execute("UPDATE buy SET share = ? WHERE who_id=? AND symbol=?", new, session["user_id"], simp)
            db.execute("UPDATE buy SET total = ? WHERE who_id=? AND symbol=?", newer, session["user_id"], simp)
            update = float(moni[0]["cash"]) + ggs
            db.execute("UPDATE users SET cash = ? WHERE id = ?", update, session["user_id"])
            return redirect("/")
        else:
            return apology("sensational")




    elol = db.execute("SELECT symbol from buy where who_id=?", session["user_id"])
    return render_template("sell.html", elol=elol)



