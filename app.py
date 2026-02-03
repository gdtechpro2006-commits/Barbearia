from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista simples para guardar agendamentos (banco de dados fake por enquanto)
agendamentos = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/agendar", methods=["POST"])
def agendar():
    nome = request.form["nome"]
    servico = request.form["servico"]
    data = request.form["data"]
    hora = request.form["hora"]

    agendamentos.append({
        "nome": nome,
        "servico": servico,
        "data": data,
        "hora": hora
    })

    return redirect("/agendamentos")

@app.route("/agendamentos")
def lista_agendamentos():
    return render_template("agendamentos.html", agendamentos=agendamentos)

if __name__ == "__main__":
    app.run(debug=True)