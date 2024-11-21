from flask import Flask, request, render_template
from features.password_checker import verify_password_strength

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/password-checker", methods=["GET", "POST"])
def password_checker():
    result = None
    if request.method == "POST":
        password = request.form.get("password")
        result = verify_password_strength(password)
    return render_template("password_checker.html", result=result)

if __name__ == "__main__":
    app.run()