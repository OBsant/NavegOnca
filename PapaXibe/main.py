from flask import Flask, render_template, request

app = Flask(__name__)

""" Configurações para pagina de login/delete da aplicação """
# Apagar algo do banco de dados
@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template("list.html")
    else:
        return render_template("index.html")


"""Configurações para pagina de list da aplicação"""
# fazer um while com jinja que list todos os anúncios do banco de dados
@app.route("/")
def list():
    return render_template("list.html")


"""Configurações para pagina de cadastro da aplicação"""
# Salvar dados no banco de dados
@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        return render_template("list.html")
    else:
        return render_template("cadastrar.html")


"""Configurações para pagina de exibição da aplicação"""
# Mostrar os dados dos anúncios salvos no banco de dados
@app.route("/exibir")
def exibir():
    return render_template("exibir.html")

if __name__ == "__main__":
    app.run(debug=True)