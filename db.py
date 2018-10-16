import cx_Oracle as oracle

db = oracle.connect('tasy/redcross@DBTESTE')


def get_connection():
    if(db):
        return db
    return False


def busca_altas():
    cursor = db.cursor()
    query = ''' select nm_usuario,
                       ds_usuario,
                       obter_ds_setor_atendimento(cd_setor_atendimento) setor
                from usuario a
                where a.ie_situacao = 'A' '''
    print(query)
    result = cursor.execute(query)
    for re in result:
        print(re)


busca_altas()
