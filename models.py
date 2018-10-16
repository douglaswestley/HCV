import peewee as p

db = p.SqliteDatabase('banco.db')

class BaseModel(p.Model):
    class Meta:
        database = db

class Usuario(BaseModel):

    ''' Model for Users '''
    nm_usuario = p.CharField()
    ds_usuario = p.CharField()
    dt_registro = p.DateTimeField()


class Ocorrencia(BaseModel):

    cd_usuario = p.ForeignKeyField(Usuario, backref='cd_user')
    reclamacao = p.TextField()



    
    