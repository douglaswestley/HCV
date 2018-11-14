import firebase_admin
from firebase_admin import auth, credentials
import app_firebase


def criar_usuario(nome, email, senha):
    user = auth.create_user(
        email=email,
        email_verified=False,
        password=senha,
        display_name=nome,
        disabled=False
    )
    print(f"Usuário criado com sucesso : {user.uid}")


def get_list_users():
    for user in auth.list_users().iterate_all():
        print('User: ' + user.display_name)

def get_user_email(email):
    return auth.get_user_by_email(email)

def delete_user(uid):
    try:
        auth.delete_user(uid)
        print("Usuário excluido com sucesso!")
    except firebase_admin.auth.AuthError as e:
        print("Usuário não pode ser excluido ou não existe {0}".format(e))    


if __name__ == "__main__":
    #criar_usuario("Walicen", "walicen@gmail.com","123456789")
    
    get_list_users()
