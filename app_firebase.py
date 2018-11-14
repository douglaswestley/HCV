import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('python-fireba.json')
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://python-fireba.firebaseio.com/',
})