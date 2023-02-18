from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import pandas as pd

app = Flask(__name__, template_folder='C:/flask_excel/upload/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Table.sqlite3'
db = SQLAlchemy(app)
app.app_context().push()


class Table(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(150))
    cnpj_cpf = db.Column('cnpj_cpf', db.Integer)
    valor = db.Column('valor', db.String(150))
    modalidade = db.Column('modalidade', db.String(20))
    data_de_pagamento = db.Column(
        'data_de_pagamento', db.String(100), nullable=False)
    quantidade_de_parcelas = db.Column(
        'quantidade_de_parcelas', db.Integer)

    def __init__(self, nome, cnpj_cpf, valor, modalidade, data_de_pagamento, quantidade_de_parcelas):
        self.nome = nome
        self.cnpj_cpf = cnpj_cpf
        self.valor = valor
        self.modalidade = modalidade
        self.data_de_pagamento = data_de_pagamento
        self.quantidade_de_parcelas = quantidade_de_parcelas


@app.route('/')
def Home():
    band = Table.query.all()
    return render_template('home.html', banda=band)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Verifica se o arquivo foi enviado pelo usuário
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        # Verifica se o arquivo é uma planilha do Excel
        if file and file.filename.endswith('.xlsx'):
            df = pd.read_excel(file)
            

            # Converte os dados do arquivo em um dicionário para serem exibidos no template
            data = df.to_dict('records')
                 
            # Exibe os dados do arquivo no template de edição
            return render_template('upload.html', data=data)

    # Exibe o formulário para enviar o arquivo
    return render_template('upload.html')


@app.route('/Add', methods=['GET', 'POST'])
def Add():
    #dicionario que vai ser usado pra armazenar os valores das chaves
    valores = {'nome': [], 'cnpj_cpf': [],
               'valor': [], 'modalidade': [], 'data_de_pagamento': [], 'quantidade_de_parcelas': [], }
    
    lista = list(request.form)
    
    for i in lista:
       
        objetos = request.form.getlist(i)
        
        valores[i].append(objetos)
    
    if request.method == 'POST':
      
        for i in range(len(valores['nome'][0])):
            
            tabela = Table(valores['nome'][0][i],
                           valores['cnpj_cpf'][0][i],
                           valores['valor'][0][i],
                           valores['modalidade'][0][i],
                           str(valores['data_de_pagamento'][0][i]),
                           valores['quantidade_de_parcelas'][0][i])

            db.session.add(tabela)
            db.session.commit()
        return redirect(url_for('Home'))
     
    return render_template('home.html')

# atualizando informações das bandas
@app.route('/Update/<int:id>', methods=["GET", "POST"])
def Update(id):
    table = Table.query.get(id)
    if request.method == "POST":
        table.nome = request.form['nome']
        table.cnpj_cpf = request.form['cnpj_cpf']
        table.valor = request.form['valor']
        table.modalidade = request.form['modalidade']
        table.data_de_pagamento = request.form['data_de_pagamento']
        table.quantidade_de_parcelas = request.form['quantidade_de_parcelas']
        db.session.commit()
        return redirect(url_for('Home'))

    return render_template('edit.html', table=table)


@app.route('/Del/<int:id>')
def Del(id):
    table = Table.query.get(id)
    db.session.delete(table)
    db.session.commit()
    return redirect(url_for('Home'))


