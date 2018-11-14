import app_firebase
from firebase_admin import db


ref = db.reference('/')
produtos = ref.child('produtos')
users  = ref.child('users')

""" produtos.child('5').set(
    {
    'codigo': 'prd05',
     'nome': 'Bolinho',
     'preco': 1,
     'status': 'A'
    }
) """


users.child('Walicen').set(
    {
    'name': 'Walicen Dalazuana',
    'dt_nasc': '30/06/1993',
    'email': 'walicen.r@gmail.com',
    'status': 'A'
    }
) 

print(users.get())