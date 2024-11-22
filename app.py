from flask import Flask, request, render_template
from features.password_checker import verify_password_strength
from features.password_generator import generate_password

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


@app.route("/password-generator", methods=["GET", "POST"])
def password_generator():
    password = None
    if request.method == "POST":
        try:
            length = int(request.form.get("length"))
            numbers = request.form.get("numbers") is not None
            symbols = request.form.get("symbols") is not None
            password = generate_password(length, numbers, symbols)
        except ValueError:
            password = "Invalid input. Please enter a valid length."
    return render_template("password_generator.html", password=password)

if __name__ == "__main__":
    app.run()
