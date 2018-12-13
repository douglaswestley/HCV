import app_firebase
from firebase_admin import db


ref = db.reference('/')
produtos = ref.child('produtos')


def update_user(user):
    users  = ref.child('users')
    users.child(user).set(
        {
        'name': 'Walicen Dalazuana',
        'dt_nasc': '30/06/1993',
        'email': 'walicen.r@gmail.com',
        'status': 'A'
        }
    )
