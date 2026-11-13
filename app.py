
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():

    mensagem = ""

    if request.method == "POST":

        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")

        if usuario == "admin" and senha == "1234":
            mensagem = "Login realizado com sucesso!"
        else:
            mensagem = "Usuário ou senha incorretos!"

    return render_template("login.html", mensagem=mensagem)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    mensagem = ""

    if request.method == "POST":

        nome = request.form.get("nome", "")
        email = request.form.get("email", "")
        usuario = request.form.get("usuario", "")
        senha = request.form.get("senha", "")

        mensagem = f"Cadastro realizado para {nome}!"

    return render_template("cadastro.html", mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)
