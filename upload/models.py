# # from upload.views.upload import db
# from .views import db
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy(views.app)


# class Table(db.Model):
#     id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column('nome', db.String(150))
#     cnpj_cpf = db.Column('cnpj_cpf', db.interger(15))
#     valor = db.Column('valor', db.String(150))
#     modalidade = db.Column('modalidade', db.String(20))
#     data_de_pagamento = db.Column('data_de_pagamento', db.Date, nullable=False)
#     quantidade_de_parcelas = db.Column(
#         'quantidade_de_parcelas', db.interger(15))

#     def __init__(self, nome, cnpj_cpf, valor, modalidade, data_de_pagamento, quantidade_de_parcelas):
#         self.nome = nome
#         self.cnpj_cpf = cnpj_cpf
#         self.valor = valor
#         self.modalidade = modalidade
#         self.data_de_pagamento = data_de_pagamento
#         self.quantidade_de_parcelas = quantidade_de_parcelas
