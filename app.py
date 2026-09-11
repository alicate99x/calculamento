from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")


@app.route("/resultado")
def resultado():
    return render_template("resultado.html")


if __name__ == "__main__":
    app.run(debug=True)

