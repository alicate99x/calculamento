from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")

@app.route("/calcular", methods=["POST"])
def calcular():

    numero1 = float(request.form["numero1"])
    numero2 = float(request.form["numero2"])
    operacao = request.form["operacao"]

    if operacao == "soma":
        resultado = numero1 + numero2

    elif operacao == "subtracao":
        resultado = numero1 - numero2

    elif operacao == "multiplicacao":
        resultado = numero1 * numero2

    elif operacao == "divisao":
     if numero2 == 0:
         return "Não dá pra dividir."

     resultado = numero1 / numero2
    return render_template("resultado.html", resultado=resultado)

@app.route("/resultado")
def resultado():
    return render_template("resultado.html")

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        app.static_folder,
        "favicon.ico",
        mimetype="image/x-icon"
    )

if __name__ == "__main__":
    app.run(debug=True)
