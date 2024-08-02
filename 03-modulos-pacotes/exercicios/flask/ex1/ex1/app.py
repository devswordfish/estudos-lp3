from flask import Flask, render_template, redirect, url_for, request
from validate_docbr import CPF

app = Flask(__name__)

cpf = CPF()

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('home.html')
    
    if request.method == 'POST':
        num_cpf = int(request.form['input-cpf'])

        return redirect(url_for('CPF_page', n=num_cpf))
    
    raise Exception(f'Invalid {request.method} method in home_page()')

@app.route('/cpf/<int:n>', methods=['GET'])
def CPF_page(n):
    cpf_list = cpf.generate_list(n, mask=True)

    return render_template('CPF.html', cpf_list=cpf_list)
