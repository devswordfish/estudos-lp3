from flask import Flask, render_template, redirect, url_for, request
from validate_docbr import CNPJ

app = Flask(__name__)

cnpj = CNPJ()

@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
        return render_template('home.html')
    
    if request.method == 'POST':
        num_cnpj = int(request.form['input-cnpj'])

        return redirect(url_for('CNPJ_page', n=num_cnpj))
    
    raise Exception(f'Invalid {request.method} method in home_page()')

@app.route('/cnpj/<int:n>', methods=['GET'])
def CNPJ_page(n):
    cnpj_list = cnpj.generate_list(n, mask=True)

    return render_template('CNPJ.html', cnpj_list=cnpj_list)
