import peewee

db = peewee.SqliteDatabase('banco.db')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Usuario(BaseModel):

    ''' Model for Users '''
    nm_usuario = peewee.CharField()
    ds_usuario = peewee.CharField()
    dt_registro = peewee.DateTimeField()
    