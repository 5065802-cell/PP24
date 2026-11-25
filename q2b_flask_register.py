from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"<h3>Registered!</h3><p>Name: {name}</p><p>Email: {email}</p>"
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
