from models import Usuario, Ocorrencia, db

def cria_tabelas():
    db.create_tables([Usuario, Ocorrencia])


def cria_usuarios():
    usuarios = []
