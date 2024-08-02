from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/contato')
def contato_page():
    return render_template('contato.html')

@app.route('/produtos')
def produtos_page():
    return render_template('produtos.html')

@app.route('/termos-de-uso')
def termos_de_uso_page():
    return render_template('termos-de-uso.html')

@app.route('/politica-de-privacidade')
def politica_de_privacidade_page():
    return render_template('politica-de-privacidade.html')

@app.route('/como-utilizar')
def como_utilizar_page():
    return render_template('como-utilizar.html')
