from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Flask tutorial</h1>"
    
@app.route("/<name>")
def user(name):
    return f"<h1>Welcome {name}</h1>"

@app.route("/admin")
def admin():
    return (redirect(url_for("home")))

if __name__ == "__main__":
    app.run(debug=True)
