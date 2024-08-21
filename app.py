from flask import Flask, redirect, render_template, request, session
from flask_session import Session
app = Flask(__name__)

#a session cookie: ensures the cookie is deleted when you quit the browser
app.config["SESSION_PERMANENT"] = False
#the content is stored in the session's files, not in the cookie itself for provasy's sake
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html", name=session.get("name"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #session variable is a dictionary
        # gives an illusion that every user has their own session object
        session["name"] = request.form.get("name")
        return redirect("/")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)